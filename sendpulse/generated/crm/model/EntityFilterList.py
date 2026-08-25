from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class EntityFilterList:
    pass

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EntityFilterList:
        return cls()
