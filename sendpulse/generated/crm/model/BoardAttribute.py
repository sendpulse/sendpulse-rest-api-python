from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class BoardAttribute:
    id: int | None = None
    name: str | None = None
    type: int | None = None
    mandatory: bool | None = None
    options: list[Any] | None = None
    status: int | None = None
    order: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BoardAttribute:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            type=data.get("type"),
            mandatory=data.get("mandatory"),
            options=data.get("options"),
            status=data.get("status"),
            order=data.get("order"),
        )
