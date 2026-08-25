from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class AddEmailsDoubleOptIn:
    emails: list[Any] | None = None
    confirmation: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AddEmailsDoubleOptIn:
        return cls(
            emails=data.get("emails"),
            confirmation=data.get("confirmation"),
        )
