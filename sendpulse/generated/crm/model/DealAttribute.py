from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.crm.model.DefaultStatusProperty import DefaultStatusProperty


@dataclass(slots=True)
class DealAttribute:
    id: int | None = None
    name: str | None = None
    status: DefaultStatusProperty | None = None
    type: int | None = None
    mandatory: bool | None = None
    order: int | None = None
    options: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DealAttribute:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            status=DefaultStatusProperty.from_dict(data["status"]) if isinstance(data.get("status"), dict) else None,
            type=data.get("type"),
            mandatory=data.get("mandatory"),
            order=data.get("order"),
            options=data.get("options"),
        )
