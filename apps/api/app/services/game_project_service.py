import re
import unicodedata
from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.game_project import GameProject
from app.models.mixins import utc_now
from app.models.user import User
from app.repositories.game_project_repository import GameProjectRepository
from app.schemas.game_project import GameProjectCreate, GameProjectUpdate

DEFAULT_PROJECT_STATUS = "preparation"
ARCHIVED_PROJECT_STATUS = "archived"
DEFAULT_PROJECT_THEME = "cartographer"

DEFAULT_MODULE_SETTINGS = [
    {
        "module_key": "overview",
        "display_name": "Resumo",
        "is_enabled": True,
        "order_index": 10,
        "icon_key": "layout-dashboard",
    },
    {
        "module_key": "sessions",
        "display_name": "Sessoes",
        "is_enabled": True,
        "order_index": 20,
        "icon_key": "calendar-days",
    },
    {
        "module_key": "scenes",
        "display_name": "Cenas",
        "is_enabled": True,
        "order_index": 30,
        "icon_key": "clapperboard",
    },
    {
        "module_key": "characters_creatures",
        "display_name": "Personagens & Criaturas",
        "is_enabled": True,
        "order_index": 40,
        "icon_key": "users",
    },
    {
        "module_key": "locations_atlas",
        "display_name": "Locais / Atlas",
        "is_enabled": True,
        "order_index": 50,
        "icon_key": "map",
    },
    {
        "module_key": "organizations_factions",
        "display_name": "Organizacoes / Faccoes",
        "is_enabled": True,
        "order_index": 60,
        "icon_key": "flag",
    },
    {
        "module_key": "documents",
        "display_name": "Documentos",
        "is_enabled": True,
        "order_index": 70,
        "icon_key": "file-text",
    },
    {
        "module_key": "notes",
        "display_name": "Notas",
        "is_enabled": True,
        "order_index": 80,
        "icon_key": "notebook-pen",
    },
    {
        "module_key": "relationships",
        "display_name": "Relacoes",
        "is_enabled": True,
        "order_index": 90,
        "icon_key": "network",
    },
    {
        "module_key": "settings",
        "display_name": "Configuracoes",
        "is_enabled": True,
        "order_index": 100,
        "icon_key": "settings",
    },
]


class GameProjectNotFoundError(Exception):
    pass


class RelatedGameProjectResourceNotFoundError(Exception):
    pass


class GameProjectConflictError(Exception):
    pass


class GameProjectService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.projects = GameProjectRepository(db)

    def create_project(
        self,
        *,
        current_user: User,
        project_create: GameProjectCreate,
    ) -> GameProject:
        self._validate_related_resources(
            owner_user_id=current_user.id,
            system_template_id=project_create.system_template_id,
            world_id=project_create.world_id,
        )

        slug = self._generate_unique_slug(
            owner_user_id=current_user.id,
            name=project_create.name,
        )

        try:
            project = self.projects.create(
                owner_user_id=current_user.id,
                name=project_create.name,
                slug=slug,
                format=project_create.format,
                description=project_create.description,
                status=project_create.status or DEFAULT_PROJECT_STATUS,
                system_template_id=project_create.system_template_id,
                world_id=project_create.world_id,
                theme=project_create.theme or DEFAULT_PROJECT_THEME,
                cover_image_url=project_create.cover_image_url,
                metadata_json=project_create.metadata_json,
            )
            self.projects.add_module_settings(
                game_project_id=project.id,
                module_settings=DEFAULT_MODULE_SETTINGS,
            )
            self.db.commit()
        except IntegrityError as exc:
            self.db.rollback()
            raise GameProjectConflictError from exc

        return self._get_project_after_write(
            owner_user_id=current_user.id,
            project_id=project.id,
        )

    def list_projects(
        self,
        *,
        current_user: User,
        include_archived: bool = False,
    ) -> list[GameProject]:
        return self.projects.list_for_owner(
            owner_user_id=current_user.id,
            include_archived=include_archived,
        )

    def get_project(
        self,
        *,
        current_user: User,
        project_id: UUID,
    ) -> GameProject:
        project = self.projects.get_by_id_for_owner(
            owner_user_id=current_user.id,
            project_id=project_id,
        )
        if project is None:
            raise GameProjectNotFoundError

        return self._sort_module_settings(project)

    def update_project(
        self,
        *,
        current_user: User,
        project_id: UUID,
        project_update: GameProjectUpdate,
    ) -> GameProject:
        project = self.projects.get_by_id_for_owner(
            owner_user_id=current_user.id,
            project_id=project_id,
        )
        if project is None:
            raise GameProjectNotFoundError

        updates = project_update.model_dump(exclude_unset=True)
        self._validate_related_resources(
            owner_user_id=current_user.id,
            system_template_id=updates.get("system_template_id"),
            world_id=updates.get("world_id"),
        )

        for field_name, value in updates.items():
            setattr(project, field_name, value)

        return self._commit_and_reload(
            owner_user_id=current_user.id,
            project_id=project.id,
        )

    def archive_project(
        self,
        *,
        current_user: User,
        project_id: UUID,
    ) -> GameProject:
        project = self.projects.get_by_id_for_owner(
            owner_user_id=current_user.id,
            project_id=project_id,
        )
        if project is None:
            raise GameProjectNotFoundError

        if project.archived_at is None:
            project.archived_at = utc_now()
            project.status = ARCHIVED_PROJECT_STATUS

        return self._commit_and_reload(
            owner_user_id=current_user.id,
            project_id=project.id,
        )

    def restore_project(
        self,
        *,
        current_user: User,
        project_id: UUID,
    ) -> GameProject:
        project = self.projects.get_by_id_for_owner(
            owner_user_id=current_user.id,
            project_id=project_id,
        )
        if project is None:
            raise GameProjectNotFoundError

        project.archived_at = None
        if project.status == ARCHIVED_PROJECT_STATUS:
            project.status = DEFAULT_PROJECT_STATUS

        return self._commit_and_reload(
            owner_user_id=current_user.id,
            project_id=project.id,
        )

    def _generate_unique_slug(self, *, owner_user_id: UUID, name: str) -> str:
        base_slug = self._slugify(name)
        slug = base_slug
        suffix = 2

        while (
            self.projects.get_by_owner_and_slug(
                owner_user_id=owner_user_id,
                slug=slug,
            )
            is not None
        ):
            slug = f"{base_slug}-{suffix}"
            suffix += 1

        return slug

    def _slugify(self, value: str) -> str:
        normalized = unicodedata.normalize("NFKD", value)
        ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value.lower()).strip("-")
        return slug or "game-project"

    def _validate_related_resources(
        self,
        *,
        owner_user_id: UUID,
        system_template_id: UUID | None,
        world_id: UUID | None,
    ) -> None:
        if world_id is not None:
            world = self.projects.get_world_for_owner(
                owner_user_id=owner_user_id,
                world_id=world_id,
            )
            if world is None:
                raise RelatedGameProjectResourceNotFoundError

        if system_template_id is not None:
            system_template = self.projects.get_system_template_for_owner(
                owner_user_id=owner_user_id,
                system_template_id=system_template_id,
            )
            if system_template is None:
                raise RelatedGameProjectResourceNotFoundError

    def _commit_and_reload(
        self,
        *,
        owner_user_id: UUID,
        project_id: UUID,
    ) -> GameProject:
        try:
            self.db.commit()
        except IntegrityError as exc:
            self.db.rollback()
            raise GameProjectConflictError from exc

        return self._get_project_after_write(
            owner_user_id=owner_user_id,
            project_id=project_id,
        )

    def _get_project_after_write(
        self,
        *,
        owner_user_id: UUID,
        project_id: UUID,
    ) -> GameProject:
        project = self.projects.get_by_id_for_owner(
            owner_user_id=owner_user_id,
            project_id=project_id,
        )
        if project is None:
            raise GameProjectNotFoundError

        return self._sort_module_settings(project)

    def _sort_module_settings(self, project: GameProject) -> GameProject:
        project.module_settings.sort(key=lambda setting: setting.order_index)
        return project
