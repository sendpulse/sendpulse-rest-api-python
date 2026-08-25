from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class EmailRecord:
    id: str | None = None
    sender: str | None = None
    total_size: int | None = None
    sender_ip: str | None = None
    smtp_answer_code: int | None = None
    smtp_answer_subcode: str | None = None
    smtp_answer_data: str | None = None
    used_ip: str | None = None
    recipient: str | None = None
    subject: str | None = None
    send_date: str | None = None
    tracking: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EmailRecord:
        return cls(
            id=data.get("id"),
            sender=data.get("sender"),
            total_size=data.get("total_size"),
            sender_ip=data.get("sender_ip"),
            smtp_answer_code=data.get("smtp_answer_code"),
            smtp_answer_subcode=data.get("smtp_answer_subcode"),
            smtp_answer_data=data.get("smtp_answer_data"),
            used_ip=data.get("used_ip"),
            recipient=data.get("recipient"),
            subject=data.get("subject"),
            send_date=data.get("send_date"),
            tracking=data.get("tracking"),
        )
