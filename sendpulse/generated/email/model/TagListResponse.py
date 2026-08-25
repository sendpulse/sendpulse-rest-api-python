from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sendpulse.generated.email.model.Tag import Tag


@dataclass(slots=True)
class TagListResponse:
    tags: list[Tag] | None = None
    user_id: int | None = None
    version: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TagListResponse:
        return cls(
            tags=[Tag.from_dict(i) for i in data["tags"]] if isinstance(data.get("tags"), list) else None,
            user_id=data.get("user_id"),
            version=data.get("version"),
        )
