from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class FilterExpressionProperty:
    pass

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> FilterExpressionProperty:
        return cls()
