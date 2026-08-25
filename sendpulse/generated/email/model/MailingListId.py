from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class MailingListId:
    id: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MailingListId:
        return cls(
            id=data.get("id"),
        )
