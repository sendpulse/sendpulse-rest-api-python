from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ListContactInfo:
    email: str | None = None
    abook_id: str | None = None
    phone: str | None = None
    status: int | None = None
    status_explain: str | None = None
    variables: list[Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ListContactInfo:
        return cls(
            email=data.get("email"),
            abook_id=data.get("abook_id"),
            phone=data.get("phone"),
            status=data.get("status"),
            status_explain=data.get("status_explain"),
            variables=data.get("variables"),
        )
