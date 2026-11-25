# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestTeams:
    @smoke_case("teams.list:single", operation="list", path="/v1/teams")
    def test_method_list(self) -> None:
        team = client.teams.list()
