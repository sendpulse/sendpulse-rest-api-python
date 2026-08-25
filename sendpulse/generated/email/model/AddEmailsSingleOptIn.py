from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class AddEmailsSingleOptIn:
    emails: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AddEmailsSingleOptIn:
        return cls(
            emails=data.get("emails"),
        )
