from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class SentEmail:
    result: bool | None = None
    id: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SentEmail:
        return cls(
            result=data.get("result"),
            id=data.get("id"),
        )
