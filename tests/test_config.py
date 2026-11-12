import pytest

from sendpulse.config import Config


def test_api_key_only_is_valid() -> None:
    config = Config(api_key="my-key")
    assert config.api_key == "my-key"
    assert not config.is_oauth


def test_oauth_credentials_are_valid() -> None:
    config = Config(client_id="id", client_secret="secret")
    assert config.is_oauth


def test_raises_when_no_credentials() -> None:
    with pytest.raises(ValueError, match="api_key"):
        Config()


def test_raises_when_both_api_key_and_oauth() -> None:
    with pytest.raises(ValueError, match="not both"):
        Config(api_key="key", client_id="id", client_secret="secret")


def test_raises_when_partial_oauth() -> None:
    with pytest.raises(ValueError):
        Config(client_id="id")


def test_default_timeouts() -> None:
    config = Config(api_key="key")
    assert config.connect_timeout == 10.0
    assert config.request_timeout == 30.0


def test_custom_timeouts() -> None:
    config = Config(api_key="key", connect_timeout=5.0, request_timeout=15.0)
    assert config.connect_timeout == 5.0
    assert config.request_timeout == 15.0
