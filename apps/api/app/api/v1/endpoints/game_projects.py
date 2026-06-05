from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.game_project import GameProject
from app.models.project_module_setting import ProjectModuleSetting
from app.models.user import User
from app.schemas.game_project import (
    GameProjectCreate,
    GameProjectListItem,
    GameProjectRead,
    GameProjectSummary,
    GameProjectUpdate,
)
from app.schemas.project_module_setting import (
    ProjectModuleSettingRead,
    ProjectModuleSettingUpdate,
)
from app.services.game_project_service import (
    GameProjectConflictError,
    GameProjectNotFoundError,
    GameProjectService,
    RelatedGameProjectResourceNotFoundError,
)
from app.services.project_module_setting_service import (
    ProjectModuleSettingConflictError,
    ProjectModuleSettingNotFoundError,
    ProjectModuleSettingService,
)

router = APIRouter(prefix="/game-projects", tags=["game-projects"])


@router.post(
    "",
    response_model=GameProjectRead,
    status_code=status.HTTP_201_CREATED,
)
def create_game_project(
    project_create: GameProjectCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> GameProject:
    try:
        return GameProjectService(db).create_project(
            current_user=current_user,
            project_create=project_create,
        )
    except RelatedGameProjectResourceNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Related world or system template not found",
        ) from None
    except GameProjectConflictError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Game project slug already exists",
        ) from None


@router.get("", response_model=list[GameProjectListItem])
def list_game_projects(
    include_archived: bool = Query(default=False),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[GameProject]:
    return GameProjectService(db).list_projects(
        current_user=current_user,
        include_archived=include_archived,
    )


@router.get("/{project_id}", response_model=GameProjectRead)
def get_game_project(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> GameProject:
    try:
        return GameProjectService(db).get_project(
            current_user=current_user,
            project_id=project_id,
        )
    except GameProjectNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game project not found",
        ) from None


@router.get("/{project_id}/modules", response_model=list[ProjectModuleSettingRead])
def list_game_project_modules(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[ProjectModuleSetting]:
    try:
        return ProjectModuleSettingService(db).list_project_modules(
            current_user=current_user,
            project_id=project_id,
        )
    except ProjectModuleSettingNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game project not found",
        ) from None


@router.patch(
    "/{project_id}/modules/{module_setting_id}",
    response_model=ProjectModuleSettingRead,
)
def update_game_project_module(
    project_id: UUID,
    module_setting_id: UUID,
    module_update: ProjectModuleSettingUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ProjectModuleSetting:
    try:
        return ProjectModuleSettingService(db).update_project_module(
            current_user=current_user,
            project_id=project_id,
            module_setting_id=module_setting_id,
            module_update=module_update,
        )
    except ProjectModuleSettingNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project module setting not found",
        ) from None
    except ProjectModuleSettingConflictError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Project module setting conflict",
        ) from None


@router.get("/{project_id}/summary", response_model=GameProjectSummary)
def get_game_project_summary(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> GameProjectSummary:
    try:
        return GameProjectService(db).get_project_summary(
            current_user=current_user,
            project_id=project_id,
        )
    except GameProjectNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game project not found",
        ) from None


@router.patch("/{project_id}", response_model=GameProjectRead)
def update_game_project(
    project_id: UUID,
    project_update: GameProjectUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> GameProject:
    try:
        return GameProjectService(db).update_project(
            current_user=current_user,
            project_id=project_id,
            project_update=project_update,
        )
    except GameProjectNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game project not found",
        ) from None
    except RelatedGameProjectResourceNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Related world or system template not found",
        ) from None
    except GameProjectConflictError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Game project slug already exists",
        ) from None


@router.post("/{project_id}/archive", response_model=GameProjectRead)
def archive_game_project(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> GameProject:
    try:
        return GameProjectService(db).archive_project(
            current_user=current_user,
            project_id=project_id,
        )
    except GameProjectNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game project not found",
        ) from None


@router.post("/{project_id}/restore", response_model=GameProjectRead)
def restore_game_project(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> GameProject:
    try:
        return GameProjectService(db).restore_project(
            current_user=current_user,
            project_id=project_id,
        )
    except GameProjectNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game project not found",
        ) from None
