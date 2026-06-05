from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import (
    ArchiveMixin,
    MetadataJsonMixin,
    TimestampMixin,
    UUIDPrimaryKeyMixin,
)

if TYPE_CHECKING:
    from app.models.project_module_setting import ProjectModuleSetting
    from app.models.system_template import SystemTemplate
    from app.models.user import User
    from app.models.world import World


class GameProject(
    UUIDPrimaryKeyMixin,
    MetadataJsonMixin,
    TimestampMixin,
    ArchiveMixin,
    Base,
):
    __tablename__ = "game_projects"
    __table_args__ = (
        UniqueConstraint(
            "owner_user_id",
            "slug",
            name="uq_game_projects_owner_user_id_slug",
        ),
    )

    owner_user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(160), nullable=False)
    format: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="active",
        server_default=text("'active'"),
    )
    system_template_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("system_templates.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    world_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("worlds.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    theme: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="cartographer",
        server_default=text("'cartographer'"),
    )
    cover_image_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)

    owner: Mapped[User] = relationship(back_populates="game_projects")
    system_template: Mapped[SystemTemplate | None] = relationship(
        back_populates="game_projects"
    )
    world: Mapped[World | None] = relationship(back_populates="game_projects")
    module_settings: Mapped[list[ProjectModuleSetting]] = relationship(
        back_populates="game_project",
        cascade="all, delete-orphan",
    )
