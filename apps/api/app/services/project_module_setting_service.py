from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.project_module_setting import ProjectModuleSetting
from app.models.user import User
from app.repositories.project_module_setting_repository import (
    ProjectModuleSettingRepository,
)
from app.schemas.project_module_setting import ProjectModuleSettingUpdate


class ProjectModuleSettingNotFoundError(Exception):
    pass


class ProjectModuleSettingConflictError(Exception):
    pass


class ProjectModuleSettingService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.project_modules = ProjectModuleSettingRepository(db)

    def list_project_modules(
        self,
        *,
        current_user: User,
        project_id: UUID,
    ) -> list[ProjectModuleSetting]:
        modules = self.project_modules.list_for_owner_project(
            owner_user_id=current_user.id,
            project_id=project_id,
        )
        if modules is None:
            raise ProjectModuleSettingNotFoundError

        return modules

    def update_project_module(
        self,
        *,
        current_user: User,
        project_id: UUID,
        module_setting_id: UUID,
        module_update: ProjectModuleSettingUpdate,
    ) -> ProjectModuleSetting:
        module_setting = self.project_modules.get_for_owner_project(
            owner_user_id=current_user.id,
            project_id=project_id,
            module_setting_id=module_setting_id,
        )
        if module_setting is None:
            raise ProjectModuleSettingNotFoundError

        for field_name, value in module_update.model_dump(exclude_unset=True).items():
            setattr(module_setting, field_name, value)

        try:
            self.db.commit()
        except IntegrityError as exc:
            self.db.rollback()
            raise ProjectModuleSettingConflictError from exc

        self.db.refresh(module_setting)
        return module_setting
