from __future__ import annotations

from sendpulse.service.abstract import AbstractService
from sendpulse.generated.sms.service.contacts_resource import ContactsResource
from sendpulse.generated.sms.service.compliance_resource import ComplianceResource
from sendpulse.generated.sms.service.campaigns_resource import CampaignsResource
from sendpulse.generated.sms.service.configuration_resource import ConfigurationResource


class SmsService(AbstractService):
    def contacts(self) -> ContactsResource:
        return ContactsResource(self._client)

    def compliance(self) -> ComplianceResource:
        return ComplianceResource(self._client)

    def campaigns(self) -> CampaignsResource:
        return CampaignsResource(self._client)

    def configuration(self) -> ConfigurationResource:
        return ConfigurationResource(self._client)
