from uuid import UUID

from sqlalchemy import or_, select
from sqlalchemy.orm import Session, selectinload

from app.models.game_project import GameProject
from app.models.project_module_setting import ProjectModuleSetting
from app.models.system_template import SystemTemplate
from app.models.world import World


class GameProjectRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(
        self,
        *,
        owner_user_id: UUID,
        name: str,
        slug: str,
        format: str,
        description: str | None,
        status: str,
        system_template_id: UUID | None,
        world_id: UUID | None,
        theme: str,
        cover_image_url: str | None,
        metadata_json: dict,
    ) -> GameProject:
        project = GameProject(
            owner_user_id=owner_user_id,
            name=name,
            slug=slug,
            format=format,
            description=description,
            status=status,
            system_template_id=system_template_id,
            world_id=world_id,
            theme=theme,
            cover_image_url=cover_image_url,
            metadata_json=metadata_json,
        )
        self.db.add(project)
        self.db.flush()
        return project

    def add_module_settings(
        self,
        *,
        game_project_id: UUID,
        module_settings: list[dict],
    ) -> list[ProjectModuleSetting]:
        settings = [
            ProjectModuleSetting(
                game_project_id=game_project_id,
                module_key=module_setting["module_key"],
                display_name=module_setting["display_name"],
                is_enabled=module_setting["is_enabled"],
                order_index=module_setting["order_index"],
                icon_key=module_setting["icon_key"],
            )
            for module_setting in module_settings
        ]
        self.db.add_all(settings)
        self.db.flush()
        return settings

    def get_by_owner_and_slug(
        self,
        *,
        owner_user_id: UUID,
        slug: str,
    ) -> GameProject | None:
        statement = select(GameProject).where(
            GameProject.owner_user_id == owner_user_id,
            GameProject.slug == slug,
        )
        return self.db.scalar(statement)

    def get_by_id_for_owner(
        self,
        *,
        owner_user_id: UUID,
        project_id: UUID,
        include_archived: bool = True,
    ) -> GameProject | None:
        statement = (
            select(GameProject)
            .options(selectinload(GameProject.module_settings))
            .where(
                GameProject.id == project_id,
                GameProject.owner_user_id == owner_user_id,
            )
        )
        if not include_archived:
            statement = statement.where(GameProject.archived_at.is_(None))

        return self.db.scalar(statement)

    def list_for_owner(
        self,
        *,
        owner_user_id: UUID,
        include_archived: bool = False,
    ) -> list[GameProject]:
        statement = (
            select(GameProject)
            .where(GameProject.owner_user_id == owner_user_id)
            .order_by(GameProject.updated_at.desc())
        )
        if not include_archived:
            statement = statement.where(GameProject.archived_at.is_(None))

        return list(self.db.scalars(statement).all())

    def get_world_for_owner(
        self,
        *,
        owner_user_id: UUID,
        world_id: UUID,
    ) -> World | None:
        statement = select(World).where(
            World.id == world_id,
            World.owner_user_id == owner_user_id,
            World.archived_at.is_(None),
        )
        return self.db.scalar(statement)

    def get_system_template_for_owner(
        self,
        *,
        owner_user_id: UUID,
        system_template_id: UUID,
    ) -> SystemTemplate | None:
        statement = select(SystemTemplate).where(
            SystemTemplate.id == system_template_id,
            SystemTemplate.archived_at.is_(None),
            or_(
                SystemTemplate.owner_user_id == owner_user_id,
                SystemTemplate.owner_user_id.is_(None),
                SystemTemplate.is_builtin.is_(True),
            ),
        )
        return self.db.scalar(statement)
