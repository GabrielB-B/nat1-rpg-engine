import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from app.core.config import Settings
from app.core.security import create_access_token, decode_access_token
from app.main import app, create_app


PRODUCTION_DATABASE_URL = (
    "postgresql+psycopg://nat1_app:test-password@db.nat1.example/nat1"
)


def test_settings_require_explicit_environment_and_secret(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("ENVIRONMENT", raising=False)
    monkeypatch.delenv("SECRET_KEY", raising=False)

    with pytest.raises(ValidationError, match="ENVIRONMENT"):
        Settings(_env_file=None)  # type: ignore[call-arg]


def test_settings_allow_placeholder_secret_only_for_local_environment() -> None:
    local_settings = Settings(
        ENVIRONMENT="local",
        SECRET_KEY="replace-with-local-development-secret",
    )

    assert local_settings.SECRET_KEY == "replace-with-local-development-secret"


def test_settings_reject_placeholder_secret_outside_local_environment() -> None:
    with pytest.raises(ValidationError, match="SECRET_KEY"):
        Settings(
            ENVIRONMENT="production",
            SECRET_KEY="replace-with-local-development-secret",
        )


def test_settings_require_strong_secret_outside_local_environment() -> None:
    with pytest.raises(ValidationError, match="at least 32 characters"):
        Settings(
            ENVIRONMENT="production",
            SECRET_KEY="short-production-secret",
            DATABASE_URL=PRODUCTION_DATABASE_URL,
            BACKEND_CORS_ORIGINS=["https://app.nat1.example"],
        )


@pytest.mark.parametrize(
    "origin",
    [
        "http://app.nat1.example",
        "http://localhost:3000",
        "https://127.0.0.2:8000",
        "https://[::1]:5173",
    ],
)
def test_settings_reject_insecure_or_loopback_cors_in_production(
    origin: str,
) -> None:
    with pytest.raises(ValidationError, match="HTTPS and non-loopback"):
        Settings(
            ENVIRONMENT="production",
            SECRET_KEY="s" * 32,
            DATABASE_URL=PRODUCTION_DATABASE_URL,
            BACKEND_CORS_ORIGINS=[origin],
        )


def test_settings_accept_production_security_configuration() -> None:
    settings = Settings(
        ENVIRONMENT="production",
        SECRET_KEY="s" * 32,
        DATABASE_URL=PRODUCTION_DATABASE_URL,
        BACKEND_CORS_ORIGINS=["https://app.nat1.example"],
        ACCESS_TOKEN_EXPIRE_MINUTES=30,
    )

    assert settings.BACKEND_CORS_ORIGINS == ["https://app.nat1.example"]


def test_settings_reject_documented_local_database_credentials_in_production() -> None:
    with pytest.raises(ValidationError, match="DATABASE_URL"):
        Settings(
            ENVIRONMENT="production",
            SECRET_KEY="s" * 32,
            DATABASE_URL=(
                "postgresql+psycopg://nat1_user:nat1_password@localhost:5432/nat1_db"
            ),
            BACKEND_CORS_ORIGINS=["https://app.nat1.example"],
        )


def test_settings_reject_invalid_token_expiration() -> None:
    with pytest.raises(ValidationError, match="ACCESS_TOKEN_EXPIRE_MINUTES"):
        Settings(ACCESS_TOKEN_EXPIRE_MINUTES=0)


def test_settings_reject_non_http_cors_origin() -> None:
    with pytest.raises(ValidationError, match="valid origins"):
        Settings(BACKEND_CORS_ORIGINS="ftp://example.com")


def test_settings_normalize_cors_origin_and_reject_paths() -> None:
    settings = Settings(BACKEND_CORS_ORIGINS="https://app.nat1.example/")

    assert settings.BACKEND_CORS_ORIGINS == ["https://app.nat1.example"]

    with pytest.raises(ValidationError, match="without paths"):
        Settings(BACKEND_CORS_ORIGINS="https://app.nat1.example/private")


def test_api_adds_baseline_security_headers() -> None:
    with TestClient(app) as client:
        response = client.get("/api/v1/health")

    assert response.headers["x-content-type-options"] == "nosniff"
    assert response.headers["x-frame-options"] == "DENY"
    assert response.headers["referrer-policy"] == "strict-origin-when-cross-origin"
    assert response.headers["permissions-policy"] == (
        "camera=(), geolocation=(), microphone=()"
    )


def test_access_token_round_trip_requires_subject_and_expiration() -> None:
    token = create_access_token("test-subject")
    payload = decode_access_token(token)

    assert payload["sub"] == "test-subject"
    assert isinstance(payload["exp"], int)


def test_cors_allows_configured_origin_without_cookie_credentials() -> None:
    configured_origin = "http://127.0.0.1:5173"
    test_app = create_app(
        Settings(
            ENVIRONMENT="testing",
            DATABASE_URL="sqlite+pysqlite:///:memory:",
            SECRET_KEY="test-only-secret-that-is-long-enough-for-hs256",
            BACKEND_CORS_ORIGINS=[configured_origin],
        )
    )

    with TestClient(test_app) as client:
        response = client.options(
            "/api/v1/health",
            headers={
                "Origin": configured_origin,
                "Access-Control-Request-Method": "GET",
                "Access-Control-Request-Headers": "Authorization",
            },
        )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == configured_origin
    assert "access-control-allow-credentials" not in response.headers
    assert response.headers["x-content-type-options"] == "nosniff"
    assert response.headers["x-frame-options"] == "DENY"
    assert response.headers["referrer-policy"] == "strict-origin-when-cross-origin"
    assert response.headers["permissions-policy"] == (
        "camera=(), geolocation=(), microphone=()"
    )
