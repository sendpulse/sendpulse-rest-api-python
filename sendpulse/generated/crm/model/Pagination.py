from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Pagination:
    currentPage: int | None = None
    lastPage: int | None = None
    perPage: int | None = None
    total: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Pagination:
        return cls(
            currentPage=data.get("currentPage"),
            lastPage=data.get("lastPage"),
            perPage=data.get("perPage"),
            total=data.get("total"),
        )
