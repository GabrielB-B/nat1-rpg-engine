from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.game_project import GameProject
from app.models.project_module_setting import ProjectModuleSetting


class ProjectModuleSettingRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list_for_owner_project(
        self,
        *,
        owner_user_id: UUID,
        project_id: UUID,
    ) -> list[ProjectModuleSetting] | None:
        project_exists = self.db.scalar(
            select(GameProject.id).where(
                GameProject.id == project_id,
                GameProject.owner_user_id == owner_user_id,
            )
        )
        if project_exists is None:
            return None

        statement = (
            select(ProjectModuleSetting)
            .where(ProjectModuleSetting.game_project_id == project_id)
            .order_by(ProjectModuleSetting.order_index.asc())
        )
        return list(self.db.scalars(statement).all())

    def get_for_owner_project(
        self,
        *,
        owner_user_id: UUID,
        project_id: UUID,
        module_setting_id: UUID,
    ) -> ProjectModuleSetting | None:
        statement = (
            select(ProjectModuleSetting)
            .join(GameProject)
            .where(
                ProjectModuleSetting.id == module_setting_id,
                ProjectModuleSetting.game_project_id == project_id,
                GameProject.owner_user_id == owner_user_id,
            )
        )
        return self.db.scalar(statement)
