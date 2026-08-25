from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CampaignUpdateRequest:
    name: str | None = None
    subject: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CampaignUpdateRequest:
        return cls(
            name=data.get("name"),
            subject=data.get("subject"),
        )
