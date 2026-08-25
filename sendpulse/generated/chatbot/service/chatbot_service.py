from __future__ import annotations

from sendpulse.service.abstract import AbstractService
from sendpulse.generated.chatbot.service.dialogs_resource import DialogsResource
from sendpulse.generated.chatbot.service.account_resource import AccountResource
from sendpulse.generated.chatbot.service.bots_resource import BotsResource


class ChatbotService(AbstractService):
    def dialogs(self) -> DialogsResource:
        return DialogsResource(self._client)

    def account(self) -> AccountResource:
        return AccountResource(self._client)

    def bots(self) -> BotsResource:
        return BotsResource(self._client)
