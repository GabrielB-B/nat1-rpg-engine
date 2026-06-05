from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.slug import slugify
from app.models.mixins import utc_now
from app.models.system_template import SystemTemplate
from app.models.user import User
from app.repositories.system_template_repository import SystemTemplateRepository
from app.schemas.system_template import SystemTemplateCreate, SystemTemplateUpdate

ARCHIVED_SYSTEM_TEMPLATE_STATUS = "archived"


class SystemTemplateNotFoundError(Exception):
    pass


class SystemTemplateConflictError(Exception):
    pass


class BuiltInSystemTemplateProtectedError(Exception):
    pass


class SystemTemplateService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.system_templates = SystemTemplateRepository(db)

    def create_system_template(
        self,
        *,
        current_user: User,
        template_create: SystemTemplateCreate,
    ) -> SystemTemplate:
        slug = self._generate_unique_slug(
            owner_user_id=current_user.id,
            name=template_create.name,
        )

        try:
            system_template = self.system_templates.create(
                owner_user_id=current_user.id,
                name=template_create.name,
                slug=slug,
                type=template_create.type,
                description=template_create.description,
                metadata_json=template_create.metadata_json,
            )
            self.db.commit()
        except IntegrityError as exc:
            self.db.rollback()
            raise SystemTemplateConflictError from exc

        self.db.refresh(system_template)
        return system_template

    def list_system_templates(
        self,
        *,
        current_user: User,
        include_archived: bool = False,
    ) -> list[SystemTemplate]:
        return self.system_templates.list_available(
            owner_user_id=current_user.id,
            include_archived=include_archived,
        )

    def get_system_template(
        self,
        *,
        current_user: User,
        template_id: UUID,
    ) -> SystemTemplate:
        system_template = self.system_templates.get_available_by_id(
            owner_user_id=current_user.id,
            template_id=template_id,
        )
        if system_template is None:
            raise SystemTemplateNotFoundError

        return system_template

    def update_system_template(
        self,
        *,
        current_user: User,
        template_id: UUID,
        template_update: SystemTemplateUpdate,
    ) -> SystemTemplate:
        system_template = self._get_editable_template(
            owner_user_id=current_user.id,
            template_id=template_id,
        )

        for field_name, value in template_update.model_dump(exclude_unset=True).items():
            setattr(system_template, field_name, value)

        return self._commit_and_reload(
            owner_user_id=current_user.id,
            template_id=system_template.id,
        )

    def archive_system_template(
        self,
        *,
        current_user: User,
        template_id: UUID,
    ) -> SystemTemplate:
        system_template = self._get_editable_template(
            owner_user_id=current_user.id,
            template_id=template_id,
        )

        if system_template.archived_at is None:
            system_template.archived_at = utc_now()

        return self._commit_and_reload(
            owner_user_id=current_user.id,
            template_id=system_template.id,
        )

    def _generate_unique_slug(self, *, owner_user_id: UUID, name: str) -> str:
        base_slug = slugify(name, fallback="system-template")
        slug = base_slug
        suffix = 2

        while (
            self.system_templates.get_user_template_by_slug(
                owner_user_id=owner_user_id,
                slug=slug,
            )
            is not None
        ):
            slug = f"{base_slug}-{suffix}"
            suffix += 1

        return slug

    def _get_editable_template(
        self,
        *,
        owner_user_id: UUID,
        template_id: UUID,
    ) -> SystemTemplate:
        system_template = self.system_templates.get_available_by_id(
            owner_user_id=owner_user_id,
            template_id=template_id,
        )
        if system_template is None:
            raise SystemTemplateNotFoundError
        if system_template.is_builtin or system_template.owner_user_id != owner_user_id:
            raise BuiltInSystemTemplateProtectedError

        return system_template

    def _commit_and_reload(
        self,
        *,
        owner_user_id: UUID,
        template_id: UUID,
    ) -> SystemTemplate:
        try:
            self.db.commit()
        except IntegrityError as exc:
            self.db.rollback()
            raise SystemTemplateConflictError from exc

        system_template = self.system_templates.get_available_by_id(
            owner_user_id=owner_user_id,
            template_id=template_id,
        )
        if system_template is None:
            raise SystemTemplateNotFoundError

        return system_template
