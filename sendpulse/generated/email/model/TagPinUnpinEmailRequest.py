from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TagPinUnpinEmailRequest:
    email: str | None = None
    tags: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TagPinUnpinEmailRequest:
        return cls(
            email=data.get("email"),
            tags=data.get("tags"),
        )
