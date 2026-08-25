from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class BlacklistAddRequest:
    emails: str | None = None
    comment: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BlacklistAddRequest:
        return cls(
            emails=data.get("emails"),
            comment=data.get("comment"),
        )
