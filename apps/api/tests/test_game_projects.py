from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app import models  # noqa: F401
from app.db.base import Base
from app.db.session import get_db
from app.main import app


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


def test_create_game_project_success(client: TestClient) -> None:
    token = register_and_login_user(client, email="owner@example.com")

    response = client.post(
        "/api/v1/game-projects",
        json={
            "name": "Aelthos - A Dama de Ferro",
            "format": "Campanha",
            "description": "Primeira campanha oficial do teste.",
        },
        headers=auth_headers(token),
    )

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Aelthos - A Dama de Ferro"
    assert data["slug"] == "aelthos-a-dama-de-ferro"
    assert data["format"] == "Campanha"
    assert data["status"] == "preparation"
    assert data["theme"] == "cartographer"
    assert data["metadata_json"] == {}
    assert data["archived_at"] is None
    assert {setting["module_key"] for setting in data["module_settings"]} == {
        "overview",
        "sessions",
        "scenes",
        "characters_creatures",
        "locations_atlas",
        "organizations_factions",
        "documents",
        "notes",
        "relationships",
        "settings",
    }


def test_create_game_project_requires_authentication(client: TestClient) -> None:
    response = client.post(
        "/api/v1/game-projects",
        json={"name": "Sem Dono", "format": "Campanha"},
    )

    assert response.status_code == 401


def test_list_game_projects_only_returns_current_user_projects(
    client: TestClient,
) -> None:
    owner_token = register_and_login_user(client, email="owner@example.com")
    other_token = register_and_login_user(client, email="other@example.com")

    owner_project = create_game_project(
        client,
        token=owner_token,
        name="Projeto do Dono",
    )
    create_game_project(client, token=other_token, name="Projeto de Outra Pessoa")

    response = client.get(
        "/api/v1/game-projects",
        headers=auth_headers(owner_token),
    )

    assert response.status_code == 200
    projects = response.json()
    assert [project["id"] for project in projects] == [owner_project["id"]]


def test_user_cannot_access_another_users_game_project(client: TestClient) -> None:
    owner_token = register_and_login_user(client, email="owner@example.com")
    other_token = register_and_login_user(client, email="other@example.com")
    other_project = create_game_project(
        client,
        token=other_token,
        name="Projeto Privado",
    )

    response = client.get(
        f"/api/v1/game-projects/{other_project['id']}",
        headers=auth_headers(owner_token),
    )

    assert response.status_code == 404


def test_update_game_project_for_owner(client: TestClient) -> None:
    token = register_and_login_user(client, email="owner@example.com")
    project = create_game_project(client, token=token, name="Nome Inicial")

    response = client.patch(
        f"/api/v1/game-projects/{project['id']}",
        json={
            "name": "Nome Atualizado",
            "description": "Descricao revisada.",
            "status": "active",
            "metadata_json": {"display_labels": {"project": "Cronica"}},
        },
        headers=auth_headers(token),
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Nome Atualizado"
    assert data["slug"] == "nome-inicial"
    assert data["description"] == "Descricao revisada."
    assert data["status"] == "active"
    assert data["metadata_json"] == {"display_labels": {"project": "Cronica"}}


def test_archive_hides_project_from_default_list(client: TestClient) -> None:
    token = register_and_login_user(client, email="owner@example.com")
    project = create_game_project(client, token=token, name="Projeto Arquivado")

    archive_response = client.post(
        f"/api/v1/game-projects/{project['id']}/archive",
        headers=auth_headers(token),
    )
    default_list_response = client.get(
        "/api/v1/game-projects",
        headers=auth_headers(token),
    )
    archived_list_response = client.get(
        "/api/v1/game-projects",
        params={"include_archived": True},
        headers=auth_headers(token),
    )

    assert archive_response.status_code == 200
    assert archive_response.json()["status"] == "archived"
    assert archive_response.json()["archived_at"] is not None
    assert default_list_response.status_code == 200
    assert default_list_response.json() == []
    assert archived_list_response.status_code == 200
    assert [item["id"] for item in archived_list_response.json()] == [project["id"]]


def test_restore_readds_project_to_default_list(client: TestClient) -> None:
    token = register_and_login_user(client, email="owner@example.com")
    project = create_game_project(client, token=token, name="Projeto Restaurado")
    client.post(
        f"/api/v1/game-projects/{project['id']}/archive",
        headers=auth_headers(token),
    )

    restore_response = client.post(
        f"/api/v1/game-projects/{project['id']}/restore",
        headers=auth_headers(token),
    )
    list_response = client.get(
        "/api/v1/game-projects",
        headers=auth_headers(token),
    )

    assert restore_response.status_code == 200
    assert restore_response.json()["status"] == "preparation"
    assert restore_response.json()["archived_at"] is None
    assert [item["id"] for item in list_response.json()] == [project["id"]]


def test_duplicate_names_generate_unique_slugs_for_same_user(
    client: TestClient,
) -> None:
    token = register_and_login_user(client, email="owner@example.com")

    first_project = create_game_project(client, token=token, name="Mesa Teste")
    second_project = create_game_project(client, token=token, name="Mesa Teste")

    assert first_project["slug"] == "mesa-teste"
    assert second_project["slug"] == "mesa-teste-2"


def register_and_login_user(client: TestClient, *, email: str) -> str:
    password = "strong-password"
    register_response = client.post(
        "/api/v1/auth/register",
        json={
            "name": "Gabriel",
            "email": email,
            "password": password,
        },
    )
    assert register_response.status_code == 201

    login_response = client.post(
        "/api/v1/auth/login",
        data={"username": email, "password": password},
    )
    assert login_response.status_code == 200
    return str(login_response.json()["access_token"])


def create_game_project(
    client: TestClient,
    *,
    token: str,
    name: str,
) -> dict:
    response = client.post(
        "/api/v1/game-projects",
        json={"name": name, "format": "Campanha"},
        headers=auth_headers(token),
    )
    assert response.status_code == 201
    return dict(response.json())


def auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}
