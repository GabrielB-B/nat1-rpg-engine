from collections.abc import Generator
from typing import Any

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app import models  # noqa: F401
from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.models.system_template import SystemTemplate


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


def test_worlds_are_user_scoped_and_support_archive_restore(
    client: TestClient,
) -> None:
    owner_token = register_and_login_user(client, email="owner@example.com")
    other_token = register_and_login_user(client, email="other@example.com")

    owner_world = create_world(client, token=owner_token, name="Aelthos")
    create_world(client, token=other_token, name="Outro Mundo")

    list_response = client.get("/api/v1/worlds", headers=auth_headers(owner_token))
    other_access_response = client.get(
        f"/api/v1/worlds/{owner_world['id']}",
        headers=auth_headers(other_token),
    )
    archive_response = client.post(
        f"/api/v1/worlds/{owner_world['id']}/archive",
        headers=auth_headers(owner_token),
    )
    default_list_response = client.get(
        "/api/v1/worlds",
        headers=auth_headers(owner_token),
    )
    archived_list_response = client.get(
        "/api/v1/worlds",
        params={"include_archived": True},
        headers=auth_headers(owner_token),
    )
    restore_response = client.post(
        f"/api/v1/worlds/{owner_world['id']}/restore",
        headers=auth_headers(owner_token),
    )

    assert list_response.status_code == 200
    assert [world["id"] for world in list_response.json()] == [owner_world["id"]]
    assert other_access_response.status_code == 404
    assert archive_response.status_code == 200
    assert archive_response.json()["status"] == "archived"
    assert archive_response.json()["archived_at"] is not None
    assert default_list_response.json() == []
    assert [world["id"] for world in archived_list_response.json()] == [
        owner_world["id"]
    ]
    assert restore_response.status_code == 200
    assert restore_response.json()["status"] == "active"
    assert restore_response.json()["archived_at"] is None


def test_world_create_requires_authentication(client: TestClient) -> None:
    response = client.post("/api/v1/worlds", json={"name": "Sem Dono"})

    assert response.status_code == 401


def test_world_update_works_for_owner(client: TestClient) -> None:
    token = register_and_login_user(client, email="owner@example.com")
    world = create_world(client, token=token, name="Nome Antigo")

    response = client.patch(
        f"/api/v1/worlds/{world['id']}",
        json={
            "name": "Nome Novo",
            "description": "Worldbuilding revisado.",
            "metadata_json": {"tone": "dark fantasy"},
        },
        headers=auth_headers(token),
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Nome Novo"
    assert response.json()["slug"] == "nome-antigo"
    assert response.json()["metadata_json"] == {"tone": "dark fantasy"}


def test_system_templates_are_user_scoped_and_builtin_is_protected(
    client: TestClient,
    db_session: Session,
) -> None:
    builtin_template = create_builtin_system_template(db_session)
    owner_token = register_and_login_user(client, email="owner@example.com")
    other_token = register_and_login_user(client, email="other@example.com")

    owner_template = create_system_template(
        client,
        token=owner_token,
        name="Sistema Autoral",
    )
    other_template = create_system_template(
        client,
        token=other_token,
        name="Sistema Privado",
    )

    list_response = client.get(
        "/api/v1/system-templates",
        headers=auth_headers(owner_token),
    )
    private_get_response = client.get(
        f"/api/v1/system-templates/{other_template['id']}",
        headers=auth_headers(owner_token),
    )
    private_patch_response = client.patch(
        f"/api/v1/system-templates/{other_template['id']}",
        json={"name": "Tentativa"},
        headers=auth_headers(owner_token),
    )
    builtin_patch_response = client.patch(
        f"/api/v1/system-templates/{builtin_template.id}",
        json={"name": "D&D Editado"},
        headers=auth_headers(owner_token),
    )

    assert list_response.status_code == 200
    assert {template["id"] for template in list_response.json()} == {
        str(builtin_template.id),
        owner_template["id"],
    }
    assert private_get_response.status_code == 404
    assert private_patch_response.status_code == 404
    assert builtin_patch_response.status_code == 403


def test_system_template_create_update_and_archive(client: TestClient) -> None:
    token = register_and_login_user(client, email="owner@example.com")
    system_template = create_system_template(
        client,
        token=token,
        name="Sistema Autoral",
    )

    update_response = client.patch(
        f"/api/v1/system-templates/{system_template['id']}",
        json={"name": "Sistema Revisado", "type": "custom-rules"},
        headers=auth_headers(token),
    )
    archive_response = client.post(
        f"/api/v1/system-templates/{system_template['id']}/archive",
        headers=auth_headers(token),
    )
    default_list_response = client.get(
        "/api/v1/system-templates",
        headers=auth_headers(token),
    )
    archived_list_response = client.get(
        "/api/v1/system-templates",
        params={"include_archived": True},
        headers=auth_headers(token),
    )

    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Sistema Revisado"
    assert update_response.json()["type"] == "custom-rules"
    assert archive_response.status_code == 200
    assert archive_response.json()["archived_at"] is not None
    assert default_list_response.json() == []
    assert [template["id"] for template in archived_list_response.json()] == [
        system_template["id"]
    ]


def test_project_modules_are_user_scoped_and_updateable(client: TestClient) -> None:
    owner_token = register_and_login_user(client, email="owner@example.com")
    other_token = register_and_login_user(client, email="other@example.com")
    owner_project = create_game_project(client, token=owner_token, name="Mesa do Dono")
    other_project = create_game_project(client, token=other_token, name="Mesa Privada")

    modules_response = client.get(
        f"/api/v1/game-projects/{owner_project['id']}/modules",
        headers=auth_headers(owner_token),
    )
    other_modules_response = client.get(
        f"/api/v1/game-projects/{other_project['id']}/modules",
        headers=auth_headers(owner_token),
    )
    first_module = modules_response.json()[0]
    update_response = client.patch(
        f"/api/v1/game-projects/{owner_project['id']}/modules/{first_module['id']}",
        json={
            "display_name": "Painel",
            "is_enabled": False,
            "order_index": 5,
            "icon_key": "panel-top",
        },
        headers=auth_headers(owner_token),
    )
    other_update_response = client.patch(
        f"/api/v1/game-projects/{other_project['id']}/modules/{first_module['id']}",
        json={"is_enabled": False},
        headers=auth_headers(owner_token),
    )

    assert modules_response.status_code == 200
    assert len(modules_response.json()) == 10
    assert other_modules_response.status_code == 404
    assert update_response.status_code == 200
    assert update_response.json()["display_name"] == "Painel"
    assert update_response.json()["is_enabled"] is False
    assert update_response.json()["order_index"] == 5
    assert update_response.json()["icon_key"] == "panel-top"
    assert other_update_response.status_code == 404


def test_game_project_summary_is_user_scoped_and_returns_zero_counters(
    client: TestClient,
) -> None:
    owner_token = register_and_login_user(client, email="owner@example.com")
    other_token = register_and_login_user(client, email="other@example.com")
    world = create_world(client, token=owner_token, name="Aelthos")
    system_template = create_system_template(
        client,
        token=owner_token,
        name="Sistema Aelthos",
    )
    project = create_game_project(
        client,
        token=owner_token,
        name="A Dama de Ferro",
        extra={
            "world_id": world["id"],
            "system_template_id": system_template["id"],
        },
    )

    summary_response = client.get(
        f"/api/v1/game-projects/{project['id']}/summary",
        headers=auth_headers(owner_token),
    )
    other_summary_response = client.get(
        f"/api/v1/game-projects/{project['id']}/summary",
        headers=auth_headers(other_token),
    )

    assert summary_response.status_code == 200
    summary = summary_response.json()
    assert summary["id"] == project["id"]
    assert summary["world"] == {"id": world["id"], "name": world["name"]}
    assert summary["system_template"] == {
        "id": system_template["id"],
        "name": system_template["name"],
    }
    assert len(summary["active_modules"]) == 10
    assert summary["counters"] == {
        "sessions_count": 0,
        "scenes_count": 0,
        "characters_creatures_count": 0,
        "locations_count": 0,
        "organizations_factions_count": 0,
        "documents_count": 0,
        "notes_count": 0,
        "relationships_count": 0,
    }
    assert other_summary_response.status_code == 404


def test_game_project_rejects_world_and_template_from_other_user(
    client: TestClient,
) -> None:
    owner_token = register_and_login_user(client, email="owner@example.com")
    other_token = register_and_login_user(client, email="other@example.com")
    project = create_game_project(client, token=owner_token, name="Projeto do Dono")
    owner_world = create_world(client, token=owner_token, name="Mundo do Dono")
    other_world = create_world(client, token=other_token, name="Mundo Privado")
    owner_template = create_system_template(
        client,
        token=owner_token,
        name="Sistema do Dono",
    )
    other_template = create_system_template(
        client,
        token=other_token,
        name="Sistema Privado",
    )

    own_world_response = client.patch(
        f"/api/v1/game-projects/{project['id']}",
        json={"world_id": owner_world["id"]},
        headers=auth_headers(owner_token),
    )
    other_world_response = client.patch(
        f"/api/v1/game-projects/{project['id']}",
        json={"world_id": other_world["id"]},
        headers=auth_headers(owner_token),
    )
    own_template_response = client.patch(
        f"/api/v1/game-projects/{project['id']}",
        json={"system_template_id": owner_template["id"]},
        headers=auth_headers(owner_token),
    )
    other_template_response = client.patch(
        f"/api/v1/game-projects/{project['id']}",
        json={"system_template_id": other_template["id"]},
        headers=auth_headers(owner_token),
    )

    assert own_world_response.status_code == 200
    assert own_world_response.json()["world_id"] == owner_world["id"]
    assert other_world_response.status_code == 404
    assert own_template_response.status_code == 200
    assert own_template_response.json()["system_template_id"] == owner_template["id"]
    assert other_template_response.status_code == 404


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
    extra: dict[str, Any] | None = None,
) -> dict:
    payload: dict[str, Any] = {"name": name, "format": "Campanha"}
    if extra:
        payload.update(extra)

    response = client.post(
        "/api/v1/game-projects",
        json=payload,
        headers=auth_headers(token),
    )
    assert response.status_code == 201
    return dict(response.json())


def create_world(client: TestClient, *, token: str, name: str) -> dict:
    response = client.post(
        "/api/v1/worlds",
        json={"name": name},
        headers=auth_headers(token),
    )
    assert response.status_code == 201
    return dict(response.json())


def create_system_template(client: TestClient, *, token: str, name: str) -> dict:
    response = client.post(
        "/api/v1/system-templates",
        json={"name": name},
        headers=auth_headers(token),
    )
    assert response.status_code == 201
    return dict(response.json())


def create_builtin_system_template(db_session: Session) -> SystemTemplate:
    system_template = SystemTemplate(
        owner_user_id=None,
        name="D&D 5e",
        slug="dnd-5e",
        type="builtin",
        description="Template built-in de teste.",
        is_builtin=True,
        metadata_json={},
    )
    db_session.add(system_template)
    db_session.commit()
    db_session.refresh(system_template)
    return system_template


def auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}
