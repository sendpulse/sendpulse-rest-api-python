from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ContactMessenger:
    id: int | None = None
    typeId: int | None = None
    login: str | None = None
    botId: str | None = None
    contactId: str | None = None
    status: int | None = None
    chatbotUrl: str | None = None
    isMainChatbot: bool | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContactMessenger:
        return cls(
            id=data.get("id"),
            typeId=data.get("typeId"),
            login=data.get("login"),
            botId=data.get("botId"),
            contactId=data.get("contactId"),
            status=data.get("status"),
            chatbotUrl=data.get("chatbotUrl"),
            isMainChatbot=data.get("isMainChatbot"),
        )
