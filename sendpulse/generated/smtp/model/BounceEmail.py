from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class BounceEmail:
    email_to: str | None = None
    sender: str | None = None
    send_date: str | None = None
    subject: str | None = None
    smtp_answer_code: int | None = None
    smtp_answer_subcode: str | None = None
    smtp_answer_data: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BounceEmail:
        return cls(
            email_to=data.get("email_to"),
            sender=data.get("sender"),
            send_date=data.get("send_date"),
            subject=data.get("subject"),
            smtp_answer_code=data.get("smtp_answer_code"),
            smtp_answer_subcode=data.get("smtp_answer_subcode"),
            smtp_answer_data=data.get("smtp_answer_data"),
        )
