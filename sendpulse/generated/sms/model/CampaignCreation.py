from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CampaignCreation:
    result: bool | None = None
    campaign_id: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CampaignCreation:
        return cls(
            result=data.get("result"),
            campaign_id=data.get("campaign_id"),
        )
