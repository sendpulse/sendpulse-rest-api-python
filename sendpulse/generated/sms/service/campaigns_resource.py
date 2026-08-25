from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.sms.model.CampaignCreation import CampaignCreation
from sendpulse.generated.sms.model.CampaignDelivery import CampaignDelivery
from sendpulse.generated.sms.model.CostEstimate import CostEstimate
from sendpulse.generated.sms.model.ResultTrue import ResultTrue
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class CampaignsResource(AbstractService):
    def create_sms_campaign(self, body: dict[str, Any] | list[Any] | None = None) -> CampaignCreation:
        return CampaignCreation.from_dict(self._send(Request(
            method="POST",
            uri="/sms/campaigns",
            body=json.dumps(body) if body else None,
        )))

    def delete_sms_campaign(self, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="DELETE",
            uri="/sms/campaigns",
            body=json.dumps(body) if body else None,
        )))

    def send_sms_to_numbers(self, body: dict[str, Any] | list[Any] | None = None) -> CampaignDelivery:
        return CampaignDelivery.from_dict(self._send(Request(
            method="POST",
            uri="/sms/send",
            body=json.dumps(body) if body else None,
        )))

    def get_sms_campaigns(self, dateFrom: str | None = None, dateTo: str | None = None) -> dict[str, Any]:
        params = {k: v for k, v in {"dateFrom": dateFrom, "dateTo": dateTo}.items() if v is not None}
        return self._send(Request(
            method="GET",
            uri="/sms/campaigns/list",
            params=params or None,
        ))

    def get_sms_campaign_info(self, id: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/sms/campaigns/info/{id}",
        ))

    def cancel_sms_campaign(self, id: int) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="PUT",
            uri=f"/sms/campaigns/cancel/{id}",
        )))

    def calculate_sms_cost(self, body: str, sender: str, addressBookId: int | None = None, phones: list[Any] | None = None, route: dict[str, Any] | None = None) -> CostEstimate:
        params = {k: v for k, v in {"addressBookId": addressBookId, "phones": phones, "body": body, "sender": sender, "route": route}.items() if v is not None}
        return CostEstimate.from_dict(self._send(Request(
            method="GET",
            uri="/sms/campaigns/cost",
            params=params or None,
        )))
