from __future__ import annotations

from sendpulse.service.abstract import AbstractService
from sendpulse.generated.email.service.mailing_lists_resource import MailingListsResource
from sendpulse.generated.email.service.email_address_resource import EmailAddressResource
from sendpulse.generated.email.service.campaigns_resource import CampaignsResource
from sendpulse.generated.email.service.templates_resource import TemplatesResource
from sendpulse.generated.email.service.senders_resource import SendersResource
from sendpulse.generated.email.service.tags_resource import TagsResource
from sendpulse.generated.email.service.blacklist_resource import BlacklistResource
from sendpulse.generated.email.service.balance_resource import BalanceResource
from sendpulse.generated.email.service.webhooks_resource import WebhooksResource


class EmailService(AbstractService):
    def mailing_lists(self) -> MailingListsResource:
        return MailingListsResource(self._client)

    def email_address(self) -> EmailAddressResource:
        return EmailAddressResource(self._client)

    def campaigns(self) -> CampaignsResource:
        return CampaignsResource(self._client)

    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    def senders(self) -> SendersResource:
        return SendersResource(self._client)

    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    def blacklist(self) -> BlacklistResource:
        return BlacklistResource(self._client)

    def balance(self) -> BalanceResource:
        return BalanceResource(self._client)

    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)
