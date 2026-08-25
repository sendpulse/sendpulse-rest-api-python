from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class User:
    id: int | None = None
    firstname: str | None = None
    lastname: str | None = None
    email: str | None = None
    avatar: str | None = None
    lang: str | None = None
    timezone: int | None = None
    currency: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> User:
        return cls(
            id=data.get("id"),
            firstname=data.get("firstname"),
            lastname=data.get("lastname"),
            email=data.get("email"),
            avatar=data.get("avatar"),
            lang=data.get("lang"),
            timezone=data.get("timezone"),
            currency=data.get("currency"),
        )
