from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ContactTag:
    id: int | None = None
    name: str | None = None
    colorText: str | None = None
    colorBackground: str | None = None
    contactCount: int | None = None
    taskCount: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContactTag:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            colorText=data.get("colorText"),
            colorBackground=data.get("colorBackground"),
            contactCount=data.get("contactCount"),
            taskCount=data.get("taskCount"),
        )
