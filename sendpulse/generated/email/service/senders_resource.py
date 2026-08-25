from __future__ import annotations

import json
from typing import Any

from sendpulse.generated.email.model.ResultTrue import ResultTrue
from sendpulse.generated.email.model.Sender import Sender
from sendpulse.generated.email.model.SenderActivationResponse import SenderActivationResponse
from sendpulse.http.request import Request
from sendpulse.service.abstract import AbstractService


class SendersResource(AbstractService):
    def get_senders(self) -> list[Sender]:
        return [Sender.from_dict(i) for i in self._send_list(Request(
            method="GET",
            uri="/senders",
        ))]

    def add_sender(self, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="POST",
            uri="/senders",
            body=json.dumps(body) if body else None,
        )))

    def delete_sender(self, body: dict[str, Any] | list[Any] | None = None) -> ResultTrue:
        return ResultTrue.from_dict(self._send(Request(
            method="DELETE",
            uri="/senders",
            body=json.dumps(body) if body else None,
        )))

    def request_sender_activation_code(self, email: str) -> SenderActivationResponse:
        return SenderActivationResponse.from_dict(self._send(Request(
            method="GET",
            uri=f"/senders/{email}/code",
        )))

    def activate_sender(self, email: str, body: dict[str, Any] | list[Any] | None = None) -> SenderActivationResponse:
        return SenderActivationResponse.from_dict(self._send(Request(
            method="POST",
            uri=f"/senders/{email}/code",
            body=json.dumps(body) if body else None,
        )))
