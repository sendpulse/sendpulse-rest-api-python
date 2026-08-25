from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CampaignDelivery:
    result: bool | None = None
    campaign_id: int | None = None
    counters: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CampaignDelivery:
        return cls(
            result=data.get("result"),
            campaign_id=data.get("campaign_id"),
            counters=data.get("counters"),
        )
