"""Integrity of the generated operation map."""
from __future__ import annotations

import re

import pytest

from sendpulse.resources import load_operations

HTTP_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE"}
# int/float/bool/string/array/mixed, optionally with a trailing "!" (required).
TYPE_RE = re.compile(r"^(int|float|bool|string|array|mixed)!?$")

OPERATIONS = load_operations()


def test_expected_total_count() -> None:
    # Tracks the current spec snapshot across all 19 services.
    assert len(OPERATIONS) == 793


def test_all_services_present() -> None:
    services = {key.split(".")[0] for key in OPERATIONS}
    assert services == {
        "a360", "chatbot", "crm", "edu", "email", "facebook", "file-manager",
        "instagram", "live-chat", "popups", "sms", "smtp", "telegram", "tiktok",
        "verifier", "viber", "viber-chatbot", "web-push", "whatsapp",
    }


@pytest.mark.parametrize("key", list(OPERATIONS))
def test_operation_shape(key: str) -> None:
    op = OPERATIONS[key]

    assert len(key.split(".")) == 3, f"key not 3-part: {key}"
    assert op["method"] in HTTP_METHODS
    assert op["path"].startswith("/")
    assert isinstance(op["params"], dict)

    for name, type_ in op["params"].items():
        assert TYPE_RE.match(type_), f"bad type {type_!r} for {name} in {key}"

    # Every {placeholder} in the path must be a required param.
    for placeholder in re.findall(r"\{(\w+)\}", op["path"]):
        assert placeholder in op["params"], f"path param {placeholder} missing in {key}"
        assert op["params"][placeholder].endswith("!"), f"path param {placeholder} not required in {key}"


def test_loader_is_cached() -> None:
    assert load_operations() is load_operations()
