from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ComplianceResource(AbstractService):
    def get_sms_blacklist(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/sms/black_list",
        ))

    def add_sms_blacklist(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/sms/black_list",
            body=json.dumps(body) if body else None,
        ))

    def remove_sms_blacklist(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri="/sms/black_list",
            body=json.dumps(body) if body else None,
        ))
