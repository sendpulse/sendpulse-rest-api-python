from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CampaignDetails:
    id: int | None = None
    name: str | None = None
    status: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CampaignDetails:
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            status=data.get("status"),
        )
