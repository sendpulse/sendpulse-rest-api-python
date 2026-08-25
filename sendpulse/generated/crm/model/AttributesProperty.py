from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class AttributesProperty:
    pass

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AttributesProperty:
        return cls()
