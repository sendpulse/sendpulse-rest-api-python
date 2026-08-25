from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class MailingList:
    id: int | None = None
    name: str | None = None
    all_email_qty: int | None = None
    active_email_qty: int | None = None
    inactive_email_qty: int | None = None
    creationdate: str | None = None
    status: int | None = None
    status_explain: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MailingList:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            all_email_qty=data.get("all_email_qty"),
            active_email_qty=data.get("active_email_qty"),
            inactive_email_qty=data.get("inactive_email_qty"),
            creationdate=data.get("creationdate"),
            status=data.get("status"),
            status_explain=data.get("status_explain"),
        )
