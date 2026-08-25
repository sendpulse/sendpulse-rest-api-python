from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.smtp.model.EmailRecord import EmailRecord
from sendpulse.generated.smtp.model.SentEmail import SentEmail
from sendpulse.generated.smtp.model.TotalCount import TotalCount
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class EmailsResource(AbstractService):
    def get_smtp_emails(self, limit: int | None = None, offset: int | None = None, from_: str | None = None, to: str | None = None, sender: str | None = None, recipient: str | None = None, country: str | None = None) -> list[EmailRecord]:
        params = {k: v for k, v in {"limit": limit, "offset": offset, "from": from_, "to": to, "sender": sender, "recipient": recipient, "country": country}.items() if v is not None}
        return [EmailRecord.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri="/smtp/emails",
            params=params or None,
        ))]

    def send_smtp_email(self, body: dict[str, Any] | list[Any] | None = None) -> SentEmail:
        return SentEmail.from_dict(self._send(Request(
            method="POST",
            uri="/smtp/emails",
            body=json.dumps(body) if body else None,
        )))

    def get_smtp_emails_total(self) -> TotalCount:
        return TotalCount.from_dict(self._send(Request(
            method="GET",
            uri="/smtp/emails/total",
        )))

    def get_smtp_email_info(self, id: str) -> EmailRecord:
        return EmailRecord.from_dict(self._send(Request(
            method="GET",
            uri=f"/smtp/emails/{id}",
        )))

    def get_smtp_emails_batch_info(self, body: dict[str, Any] | list[Any] | None = None) -> list[EmailRecord]:
        return [EmailRecord.from_dict(i) for i in self._send_list(Request(
            method="POST",
            uri="/smtp/emails/info",
            body=json.dumps(body) if body else None,
        ))]
