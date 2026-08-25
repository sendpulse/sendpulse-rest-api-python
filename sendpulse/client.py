from __future__ import annotations

from typing import TYPE_CHECKING, Any
from urllib.parse import urlparse

from sendpulse.auth.auth import ApiKeyAuth, OAuthAuth
from sendpulse.auth.protocol import TokenStorageProtocol
from sendpulse.auth.token_manager import TokenManager
from sendpulse.auth.token_storage import FileTokenStorage
from sendpulse.config import Config
from sendpulse.http.httpx_client import HttpxClient
from sendpulse.http.protocol import HttpClient
from sendpulse.http.request import Request
from sendpulse.response.validator import ResponseValidator

_BASE_URL = "https://api.sendpulse.com"

if TYPE_CHECKING:
    from sendpulse.generated.chatbot.service.chatbot_service import ChatbotService
    from sendpulse.generated.crm.service.crm_service import CrmService
    from sendpulse.generated.email.service.email_service import EmailService
    from sendpulse.generated.sms.service.sms_service import SmsService
    from sendpulse.generated.smtp.service.smtp_service import SmtpService


class Client:
    def __init__(
        self,
        api_key: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        connect_timeout: float = 10.0,
        request_timeout: float = 30.0,
        cache_dir: str | None = None,
        token_storage: TokenStorageProtocol | None = None,
        http_client: HttpClient | None = None,
    ) -> None:
        self._config = Config(
            api_key=api_key,
            client_id=client_id,
            client_secret=client_secret,
            connect_timeout=connect_timeout,
            request_timeout=request_timeout,
            cache_dir=cache_dir,
        )
        self._http: HttpClient = http_client or HttpxClient(
            connect_timeout=self._config.connect_timeout,
            request_timeout=self._config.request_timeout,
        )
        self._auth = self._build_auth(token_storage)
        self._validator = ResponseValidator()

        self._email_service: EmailService | None = None
        self._smtp_service: SmtpService | None = None
        self._sms_service: SmsService | None = None
        self._crm_service: CrmService | None = None
        self._chatbot_service: ChatbotService | None = None

    def email_service(self) -> EmailService:
        from sendpulse.generated.email.service.email_service import EmailService
        if self._email_service is None:
            self._email_service = EmailService(self)
        return self._email_service

    def smtp_service(self) -> SmtpService:
        from sendpulse.generated.smtp.service.smtp_service import SmtpService
        if self._smtp_service is None:
            self._smtp_service = SmtpService(self)
        return self._smtp_service

    def sms_service(self) -> SmsService:
        from sendpulse.generated.sms.service.sms_service import SmsService
        if self._sms_service is None:
            self._sms_service = SmsService(self)
        return self._sms_service

    def crm_service(self) -> CrmService:
        from sendpulse.generated.crm.service.crm_service import CrmService
        if self._crm_service is None:
            self._crm_service = CrmService(self)
        return self._crm_service

    def chatbot_service(self) -> ChatbotService:
        from sendpulse.generated.chatbot.service.chatbot_service import ChatbotService
        if self._chatbot_service is None:
            self._chatbot_service = ChatbotService(self)
        return self._chatbot_service

    def close(self) -> None:
        if hasattr(self._http, "close"):
            self._http.close()

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def send(self, request: Request) -> dict[str, Any] | list[Any]:
        authed = self._with_auth(request)
        response = self._http.send(authed)

        if response.status_code == 401 and self._auth.supports_refresh():
            self._auth.invalidate()
            authed = self._with_auth(request)
            response = self._http.send(authed)

        return self._validator.validate(response)

    def _with_auth(self, request: Request) -> Request:
        uri = request.uri.lstrip("/")
        if urlparse(uri).scheme:
            raise ValueError(f"Request URI must be a relative path, got: {uri!r}")

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            **request.headers,
            # Applied last so caller headers cannot override SDK authentication.
            "Authorization": self._auth.get_authorization_header(),
        }
        return Request(
            method=request.method,
            uri=f"{_BASE_URL}/{uri}",
            headers=headers,
            body=request.body,
            params=request.params,
        )

    def _build_auth(self, token_storage: TokenStorageProtocol | None) -> ApiKeyAuth | OAuthAuth:
        if not self._config.is_oauth:
            return ApiKeyAuth(self._config.api_key or "")

        storage: TokenStorageProtocol = token_storage or FileTokenStorage(self._config.cache_dir)
        manager = TokenManager(
            http_client=self._http,
            client_id=self._config.client_id or "",
            client_secret=self._config.client_secret or "",
            base_url=_BASE_URL,
            storage=storage,
        )
        return OAuthAuth(manager)
