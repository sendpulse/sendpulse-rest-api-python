from __future__ import annotations


class SendPulseError(Exception):
    """Base class for all exceptions raised by this SDK."""


class SendPulseException(SendPulseError):
    """API-level error — carries HTTP status and raw response body."""

    def __init__(self, http_status: int, raw_body: str, message: str = "") -> None:
        self.http_status = http_status
        self.raw_body = raw_body
        super().__init__(message or raw_body)


class AuthException(SendPulseException):
    """401 / 403 — wrong credentials or insufficient permissions."""


class RateLimitException(SendPulseException):
    """429 — too many requests."""


class ApiException(SendPulseException):
    """Any other 4xx / 5xx response from the API."""


class NetworkException(SendPulseError):
    """Transport-level error — connection refused, timeout, DNS failure, etc."""


class ProtocolException(SendPulseError):
    """Response received but could not be parsed (malformed JSON from the API)."""
