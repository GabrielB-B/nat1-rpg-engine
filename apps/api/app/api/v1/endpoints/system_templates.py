from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.system_template import SystemTemplate
from app.models.user import User
from app.schemas.system_template import (
    SystemTemplateCreate,
    SystemTemplateRead,
    SystemTemplateUpdate,
)
from app.services.system_template_service import (
    BuiltInSystemTemplateProtectedError,
    SystemTemplateConflictError,
    SystemTemplateNotFoundError,
    SystemTemplateService,
)

router = APIRouter(prefix="/system-templates", tags=["system-templates"])


@router.post(
    "",
    response_model=SystemTemplateRead,
    status_code=status.HTTP_201_CREATED,
)
def create_system_template(
    template_create: SystemTemplateCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> SystemTemplate:
    try:
        return SystemTemplateService(db).create_system_template(
            current_user=current_user,
            template_create=template_create,
        )
    except SystemTemplateConflictError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="System template slug already exists",
        ) from None


@router.get("", response_model=list[SystemTemplateRead])
def list_system_templates(
    include_archived: bool = Query(default=False),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[SystemTemplate]:
    return SystemTemplateService(db).list_system_templates(
        current_user=current_user,
        include_archived=include_archived,
    )


@router.get("/{template_id}", response_model=SystemTemplateRead)
def get_system_template(
    template_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> SystemTemplate:
    try:
        return SystemTemplateService(db).get_system_template(
            current_user=current_user,
            template_id=template_id,
        )
    except SystemTemplateNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="System template not found",
        ) from None


@router.patch("/{template_id}", response_model=SystemTemplateRead)
def update_system_template(
    template_id: UUID,
    template_update: SystemTemplateUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> SystemTemplate:
    try:
        return SystemTemplateService(db).update_system_template(
            current_user=current_user,
            template_id=template_id,
            template_update=template_update,
        )
    except SystemTemplateNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="System template not found",
        ) from None
    except BuiltInSystemTemplateProtectedError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Built-in system templates cannot be changed",
        ) from None
    except SystemTemplateConflictError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="System template slug already exists",
        ) from None


@router.post("/{template_id}/archive", response_model=SystemTemplateRead)
def archive_system_template(
    template_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> SystemTemplate:
    try:
        return SystemTemplateService(db).archive_system_template(
            current_user=current_user,
            template_id=template_id,
        )
    except SystemTemplateNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="System template not found",
        ) from None
    except BuiltInSystemTemplateProtectedError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Built-in system templates cannot be changed",
        ) from None
