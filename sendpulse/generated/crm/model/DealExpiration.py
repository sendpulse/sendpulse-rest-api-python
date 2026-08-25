from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class DealExpiration:
    date: str | None = None
    time: str | None = None
    dateTime: str | None = None
    notificationEnabled: bool | None = None
    notifyIn: str | None = None
    expired: bool | None = None
    expires_within_day: bool | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DealExpiration:
        return cls(
            date=data.get("date"),
            time=data.get("time"),
            dateTime=data.get("dateTime"),
            notificationEnabled=data.get("notificationEnabled"),
            notifyIn=data.get("notifyIn"),
            expired=data.get("expired"),
            expires_within_day=data.get("expires_within_day"),
        )
