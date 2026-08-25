from __future__ import annotations

from sendpulse.service.abstract import AbstractService
from sendpulse.generated.smtp.service.emails_resource import EmailsResource
from sendpulse.generated.smtp.service.bounces_resource import BouncesResource
from sendpulse.generated.smtp.service.unsubscribe_resource import UnsubscribeResource
from sendpulse.generated.smtp.service.configuration_resource import ConfigurationResource


class SmtpService(AbstractService):
    def emails(self) -> EmailsResource:
        return EmailsResource(self._client)

    def bounces(self) -> BouncesResource:
        return BouncesResource(self._client)

    def unsubscribe(self) -> UnsubscribeResource:
        return UnsubscribeResource(self._client)

    def configuration(self) -> ConfigurationResource:
        return ConfigurationResource(self._client)
