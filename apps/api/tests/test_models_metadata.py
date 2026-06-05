from sqlalchemy import Table, UniqueConstraint
from sqlalchemy.orm import configure_mappers

from app import models
from app.db.base import Base


def test_core_models_are_registered() -> None:
    configure_mappers()

    assert models.__all__ == [
        "GameProject",
        "ProjectModuleSetting",
        "SystemTemplate",
        "User",
        "World",
    ]
    assert set(Base.metadata.tables) >= {
        "users",
        "worlds",
        "system_templates",
        "game_projects",
        "project_module_settings",
    }


def test_core_model_constraints_are_registered() -> None:
    tables = Base.metadata.tables

    users_email_index = tables["users"].indexes
    assert any(index.unique and ["email"] == list(index.columns.keys()) for index in users_email_index)

    assert _has_unique_constraint(
        tables["worlds"],
        "uq_worlds_owner_user_id_slug",
        ["owner_user_id", "slug"],
    )
    assert _has_unique_constraint(
        tables["game_projects"],
        "uq_game_projects_owner_user_id_slug",
        ["owner_user_id", "slug"],
    )
    assert _has_unique_constraint(
        tables["project_module_settings"],
        "uq_project_module_settings_game_project_id_module_key",
        ["game_project_id", "module_key"],
    )


def _has_unique_constraint(table: Table, name: str, columns: list[str]) -> bool:
    return any(
        isinstance(constraint, UniqueConstraint)
        and constraint.name == name
        and list(constraint.columns.keys()) == columns
        for constraint in table.constraints
    )
