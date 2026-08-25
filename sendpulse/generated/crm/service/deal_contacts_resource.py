from __future__ import annotations

from typing import Any

from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class DealContactsResource(AbstractService):
    def get_deal_contacts(self, dealId: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/deals/{dealId}/contacts",
        ))

    def add_contact_to_deal(self, dealId: int, contactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri=f"/deals/{dealId}/contacts/{contactId}",
        ))

    def remove_deal_contact(self, dealId: int, contactId: int) -> dict[str, Any]:
        return self._send(Request(
            method="DELETE",
            uri=f"/deals/{dealId}/contacts/{contactId}",
        ))
