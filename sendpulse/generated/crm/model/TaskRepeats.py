from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TaskRepeats:
    type: int | None = None
    startDate: str | None = None
    endSetting: dict[str, Any] | None = None
    setting: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TaskRepeats:
        return cls(
            type=data.get("type"),
            startDate=data.get("startDate"),
            endSetting=data.get("endSetting"),
            setting=data.get("setting"),
        )
