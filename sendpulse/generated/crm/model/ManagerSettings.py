from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ManagerSettings:
    sectionId: int | None = None
    responsibleId: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ManagerSettings:
        return cls(
            sectionId=data.get("sectionId"),
            responsibleId=data.get("responsibleId"),
        )
