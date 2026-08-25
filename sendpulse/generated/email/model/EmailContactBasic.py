from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class EmailContactBasic:
    email: str | None = None
    status: int | None = None
    status_explain: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EmailContactBasic:
        return cls(
            email=data.get("email"),
            status=data.get("status"),
            status_explain=data.get("status_explain"),
        )
