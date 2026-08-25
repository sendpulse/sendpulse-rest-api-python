from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TagPinUnpinPhoneRequest:
    phone: str | None = None
    tags: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TagPinUnpinPhoneRequest:
        return cls(
            phone=data.get("phone"),
            tags=data.get("tags"),
        )
