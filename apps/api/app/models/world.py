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
    from app.models.game_project import GameProject
    from app.models.user import User


class World(
    UUIDPrimaryKeyMixin,
    MetadataJsonMixin,
    TimestampMixin,
    ArchiveMixin,
    Base,
):
    __tablename__ = "worlds"
    __table_args__ = (
        UniqueConstraint("owner_user_id", "slug", name="uq_worlds_owner_user_id_slug"),
    )

    owner_user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(160), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="active",
        server_default=text("'active'"),
    )

    owner: Mapped[User] = relationship(back_populates="worlds")
    game_projects: Mapped[list[GameProject]] = relationship(back_populates="world")
