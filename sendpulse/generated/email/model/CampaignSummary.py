from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CampaignSummary:
    id: int | None = None
    name: str | None = None
    status: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CampaignSummary:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            status=data.get("status"),
        )
