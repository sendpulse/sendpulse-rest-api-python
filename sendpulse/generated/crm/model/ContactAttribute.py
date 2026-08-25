from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ContactAttribute:
    id: int | None = None
    name: str | None = None
    status: int | None = None
    order: int | None = None
    options: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContactAttribute:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            status=data.get("status"),
            order=data.get("order"),
            options=data.get("options"),
        )
