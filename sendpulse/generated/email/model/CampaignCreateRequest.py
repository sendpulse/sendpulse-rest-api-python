from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class CampaignCreateRequest:
    sender_name: str | None = None
    sender_email: str | None = None
    subject: str | None = None
    body: str | None = None
    template_id: Any = None
    list_id: Any = None
    segment_id: int | None = None
    is_test: bool | None = None
    send_date: str | None = None
    name: str | None = None
    use_dynamic_list: bool | None = None
    attachments: dict[str, Any] | None = None
    attachments_binary: dict[str, Any] | None = None
    type: str | None = None
    body_amp: str | None = None
    stats: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CampaignCreateRequest:
        return cls(
            sender_name=data.get("sender_name"),
            sender_email=data.get("sender_email"),
            subject=data.get("subject"),
            body=data.get("body"),
            template_id=data.get("template_id"),
            list_id=data.get("list_id"),
            segment_id=data.get("segment_id"),
            is_test=data.get("is_test"),
            send_date=data.get("send_date"),
            name=data.get("name"),
            use_dynamic_list=data.get("use_dynamic_list"),
            attachments=data.get("attachments"),
            attachments_binary=data.get("attachments_binary"),
            type=data.get("type"),
            body_amp=data.get("body_amp"),
            stats=data.get("stats"),
        )
