from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from app.schemas.project_module_setting import ProjectModuleSettingRead


class GameProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    format: str = Field(min_length=1, max_length=50)
    description: str | None = None
    status: str = Field(default="preparation", min_length=1, max_length=50)
    system_template_id: UUID | None = None
    world_id: UUID | None = None
    theme: str = Field(default="cartographer", min_length=1, max_length=50)
    cover_image_url: str | None = Field(default=None, max_length=2048)
    metadata_json: dict[str, Any] = Field(default_factory=dict)

    @field_validator("name", "format", "status", "theme")
    @classmethod
    def validate_required_text(cls, value: str) -> str:
        stripped_value = value.strip()
        if not stripped_value:
            raise ValueError("Value is required")
        return stripped_value


class GameProjectUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    format: str | None = Field(default=None, min_length=1, max_length=50)
    description: str | None = None
    status: str | None = Field(default=None, min_length=1, max_length=50)
    system_template_id: UUID | None = None
    world_id: UUID | None = None
    theme: str | None = Field(default=None, min_length=1, max_length=50)
    cover_image_url: str | None = Field(default=None, max_length=2048)
    metadata_json: dict[str, Any] | None = None

    @field_validator("name", "format", "status", "theme")
    @classmethod
    def validate_optional_required_text(cls, value: str | None) -> str | None:
        if value is None:
            return value

        stripped_value = value.strip()
        if not stripped_value:
            raise ValueError("Value is required")
        return stripped_value

    @model_validator(mode="after")
    def validate_nullable_fields(self) -> "GameProjectUpdate":
        non_nullable_fields = {
            "name",
            "format",
            "status",
            "theme",
            "metadata_json",
        }
        for field_name in non_nullable_fields & self.model_fields_set:
            if getattr(self, field_name) is None:
                raise ValueError(f"{field_name} cannot be null")

        return self


class GameProjectListItem(BaseModel):
    id: UUID
    owner_user_id: UUID
    name: str
    slug: str
    format: str
    description: str | None
    status: str
    system_template_id: UUID | None
    world_id: UUID | None
    theme: str
    cover_image_url: str | None
    metadata_json: dict[str, Any]
    created_at: datetime
    updated_at: datetime
    archived_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


class GameProjectRead(GameProjectListItem):
    module_settings: list[ProjectModuleSettingRead] = Field(default_factory=list)


class GameProjectSummaryLinkedResource(BaseModel):
    id: UUID
    name: str

    model_config = ConfigDict(from_attributes=True)


class GameProjectSummaryCounts(BaseModel):
    sessions_count: int = 0
    scenes_count: int = 0
    characters_creatures_count: int = 0
    locations_count: int = 0
    organizations_factions_count: int = 0
    documents_count: int = 0
    notes_count: int = 0
    relationships_count: int = 0


class GameProjectSummary(BaseModel):
    id: UUID
    name: str
    slug: str
    format: str
    description: str | None
    status: str
    theme: str
    archived_at: datetime | None
    world: GameProjectSummaryLinkedResource | None
    system_template: GameProjectSummaryLinkedResource | None
    active_modules: list[ProjectModuleSettingRead]
    counters: GameProjectSummaryCounts

    model_config = ConfigDict(from_attributes=True)
