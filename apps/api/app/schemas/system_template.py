from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class SystemTemplateCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    type: str = Field(default="custom", min_length=1, max_length=50)
    description: str | None = None
    metadata_json: dict[str, Any] = Field(default_factory=dict)

    @field_validator("name", "type")
    @classmethod
    def validate_required_text(cls, value: str) -> str:
        stripped_value = value.strip()
        if not stripped_value:
            raise ValueError("Value is required")
        return stripped_value


class SystemTemplateUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    type: str | None = Field(default=None, min_length=1, max_length=50)
    description: str | None = None
    metadata_json: dict[str, Any] | None = None

    @field_validator("name", "type")
    @classmethod
    def validate_optional_required_text(cls, value: str | None) -> str | None:
        if value is None:
            return value

        stripped_value = value.strip()
        if not stripped_value:
            raise ValueError("Value is required")
        return stripped_value

    @model_validator(mode="after")
    def validate_nullable_fields(self) -> "SystemTemplateUpdate":
        for field_name in {"name", "type", "metadata_json"} & self.model_fields_set:
            if getattr(self, field_name) is None:
                raise ValueError(f"{field_name} cannot be null")

        return self


class SystemTemplateRead(BaseModel):
    id: UUID
    owner_user_id: UUID | None
    name: str
    slug: str
    type: str
    description: str | None
    is_builtin: bool
    metadata_json: dict[str, Any]
    created_at: datetime
    updated_at: datetime
    archived_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
