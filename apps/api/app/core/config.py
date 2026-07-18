from functools import lru_cache
from ipaddress import ip_address
import json
from urllib.parse import urlparse

from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


LOCAL_DATABASE_URL = (
    "postgresql+psycopg://nat1_user:nat1_password@localhost:5432/nat1_db"
)


class Settings(BaseSettings):
    APP_NAME: str = "Nat 1 RPG Engine API"
    ENVIRONMENT: str = Field(min_length=1)
    DATABASE_URL: str = Field(min_length=1)
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]
    SECRET_KEY: str = Field(min_length=1)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60, gt=0, le=1440)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, value: str | list[str]) -> list[str]:
        if isinstance(value, str):
            value = value.strip()
            if not value:
                origins: list[str] = []
            elif value.startswith("["):
                parsed = json.loads(value)
                if isinstance(parsed, list):
                    origins = [str(origin) for origin in parsed]
                else:
                    raise ValueError(
                        "BACKEND_CORS_ORIGINS must be a list of origins"
                    )
            else:
                origins = [
                    origin.strip() for origin in value.split(",") if origin.strip()
                ]
        else:
            origins = value

        normalized_origins: list[str] = []
        for raw_origin in origins:
            origin = str(raw_origin).strip().rstrip("/")
            parsed_origin = urlparse(origin)
            if (
                parsed_origin.scheme not in {"http", "https"}
                or not parsed_origin.netloc
                or parsed_origin.path
                or parsed_origin.params
                or parsed_origin.query
                or parsed_origin.fragment
                or parsed_origin.username is not None
                or parsed_origin.password is not None
            ):
                raise ValueError(
                    "BACKEND_CORS_ORIGINS must contain valid origins without paths or credentials"
                )
            normalized_origins.append(origin)

        return normalized_origins

    @model_validator(mode="after")
    def validate_security_configuration(self) -> "Settings":
        local_environments = {"local", "development", "dev", "test", "testing"}
        placeholder_secrets = {
            "change-me-in-local-env",
            "replace-with-local-development-secret",
        }

        if self.ENVIRONMENT.lower() not in local_environments:
            if self.SECRET_KEY in placeholder_secrets or len(self.SECRET_KEY) < 32:
                raise ValueError(
                    "SECRET_KEY must contain at least 32 characters outside local environments"
                )

            if self.DATABASE_URL == LOCAL_DATABASE_URL:
                raise ValueError(
                    "DATABASE_URL must not use the documented local credentials outside local environments"
                )

            for origin in self.BACKEND_CORS_ORIGINS:
                parsed_origin = urlparse(origin)
                hostname = (parsed_origin.hostname or "").lower().rstrip(".")
                is_loopback = hostname == "localhost" or hostname.endswith(
                    ".localhost"
                )

                try:
                    is_loopback = is_loopback or ip_address(hostname).is_loopback
                except ValueError:
                    pass

                if parsed_origin.scheme != "https" or is_loopback:
                    raise ValueError(
                        "BACKEND_CORS_ORIGINS must use HTTPS and non-loopback hosts outside local environments"
                    )

        return self


@lru_cache
def get_settings() -> Settings:
    return Settings()
