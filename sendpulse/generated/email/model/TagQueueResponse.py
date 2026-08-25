from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TagQueueResponse:
    code: str | None = None
    description: str | None = None
    failure: bool | None = None
    http_code: int | None = None
    queue_id: str | None = None
    success: bool | None = None
    user_id: int | None = None
    version: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TagQueueResponse:
        return cls(
            code=data.get("code"),
            description=data.get("description"),
            failure=data.get("failure"),
            http_code=data.get("http_code"),
            queue_id=data.get("queue_id"),
            success=data.get("success"),
            user_id=data.get("user_id"),
            version=data.get("version"),
        )
