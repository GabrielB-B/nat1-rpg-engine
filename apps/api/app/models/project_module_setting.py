from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.game_project import GameProject


class ProjectModuleSetting(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "project_module_settings"
    __table_args__ = (
        UniqueConstraint(
            "game_project_id",
            "module_key",
            name="uq_project_module_settings_game_project_id_module_key",
        ),
    )

    game_project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("game_projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    module_key: Mapped[str] = mapped_column(String(100), nullable=False)
    display_name: Mapped[str] = mapped_column(String(120), nullable=False)
    is_enabled: Mapped[bool] = mapped_column(
        nullable=False,
        default=True,
        server_default=text("true"),
    )
    order_index: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
        server_default=text("0"),
    )
    icon_key: Mapped[str | None] = mapped_column(String(80), nullable=True)

    game_project: Mapped[GameProject] = relationship(back_populates="module_settings")
