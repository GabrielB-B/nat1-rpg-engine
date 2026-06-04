from functools import lru_cache
import json

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Nat 1 RPG Engine API"
    ENVIRONMENT: str = "local"
    DATABASE_URL: str = "postgresql+psycopg://nat1:nat1@localhost:5432/nat1"
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]
    SECRET_KEY: str = "change-me-in-local-env"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

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
                return []
            if value.startswith("["):
                parsed = json.loads(value)
                if isinstance(parsed, list):
                    return [str(origin) for origin in parsed]
                raise ValueError("BACKEND_CORS_ORIGINS must be a list of origins")
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()
