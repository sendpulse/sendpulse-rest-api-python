from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ContactPhone:
    id: int | None = None
    phone: str | None = None
    isMain: bool | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContactPhone:
        return cls(
            id=data.get("id"),
            phone=data.get("phone"),
            isMain=data.get("isMain"),
        )
