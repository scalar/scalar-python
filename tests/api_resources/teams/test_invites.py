# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestInvites:
    @smoke_case("teams.invites.member:single", operation="member", path="/v1/teams/invites")
    def test_method_member(self) -> None:
        invite = client.teams.invites.member(
            email="alex@example.com",
            role="owner",
        )

    @smoke_case("teams.invites.resend:single", operation="resend", path="/v1/teams/invites/{uid}")
    def test_method_resend(self) -> None:
        invite = client.teams.invites.resend(
            uid="UakgbKJ5m9gl0JDMbcJqL",
        )

    @smoke_case("teams.invites.cancel:single", operation="cancel", path="/v1/teams/invites/{uid}")
    def test_method_cancel(self) -> None:
        invite = client.teams.invites.cancel(
            uid="UakgbKJ5m9gl0JDMbcJqL",
        )
