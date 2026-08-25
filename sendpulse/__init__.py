__version__ = "2.0.0"
__author__ = "Maksym Ustymenko"
__author_email__ = "tech@sendpulse.com"
__copyright__ = "Copyright 2015, SendPulse"
__credits__ = ["Maksym Ustymenko"]

from sendpulse.client import Client
from sendpulse.exception.exceptions import (
    ApiException,
    AuthException,
    NetworkException,
    ProtocolException,
    RateLimitException,
    SendPulseError,
    SendPulseException,
)

__all__ = [
    "Client",
    "SendPulseError",
    "SendPulseException",
    "AuthException",
    "RateLimitException",
    "ApiException",
    "NetworkException",
    "ProtocolException",
]
