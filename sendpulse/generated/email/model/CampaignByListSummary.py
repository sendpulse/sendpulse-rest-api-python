from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CampaignByListSummary:
    task_id: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CampaignByListSummary:
        return cls(
            task_id=data.get("task_id"),
        )
