from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class TelephonyResource(AbstractService):
    def get_telephony_calls(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/telephony/calls/get-list",
            body=json.dumps(body) if body else None,
        ))

    def get_contact_calls(self, contactId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/contacts/{contactId}/get-calls",
            body=json.dumps(body) if body else None,
        ))

    def get_deal_calls(self, dealId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/deals/{dealId}/get-calls",
            body=json.dumps(body) if body else None,
        ))

    def attach_call_to_deal(self, dealId: int, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/deals/{dealId}/attach-call",
            body=json.dumps(body) if body else None,
        ))
