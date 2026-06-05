from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.game_project import GameProject
from app.models.user import User
from app.schemas.game_project import (
    GameProjectCreate,
    GameProjectListItem,
    GameProjectRead,
    GameProjectUpdate,
)
from app.services.game_project_service import (
    GameProjectConflictError,
    GameProjectNotFoundError,
    GameProjectService,
    RelatedGameProjectResourceNotFoundError,
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
