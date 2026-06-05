from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class WorldCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    description: str | None = None
    status: str = Field(default="active", min_length=1, max_length=50)
    metadata_json: dict[str, Any] = Field(default_factory=dict)

    @field_validator("name", "status")
    @classmethod
    def validate_required_text(cls, value: str) -> str:
        stripped_value = value.strip()
        if not stripped_value:
            raise ValueError("Value is required")
        return stripped_value


class WorldUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = None
    status: str | None = Field(default=None, min_length=1, max_length=50)
    metadata_json: dict[str, Any] | None = None

    @field_validator("name", "status")
    @classmethod
    def validate_optional_required_text(cls, value: str | None) -> str | None:
        if value is None:
            return value

        stripped_value = value.strip()
        if not stripped_value:
            raise ValueError("Value is required")
        return stripped_value

    @model_validator(mode="after")
    def validate_nullable_fields(self) -> "WorldUpdate":
        for field_name in {"name", "status", "metadata_json"} & self.model_fields_set:
            if getattr(self, field_name) is None:
                raise ValueError(f"{field_name} cannot be null")

        return self


class WorldRead(BaseModel):
    id: UUID
    owner_user_id: UUID
    name: str
    slug: str
    description: str | None
    status: str
    metadata_json: dict[str, Any]
    created_at: datetime
    updated_at: datetime
    archived_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
