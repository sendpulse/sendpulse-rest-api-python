from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class EmailCampaignDeliveryInfo:
    sent_date: str | None = None
    global_status: int | None = None
    global_status_explain: str | None = None
    detail_status: int | None = None
    detail_status_explain: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EmailCampaignDeliveryInfo:
        return cls(
            sent_date=data.get("sent_date"),
            global_status=data.get("global_status"),
            global_status_explain=data.get("global_status_explain"),
            detail_status=data.get("detail_status"),
            detail_status_explain=data.get("detail_status_explain"),
        )
