from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TelephonyCall:
    id: int | None = None
    integrationId: int | None = None
    integrationGroupId: int | None = None
    responsibleId: int | None = None
    phone: str | None = None
    callDuration: int | None = None
    callType: int | None = None
    state: int | None = None
    callRecordLink: str | None = None
    createdAt: str | None = None
    contact: dict[str, Any] | None = None
    deal: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TelephonyCall:
        return cls(
            id=data.get("id"),
            integrationId=data.get("integrationId"),
            integrationGroupId=data.get("integrationGroupId"),
            responsibleId=data.get("responsibleId"),
            phone=data.get("phone"),
            callDuration=data.get("callDuration"),
            callType=data.get("callType"),
            state=data.get("state"),
            callRecordLink=data.get("callRecordLink"),
            createdAt=data.get("createdAt"),
            contact=data.get("contact"),
            deal=data.get("deal"),
        )
