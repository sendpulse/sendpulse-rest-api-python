from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.email.model.CampaignCost import CampaignCost
from sendpulse.generated.email.model.EmailContact import EmailContact
from sendpulse.generated.email.model.EmailContactBasic import EmailContactBasic
from sendpulse.generated.email.model.MailingList import MailingList
from sendpulse.generated.email.model.MailingListId import MailingListId
from sendpulse.generated.email.model.ResultTrue import ResultTrue
from sendpulse.generated.email.model.TotalCount import TotalCount
from sendpulse.generated.email.model.VariableDefinition import VariableDefinition
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class MailingListsResource(AbstractService):
    def get_mailing_lists(self, limit: int | None = None, offset: int | None = None) -> list[MailingList]:
        params = {k: v for k, v in {"limit": limit, "offset": offset}.items() if v is not None}
        return [MailingList.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri="/addressbooks",
            params=params or None,
        ))]

    def create_mailing_list(self, body: dict[str, Any] | list[Any] | None = None) -> MailingListId:
        return MailingListId.from_dict(self._send(Request(
            method="POST",
            uri="/addressbooks",
            body=json.dumps(body) if body else None,
        )))

    def get_mailing_list_by_id(self, id: int) -> list[MailingList]:
        return [MailingList.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri=f"/addressbooks/{id}",
        ))]

    def update_mailing_list(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="PUT",
            uri=f"/addressbooks/{id}",
            body=json.dumps(body) if body else None,
        )))

    def delete_mailing_list(self, id: int) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="DELETE",
            uri=f"/addressbooks/{id}",
        )))

    def get_mailing_list_variables(self, id: int) -> list[VariableDefinition]:
        return [VariableDefinition.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri=f"/addressbooks/{id}/variables",
        ))]

    def get_emails_from_mailing_list(self, id: int, limit: int | None = None, offset: int | None = None, order: str | None = None, active: bool | None = None, not_active: bool | None = None) -> list[EmailContact]:
        params = {k: v for k, v in {"limit": limit, "offset": offset, "order": order, "active": active, "not_active": not_active}.items() if v is not None}
        return [EmailContact.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri=f"/addressbooks/{id}/emails",
            params=params or None,
        ))]

    def add_emails_to_mailing_list(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="POST",
            uri=f"/addressbooks/{id}/emails",
            body=json.dumps(body) if body else None,
        )))

    def delete_emails_from_mailing_list(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="DELETE",
            uri=f"/addressbooks/{id}/emails",
            body=json.dumps(body) if body else None,
        )))

    def get_emails_total_count(self, id: int, active: bool | None = None) -> TotalCount:
        params = {k: v for k, v in {"active": active}.items() if v is not None}
        return TotalCount.from_dict(self._send(Request(
            method="GET",
            uri=f"/addressbooks/{id}/emails/total",
            params=params or None,
        )))

    def unsubscribe_emails_from_mailing_list(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="POST",
            uri=f"/addressbooks/{id}/emails/unsubscribe",
            body=json.dumps(body) if body else None,
        )))

    def get_contacts_by_variable(self, id: int, variableName: str, searchValue: str) -> list[EmailContactBasic]:
        return [EmailContactBasic.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri=f"/addressbooks/{id}/variables/{variableName}/{searchValue}",
        ))]

    def update_contact_phone(self, id: int, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="PUT",
            uri=f"/addressbooks/{id}/phone",
            body=json.dumps(body) if body else None,
        )))

    def get_campaign_cost_by_list(self, id: int) -> CampaignCost:
        return CampaignCost.from_dict(self._send(Request(
            method="GET",
            uri=f"/addressbooks/{id}/cost",
        )))
