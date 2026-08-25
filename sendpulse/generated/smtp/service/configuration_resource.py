from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.smtp.model.DomainList import DomainList
from sendpulse.generated.smtp.model.DomainResult import DomainResult
from sendpulse.generated.smtp.model.ResultTrue import ResultTrue
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ConfigurationResource(AbstractService):
    def get_smtp_ips(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/smtp/ips",
        ))

    def get_smtp_senders(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/smtp/senders",
        ))

    def get_smtp_allowed_domains(self) -> DomainList:
        return DomainList.from_dict(self._send(Request(
            method="GET",
            uri="/v2/email-service/smtp/sender_domains",
        )))

    def add_smtp_sender(self, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="POST",
            uri="/senders",
            body=json.dumps(body) if body else None,
        )))

    def add_smtp_domain(self, domain: str) -> DomainResult:
        return DomainResult.from_dict(self._send(Request(
            method="POST",
            uri=f"/v2/email-service/smtp/sender_domains/{domain}",
        )))
