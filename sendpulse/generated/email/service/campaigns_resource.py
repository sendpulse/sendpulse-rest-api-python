from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.email.model.CampaignByListSummary import CampaignByListSummary
from sendpulse.generated.email.model.CampaignCreateResponse import CampaignCreateResponse
from sendpulse.generated.email.model.CampaignDetails import CampaignDetails
from sendpulse.generated.email.model.CampaignSummary import CampaignSummary
from sendpulse.generated.email.model.ReferralStat import ReferralStat
from sendpulse.generated.email.model.ResultTrue import ResultTrue
from sendpulse.generated.email.model.ResultTrueWithId import ResultTrueWithId
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class CampaignsResource(AbstractService):
    def get_campaigns(self, limit: int | None = None, offset: int | None = None, order: str | None = None, status: list[Any] | None = None, planed: bool | None = None) -> list[CampaignSummary]:
        params = {k: v for k, v in {"limit": limit, "offset": offset, "order": order, "status": status, "planed": planed}.items() if v is not None}
        return [CampaignSummary.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri="/campaigns",
            params=params or None,
        ))]

    def create_campaign(self, body: dict[str, Any] | list[Any] | None = None) -> CampaignCreateResponse:
        return CampaignCreateResponse.from_dict(self._send(Request(
            method="POST",
            uri="/campaigns",
            body=json.dumps(body) if body else None,
        )))

    def get_campaign_by_id(self, id: int) -> CampaignDetails:
        return CampaignDetails.from_dict(self._send(Request(
            method="GET",
            uri=f"/campaigns/{id}",
        )))

    def update_campaign(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> ResultTrueWithId:
        return ResultTrueWithId.from_dict(self._send(Request(
            method="PATCH",
            uri=f"/campaigns/{id}",
            body=json.dumps(body) if body else None,
        )))

    def cancel_campaign(self, id: int) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="DELETE",
            uri=f"/campaigns/{id}",
        )))

    def get_campaign_country_stats(self, id: int) -> dict[str, Any]:
        return self._send(Request(
            method="GET",
            uri=f"/campaigns/{id}/countries",
        ))

    def get_campaign_referral_stats(self, id: int) -> list[ReferralStat]:
        return [ReferralStat.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri=f"/campaigns/{id}/referrals",
        ))]

    def get_campaigns_by_list(self, id: int, limit: int | None = None, offset: int | None = None) -> list[CampaignByListSummary]:
        params = {k: v for k, v in {"limit": limit, "offset": offset}.items() if v is not None}
        return [CampaignByListSummary.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri=f"/addressbooks/{id}/campaigns",
            params=params or None,
        ))]
