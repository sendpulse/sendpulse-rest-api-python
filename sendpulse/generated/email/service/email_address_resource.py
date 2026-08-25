from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.email.model.EmailAcrossBooks import EmailAcrossBooks
from sendpulse.generated.email.model.EmailCampaignDeliveryInfo import EmailCampaignDeliveryInfo
from sendpulse.generated.email.model.EmailDetails import EmailDetails
from sendpulse.generated.email.model.ListContactInfo import ListContactInfo
from sendpulse.generated.email.model.ResultTrue import ResultTrue
from sendpulse.generated.email.model.SubscriberStats import SubscriberStats
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class EmailAddressResource(AbstractService):
    def update_contact_variables(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="POST",
            uri=f"/addressbooks/{id}/emails/variable",
            body=json.dumps(body) if body else None,
        )))

    def get_email_info(self, email: str) -> list[EmailAcrossBooks]:
        return [EmailAcrossBooks.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri=f"/emails/{email}",
        ))]

    def delete_email_globally(self, email: str) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="DELETE",
            uri=f"/emails/{email}",
        )))

    def get_email_details(self, email: str) -> list[EmailDetails]:
        return [EmailDetails.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri=f"/emails/{email}/details",
        ))]

    def get_multiple_emails_info(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/emails",
            body=json.dumps(body) if body else None,
        ))

    def get_email_campaign_stats(self, email: str) -> SubscriberStats:
        return SubscriberStats.from_dict(self._send(Request(
            method="GET",
            uri=f"/emails/{email}/campaigns",
        )))

    def get_email_campaign_info(self, id: int, email: str) -> EmailCampaignDeliveryInfo:
        return EmailCampaignDeliveryInfo.from_dict(self._send(Request(
            method="GET",
            uri=f"/campaigns/{id}/email/{email}",
        )))

    def get_email_from_list(self, id: int, email: str) -> ListContactInfo:
        return ListContactInfo.from_dict(self._send(Request(
            method="GET",
            uri=f"/addressbooks/{id}/emails/{email}",
        )))

    def get_multiple_emails_campaign_stats(self, body: dict[str, Any] | list[Any] | None = None) -> dict[str, Any]:
        return self._send(Request(
            method="POST",
            uri="/emails/campaigns",
            body=json.dumps(body) if body else None,
        ))
