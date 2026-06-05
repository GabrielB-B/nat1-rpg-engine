from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.slug import slugify
from app.models.mixins import utc_now
from app.models.user import User
from app.models.world import World
from app.repositories.world_repository import WorldRepository
from app.schemas.world import WorldCreate, WorldUpdate

DEFAULT_WORLD_STATUS = "active"
ARCHIVED_WORLD_STATUS = "archived"


class WorldNotFoundError(Exception):
    pass


class WorldConflictError(Exception):
    pass


class WorldService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.worlds = WorldRepository(db)

    def create_world(self, *, current_user: User, world_create: WorldCreate) -> World:
        slug = self._generate_unique_slug(
            owner_user_id=current_user.id,
            name=world_create.name,
        )

        try:
            world = self.worlds.create(
                owner_user_id=current_user.id,
                name=world_create.name,
                slug=slug,
                description=world_create.description,
                status=world_create.status or DEFAULT_WORLD_STATUS,
                metadata_json=world_create.metadata_json,
            )
            self.db.commit()
        except IntegrityError as exc:
            self.db.rollback()
            raise WorldConflictError from exc

        self.db.refresh(world)
        return world

    def list_worlds(
        self,
        *,
        current_user: User,
        include_archived: bool = False,
    ) -> list[World]:
        return self.worlds.list_for_owner(
            owner_user_id=current_user.id,
            include_archived=include_archived,
        )

    def get_world(self, *, current_user: User, world_id: UUID) -> World:
        world = self.worlds.get_by_id_for_owner(
            owner_user_id=current_user.id,
            world_id=world_id,
        )
        if world is None:
            raise WorldNotFoundError

        return world

    def update_world(
        self,
        *,
        current_user: User,
        world_id: UUID,
        world_update: WorldUpdate,
    ) -> World:
        world = self.worlds.get_by_id_for_owner(
            owner_user_id=current_user.id,
            world_id=world_id,
        )
        if world is None:
            raise WorldNotFoundError

        for field_name, value in world_update.model_dump(exclude_unset=True).items():
            setattr(world, field_name, value)

        return self._commit_and_reload(
            owner_user_id=current_user.id,
            world_id=world.id,
        )

    def archive_world(self, *, current_user: User, world_id: UUID) -> World:
        world = self.worlds.get_by_id_for_owner(
            owner_user_id=current_user.id,
            world_id=world_id,
        )
        if world is None:
            raise WorldNotFoundError

        if world.archived_at is None:
            world.archived_at = utc_now()
            world.status = ARCHIVED_WORLD_STATUS

        return self._commit_and_reload(
            owner_user_id=current_user.id,
            world_id=world.id,
        )

    def restore_world(self, *, current_user: User, world_id: UUID) -> World:
        world = self.worlds.get_by_id_for_owner(
            owner_user_id=current_user.id,
            world_id=world_id,
        )
        if world is None:
            raise WorldNotFoundError

        world.archived_at = None
        if world.status == ARCHIVED_WORLD_STATUS:
            world.status = DEFAULT_WORLD_STATUS

        return self._commit_and_reload(
            owner_user_id=current_user.id,
            world_id=world.id,
        )

    def _generate_unique_slug(self, *, owner_user_id: UUID, name: str) -> str:
        base_slug = slugify(name, fallback="world")
        slug = base_slug
        suffix = 2

        while (
            self.worlds.get_by_owner_and_slug(
                owner_user_id=owner_user_id,
                slug=slug,
            )
            is not None
        ):
            slug = f"{base_slug}-{suffix}"
            suffix += 1

        return slug

    def _commit_and_reload(self, *, owner_user_id: UUID, world_id: UUID) -> World:
        try:
            self.db.commit()
        except IntegrityError as exc:
            self.db.rollback()
            raise WorldConflictError from exc

        world = self.worlds.get_by_id_for_owner(
            owner_user_id=owner_user_id,
            world_id=world_id,
        )
        if world is None:
            raise WorldNotFoundError

        return world
