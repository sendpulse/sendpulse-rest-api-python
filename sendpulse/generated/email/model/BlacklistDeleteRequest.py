from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class BlacklistDeleteRequest:
    emails: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BlacklistDeleteRequest:
        return cls(
            emails=data.get("emails"),
        )
