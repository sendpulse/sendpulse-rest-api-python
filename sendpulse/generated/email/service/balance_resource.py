from __future__ import annotations

from typing import Any

from sendpulse.generated.email.model.BalanceResponse import BalanceResponse
from sendpulse.generated.email.model.DetailedBalanceResponse import DetailedBalanceResponse
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class BalanceResource(AbstractService):
    def get_balance(self) -> BalanceResponse:
        return BalanceResponse.from_dict(self._send(Request(
            method="GET",
            uri="/balance",
        )))

    def get_balance_by_currency(self, currency: str) -> BalanceResponse:
        return BalanceResponse.from_dict(self._send(Request(
            method="GET",
            uri=f"/balance/{currency}",
        )))

    def get_detailed_balance(self) -> DetailedBalanceResponse:
        return DetailedBalanceResponse.from_dict(self._send(Request(
            method="GET",
            uri="/user/balance/detail",
        )))
