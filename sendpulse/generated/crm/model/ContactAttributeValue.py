from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ContactAttributeValue:
    id: int | None = None
    name: str | None = None
    status: int | None = None
    type: int | None = None
    mandatory: bool | None = None
    contactCardShow: bool | None = None
    order: int | None = None
    options: list[Any] | None = None
    value: Any = None
    default: bool | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContactAttributeValue:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            status=data.get("status"),
            type=data.get("type"),
            mandatory=data.get("mandatory"),
            contactCardShow=data.get("contactCardShow"),
            order=data.get("order"),
            options=data.get("options"),
            value=data.get("value"),
            default=data.get("default"),
        )
