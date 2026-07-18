from collections.abc import Generator
from datetime import datetime, timedelta, timezone
from unittest.mock import patch
from uuid import uuid4

import jwt
import pytest
from fastapi.testclient import TestClient
from passlib.context import CryptContext
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app import models  # noqa: F401
from app.core.config import get_settings
from app.core.security import verify_password
from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.models.user import User
from app.services.auth_service import DUMMY_PASSWORD_HASH


@pytest.fixture()
def db_session() -> Generator[Session, None, None]:
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    testing_session_local = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    Base.metadata.create_all(bind=engine)

    db = testing_session_local()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
        engine.dispose()


@pytest.fixture()
def client(db_session: Session) -> Generator[TestClient, None, None]:
    def override_get_db() -> Generator[Session, None, None]:
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def test_register_user_success(client: TestClient, db_session: Session) -> None:
    payload = {
        "name": "Gabriel",
        "email": "gabriel@example.com",
        "password": "strong-password",
    }

    response = client.post("/api/v1/auth/register", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert data["is_active"] is True
    assert "password" not in data
    assert "password_hash" not in data

    user = db_session.scalar(select(User).where(User.email == payload["email"]))
    assert user is not None
    assert user.password_hash != payload["password"]
    assert user.password_hash.startswith("$bcrypt-sha256$")


def test_password_verification_accepts_legacy_bcrypt() -> None:
    legacy_hash = CryptContext(schemes=["bcrypt"]).hash("legacy-password")

    assert verify_password("legacy-password", legacy_hash) is True


def test_login_rehashes_legacy_bcrypt_password(
    client: TestClient,
    db_session: Session,
) -> None:
    email = "legacy-hash@example.com"
    password = "legacy-password"
    client.post(
        "/api/v1/auth/register",
        json={"name": "Legacy Hash", "email": email, "password": password},
    )
    user = db_session.scalar(select(User).where(User.email == email))
    assert user is not None
    user.password_hash = CryptContext(schemes=["bcrypt"]).hash(password)
    db_session.commit()

    response = client.post(
        "/api/v1/auth/login",
        data={"username": email, "password": password},
    )

    db_session.refresh(user)
    assert response.status_code == 200
    assert user.password_hash.startswith("$bcrypt-sha256$")


def test_register_and_login_support_128_character_password(
    client: TestClient,
) -> None:
    password = "p" * 128
    register_response = client.post(
        "/api/v1/auth/register",
        json={
            "name": "Long Password",
            "email": "long-password@example.com",
            "password": password,
        },
    )
    login_response = client.post(
        "/api/v1/auth/login",
        data={"username": "long-password@example.com", "password": password},
    )

    assert register_response.status_code == 201
    assert login_response.status_code == 200


def test_login_rejects_password_above_registration_limit(
    client: TestClient,
) -> None:
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "missing@example.com",
            "password": "p" * 129,
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"


def test_register_duplicate_email_returns_conflict(client: TestClient) -> None:
    payload = {
        "name": "Gabriel",
        "email": "gabriel@example.com",
        "password": "strong-password",
    }

    first_response = client.post("/api/v1/auth/register", json=payload)
    duplicate_response = client.post("/api/v1/auth/register", json=payload)

    assert first_response.status_code == 201
    assert duplicate_response.status_code == 409
    assert duplicate_response.json()["detail"] == "Email already registered"


def test_login_oauth2_form_success_returns_token(client: TestClient) -> None:
    register_payload = {
        "name": "Gabriel",
        "email": "gabriel@example.com",
        "password": "strong-password",
    }
    login_payload = {
        "username": register_payload["email"],
        "password": register_payload["password"],
    }

    client.post("/api/v1/auth/register", json=register_payload)
    response = client.post("/api/v1/auth/login", data=login_payload)

    assert response.status_code == 200
    data = response.json()
    assert data["access_token"]
    assert data["token_type"] == "bearer"


def test_login_wrong_password_returns_unauthorized(client: TestClient) -> None:
    register_payload = {
        "name": "Gabriel",
        "email": "gabriel@example.com",
        "password": "strong-password",
    }

    client.post("/api/v1/auth/register", json=register_payload)
    response = client.post(
        "/api/v1/auth/login",
        data={"username": register_payload["email"], "password": "wrong-password"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"


def test_login_unknown_email_uses_generic_error(client: TestClient) -> None:
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "missing@example.com", "password": "wrong-password"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"


def test_login_unknown_email_still_verifies_a_dummy_hash(client: TestClient) -> None:
    with patch(
        "app.services.auth_service.verify_and_update_password",
        return_value=(False, None),
    ) as verify_password_mock:
        response = client.post(
            "/api/v1/auth/login",
            data={"username": "missing@example.com", "password": "wrong-password"},
        )

    assert response.status_code == 401
    verify_password_mock.assert_called_once_with(
        "wrong-password",
        DUMMY_PASSWORD_HASH,
    )


def test_me_returns_current_user_with_valid_token(client: TestClient) -> None:
    register_payload = {
        "name": "Gabriel",
        "email": "gabriel@example.com",
        "password": "strong-password",
    }

    register_response = client.post("/api/v1/auth/register", json=register_payload)
    login_response = client.post(
        "/api/v1/auth/login",
        data={
            "username": register_payload["email"],
            "password": register_payload["password"],
        },
    )
    token = login_response.json()["access_token"]

    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json() == register_response.json()
    assert "password_hash" not in response.json()


def test_me_without_token_returns_unauthorized(client: TestClient) -> None:
    response = client.get("/api/v1/auth/me")

    assert response.status_code == 401


def test_me_with_invalid_token_returns_unauthorized(client: TestClient) -> None:
    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": "Bearer invalid-token"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"


@pytest.mark.parametrize(
    "payload,secret,algorithm",
    [
        (
            {"sub": str(uuid4()), "exp": datetime.now(timezone.utc) - timedelta(seconds=1)},
            None,
            "HS256",
        ),
        ({"sub": str(uuid4())}, None, "HS256"),
        (
            {"sub": "not-a-uuid", "exp": datetime.now(timezone.utc) + timedelta(minutes=5)},
            None,
            "HS256",
        ),
        (
            {"sub": str(uuid4()), "exp": datetime.now(timezone.utc) + timedelta(minutes=5)},
            "different-test-secret-that-is-at-least-sixty-four-bytes-long-0002",
            "HS256",
        ),
        (
            {"sub": str(uuid4()), "exp": datetime.now(timezone.utc) + timedelta(minutes=5)},
            None,
            "HS384",
        ),
    ],
    ids=["expired", "missing-exp", "invalid-sub", "wrong-secret", "wrong-algorithm"],
)
def test_me_rejects_invalid_token_variants(
    client: TestClient,
    payload: dict[str, object],
    secret: str | None,
    algorithm: str,
) -> None:
    settings = get_settings()
    token = jwt.encode(
        payload,
        secret or settings.SECRET_KEY,
        algorithm=algorithm,
    )

    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"
