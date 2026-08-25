from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ContactEmail:
    id: int | None = None
    email: str | None = None
    isMain: bool | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContactEmail:
        return cls(
            id=data.get("id"),
            email=data.get("email"),
            isMain=data.get("isMain"),
        )
