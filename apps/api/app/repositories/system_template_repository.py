from uuid import UUID

from sqlalchemy import and_, or_, select
from sqlalchemy.orm import Session

from app.models.system_template import SystemTemplate


class SystemTemplateRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(
        self,
        *,
        owner_user_id: UUID,
        name: str,
        slug: str,
        type: str,
        description: str | None,
        metadata_json: dict,
    ) -> SystemTemplate:
        system_template = SystemTemplate(
            owner_user_id=owner_user_id,
            name=name,
            slug=slug,
            type=type,
            description=description,
            is_builtin=False,
            metadata_json=metadata_json,
        )
        self.db.add(system_template)
        self.db.flush()
        return system_template

    def get_user_template_by_slug(
        self,
        *,
        owner_user_id: UUID,
        slug: str,
    ) -> SystemTemplate | None:
        statement = select(SystemTemplate).where(
            SystemTemplate.owner_user_id == owner_user_id,
            SystemTemplate.slug == slug,
        )
        return self.db.scalar(statement)

    def get_available_by_id(
        self,
        *,
        owner_user_id: UUID,
        template_id: UUID,
        include_archived: bool = True,
    ) -> SystemTemplate | None:
        statement = select(SystemTemplate).where(
            SystemTemplate.id == template_id,
            self._available_to_owner_filter(owner_user_id),
        )
        if not include_archived:
            statement = statement.where(SystemTemplate.archived_at.is_(None))

        return self.db.scalar(statement)

    def get_editable_by_id(
        self,
        *,
        owner_user_id: UUID,
        template_id: UUID,
    ) -> SystemTemplate | None:
        statement = select(SystemTemplate).where(
            SystemTemplate.id == template_id,
            SystemTemplate.owner_user_id == owner_user_id,
        )
        return self.db.scalar(statement)

    def list_available(
        self,
        *,
        owner_user_id: UUID,
        include_archived: bool = False,
    ) -> list[SystemTemplate]:
        statement = (
            select(SystemTemplate)
            .where(self._available_to_owner_filter(owner_user_id))
            .order_by(SystemTemplate.is_builtin.desc(), SystemTemplate.updated_at.desc())
        )
        if not include_archived:
            statement = statement.where(SystemTemplate.archived_at.is_(None))

        return list(self.db.scalars(statement).all())

    def _available_to_owner_filter(self, owner_user_id: UUID):
        return or_(
            SystemTemplate.owner_user_id == owner_user_id,
            and_(
                SystemTemplate.owner_user_id.is_(None),
                SystemTemplate.is_builtin.is_(True),
            ),
        )
