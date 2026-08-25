from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Messenger:
    id: int | None = None
    typeId: int | None = None
    login: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Messenger:
        return cls(
            id=data.get("id"),
            typeId=data.get("typeId"),
            login=data.get("login"),
        )
