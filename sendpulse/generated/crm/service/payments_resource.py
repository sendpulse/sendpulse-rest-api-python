from __future__ import annotations

import json
from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class PaymentsResource(AbstractService):
    def get_all_payments(self) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri="/payments/all",
        ))

    def get_deal_payments(self, dealId: str) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/payments/deals/{dealId}",
        ))

    def get_payments_by_contact_id(self, contactId: str) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/payments/contacts/{contactId}",
        ))

    def create_payment(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/payments",
            body=json.dumps(body) if body else None,
        ))

    def approve_payment(self, paymentId: float) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/payments/{paymentId}/approve",
        ))

    def cancel_payment(self, paymentId: float) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/payments/{paymentId}/cancel",
        ))
