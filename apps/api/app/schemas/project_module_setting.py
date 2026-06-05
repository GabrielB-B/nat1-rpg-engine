from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class ProjectModuleSettingRead(BaseModel):
    id: UUID
    module_key: str
    display_name: str
    is_enabled: bool
    order_index: int
    icon_key: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProjectModuleSettingUpdate(BaseModel):
    display_name: str | None = Field(default=None, min_length=1, max_length=120)
    is_enabled: bool | None = None
    order_index: int | None = Field(default=None, ge=0)
    icon_key: str | None = Field(default=None, max_length=80)

    @field_validator("display_name")
    @classmethod
    def validate_display_name(cls, value: str | None) -> str | None:
        if value is None:
            return value

        stripped_value = value.strip()
        if not stripped_value:
            raise ValueError("Value is required")
        return stripped_value

    @model_validator(mode="after")
    def validate_nullable_fields(self) -> "ProjectModuleSettingUpdate":
        for field_name in {"display_name", "is_enabled", "order_index"}:
            if field_name in self.model_fields_set and getattr(self, field_name) is None:
                raise ValueError(f"{field_name} cannot be null")

        return self
