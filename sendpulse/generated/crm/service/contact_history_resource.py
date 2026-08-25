from __future__ import annotations

from typing import Any

from sendpulse.generated.crm.model.ContactHistory import ContactHistory
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class ContactHistoryResource(AbstractService):
    def get_contact_history(self, contactId: int, fromDate: str, toDate: str) -> list[ContactHistory]:
        params = {k: v for k, v in {"fromDate": fromDate, "toDate": toDate}.items() if v is not None}
        return [ContactHistory.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri=f"/contacts/{contactId}/history",
            params=params or None,
        ))]
