from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import (
    ArchiveMixin,
    MetadataJsonMixin,
    TimestampMixin,
    UUIDPrimaryKeyMixin,
)

if TYPE_CHECKING:
    from app.models.game_project import GameProject
    from app.models.user import User


class SystemTemplate(
    UUIDPrimaryKeyMixin,
    MetadataJsonMixin,
    TimestampMixin,
    ArchiveMixin,
    Base,
):
    __tablename__ = "system_templates"

    owner_user_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(160), nullable=False, index=True)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_builtin: Mapped[bool] = mapped_column(
        nullable=False,
        default=False,
        server_default=text("false"),
    )

    owner: Mapped[User | None] = relationship(back_populates="system_templates")
    game_projects: Mapped[list[GameProject]] = relationship(
        back_populates="system_template"
    )
