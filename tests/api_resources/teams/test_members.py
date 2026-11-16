# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestMembers:
    @smoke_case("teams.members.list:single", operation="list", path="/v1/teams/members")
    def test_method_list(self) -> None:
        member = client.teams.members.list()

    @smoke_case("teams.members.update:single", operation="update", path="/v1/teams/members/{uid}")
    def test_method_update(self) -> None:
        member = client.teams.members.update(
            uid="UakgbKJ5m9gl0JDMbcJqL",
            role="owner",
        )

    @smoke_case("teams.members.delete:single", operation="delete", path="/v1/teams/members/{uid}")
    def test_method_delete(self) -> None:
        member = client.teams.members.delete(
            uid="UakgbKJ5m9gl0JDMbcJqL",
        )
