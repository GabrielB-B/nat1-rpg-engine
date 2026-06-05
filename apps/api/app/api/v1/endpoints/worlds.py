from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.models.world import World
from app.schemas.world import WorldCreate, WorldRead, WorldUpdate
from app.services.world_service import (
    WorldConflictError,
    WorldNotFoundError,
    WorldService,
)

router = APIRouter(prefix="/worlds", tags=["worlds"])


@router.post("", response_model=WorldRead, status_code=status.HTTP_201_CREATED)
def create_world(
    world_create: WorldCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> World:
    try:
        return WorldService(db).create_world(
            current_user=current_user,
            world_create=world_create,
        )
    except WorldConflictError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="World slug already exists",
        ) from None


@router.get("", response_model=list[WorldRead])
def list_worlds(
    include_archived: bool = Query(default=False),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[World]:
    return WorldService(db).list_worlds(
        current_user=current_user,
        include_archived=include_archived,
    )


@router.get("/{world_id}", response_model=WorldRead)
def get_world(
    world_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> World:
    try:
        return WorldService(db).get_world(
            current_user=current_user,
            world_id=world_id,
        )
    except WorldNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="World not found",
        ) from None


@router.patch("/{world_id}", response_model=WorldRead)
def update_world(
    world_id: UUID,
    world_update: WorldUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> World:
    try:
        return WorldService(db).update_world(
            current_user=current_user,
            world_id=world_id,
            world_update=world_update,
        )
    except WorldNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="World not found",
        ) from None
    except WorldConflictError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="World slug already exists",
        ) from None


@router.post("/{world_id}/archive", response_model=WorldRead)
def archive_world(
    world_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> World:
    try:
        return WorldService(db).archive_world(
            current_user=current_user,
            world_id=world_id,
        )
    except WorldNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="World not found",
        ) from None


@router.post("/{world_id}/restore", response_model=WorldRead)
def restore_world(
    world_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> World:
    try:
        return WorldService(db).restore_world(
            current_user=current_user,
            world_id=world_id,
        )
    except WorldNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="World not found",
        ) from None
