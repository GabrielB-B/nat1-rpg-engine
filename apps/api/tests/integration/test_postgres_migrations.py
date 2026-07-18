from collections.abc import Generator
import os
from uuid import uuid4

import pytest
from alembic.config import Config as AlembicConfig
from alembic.script import ScriptDirectory
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine, inspect, text
from sqlalchemy.orm import Session, sessionmaker

from app.db.session import get_db
from app.main import app


pytestmark = pytest.mark.skipif(
    os.getenv("RUN_POSTGRES_INTEGRATION") != "1",
    reason="PostgreSQL integration tests require RUN_POSTGRES_INTEGRATION=1",
)


@pytest.fixture()
def postgres_engine() -> Generator[Engine, None, None]:
    database_url = os.environ["DATABASE_URL"]
    engine = create_engine(database_url, pool_pre_ping=True)
    try:
        yield engine
    finally:
        engine.dispose()


@pytest.fixture()
def postgres_session(postgres_engine: Engine) -> Generator[Session, None, None]:
    connection = postgres_engine.connect()
    outer_transaction = connection.begin()
    testing_session_local = sessionmaker(
        bind=connection,
        expire_on_commit=False,
        join_transaction_mode="create_savepoint",
    )
    session = testing_session_local()

    try:
        yield session
    finally:
        session.close()
        outer_transaction.rollback()
        connection.close()


def test_migrated_postgres_schema_supports_authenticated_project_lifecycle(
    postgres_engine: Engine,
    postgres_session: Session,
) -> None:
    expected_tables = {
        "alembic_version",
        "game_projects",
        "project_module_settings",
        "system_templates",
        "users",
        "worlds",
    }
    assert expected_tables.issubset(set(inspect(postgres_engine).get_table_names()))

    with postgres_engine.connect() as connection:
        revision = connection.scalar(text("SELECT version_num FROM alembic_version"))
    expected_revision = ScriptDirectory.from_config(
        AlembicConfig("alembic.ini")
    ).get_current_head()
    assert expected_revision is not None
    assert revision == expected_revision

    def override_get_db() -> Generator[Session, None, None]:
        yield postgres_session

    unique_suffix = uuid4().hex
    email = f"postgres-{unique_suffix}@example.com"
    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as client:
            register_response = client.post(
                "/api/v1/auth/register",
                json={
                    "name": "PostgreSQL Gate",
                    "email": email,
                    "password": "strong-password",
                },
            )
            assert register_response.status_code == 201

            login_response = client.post(
                "/api/v1/auth/login",
                data={"username": email, "password": "strong-password"},
            )
            assert login_response.status_code == 200
            token = login_response.json()["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            create_response = client.post(
                "/api/v1/game-projects",
                headers=headers,
                json={
                    "name": "Campanha PostgreSQL",
                    "format": "Campanha",
                    "metadata_json": {"validated_by": "postgres-integration"},
                },
            )
            assert create_response.status_code == 201
            project_id = create_response.json()["id"]

            get_response = client.get(
                f"/api/v1/game-projects/{project_id}",
                headers=headers,
            )
            update_response = client.patch(
                f"/api/v1/game-projects/{project_id}",
                headers=headers,
                json={"name": "Campanha PostgreSQL Revisada"},
            )
            list_response = client.get(
                "/api/v1/game-projects",
                headers=headers,
            )
            archive_response = client.post(
                f"/api/v1/game-projects/{project_id}/archive",
                headers=headers,
            )
            active_after_archive_response = client.get(
                "/api/v1/game-projects",
                headers=headers,
            )
            archived_response = client.get(
                "/api/v1/game-projects?include_archived=true",
                headers=headers,
            )
            restore_response = client.post(
                f"/api/v1/game-projects/{project_id}/restore",
                headers=headers,
            )

        assert get_response.status_code == 200
        assert update_response.status_code == 200
        assert update_response.json()["name"] == "Campanha PostgreSQL Revisada"
        assert list_response.status_code == 200
        assert archive_response.status_code == 200
        assert archive_response.json()["archived_at"] is not None
        assert active_after_archive_response.status_code == 200
        assert active_after_archive_response.json() == []
        assert archived_response.status_code == 200
        assert [project["id"] for project in archived_response.json()] == [project_id]
        assert restore_response.status_code == 200
        assert restore_response.json()["archived_at"] is None
        assert create_response.json()["metadata_json"] == {
            "validated_by": "postgres-integration"
        }
        assert [project["id"] for project in list_response.json()] == [project_id]
    finally:
        app.dependency_overrides.clear()
