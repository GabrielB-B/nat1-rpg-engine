from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.world import World


class WorldRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(
        self,
        *,
        owner_user_id: UUID,
        name: str,
        slug: str,
        description: str | None,
        status: str,
        metadata_json: dict,
    ) -> World:
        world = World(
            owner_user_id=owner_user_id,
            name=name,
            slug=slug,
            description=description,
            status=status,
            metadata_json=metadata_json,
        )
        self.db.add(world)
        self.db.flush()
        return world

    def get_by_owner_and_slug(self, *, owner_user_id: UUID, slug: str) -> World | None:
        statement = select(World).where(
            World.owner_user_id == owner_user_id,
            World.slug == slug,
        )
        return self.db.scalar(statement)

    def get_by_id_for_owner(
        self,
        *,
        owner_user_id: UUID,
        world_id: UUID,
        include_archived: bool = True,
    ) -> World | None:
        statement = select(World).where(
            World.id == world_id,
            World.owner_user_id == owner_user_id,
        )
        if not include_archived:
            statement = statement.where(World.archived_at.is_(None))

        return self.db.scalar(statement)

    def list_for_owner(
        self,
        *,
        owner_user_id: UUID,
        include_archived: bool = False,
    ) -> list[World]:
        statement = (
            select(World)
            .where(World.owner_user_id == owner_user_id)
            .order_by(World.updated_at.desc())
        )
        if not include_archived:
            statement = statement.where(World.archived_at.is_(None))

        return list(self.db.scalars(statement).all())
