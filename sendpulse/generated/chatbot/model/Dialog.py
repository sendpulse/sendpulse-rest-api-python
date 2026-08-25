from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Dialog:
    _id: str | None = None
    bot_id: str | None = None
    contact: dict[str, Any] | None = None
    last_inbox_message: dict[str, Any] | None = None
    last_outbox_message: dict[str, Any] | None = None
    service: int | None = None
    user_id: int | None = None
    inbox_unread_count: int | None = None
    is_chat_opened: bool | None = None
    created_at: str | None = None
    updated_at: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Dialog:
        return cls(
            _id=data.get("_id"),
            bot_id=data.get("bot_id"),
            contact=data.get("contact"),
            last_inbox_message=data.get("last_inbox_message"),
            last_outbox_message=data.get("last_outbox_message"),
            service=data.get("service"),
            user_id=data.get("user_id"),
            inbox_unread_count=data.get("inbox_unread_count"),
            is_chat_opened=data.get("is_chat_opened"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )
