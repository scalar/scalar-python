# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestDomains:
    @smoke_case("accessGroups.domains.create:single", operation="create", path="/v1/access-groups/{slug}/domains")
    def test_method_create(self) -> None:
        domain = client.access_groups.domains.create(
            slug="acme-api",
            domain="example.com",
        )

    @smoke_case("accessGroups.domains.delete:single", operation="delete", path="/v1/access-groups/{slug}/domains")
    def test_method_delete(self) -> None:
        domain = client.access_groups.domains.delete(
            slug="acme-api",
            domain="example.com",
        )
