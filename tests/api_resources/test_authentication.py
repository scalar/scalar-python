# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAuthentication:
    @smoke_case(
        "authentication.exchangePersonalToken:single", operation="exchangePersonalToken", path="/v1/auth/exchange"
    )
    def test_method_exchange_personal_token(self) -> None:
        authentication = client.authentication.exchange_personal_token(
            personal_token="scalar_example_personal_token",
        )

    @smoke_case("authentication.listCurrentUser:single", operation="listCurrentUser", path="/v1/auth/me")
    def test_method_list_current_user(self) -> None:
        authentication = client.authentication.list_current_user()
