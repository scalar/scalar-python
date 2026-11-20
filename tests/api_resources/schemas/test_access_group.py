# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAccessGroup:
    @smoke_case(
        "schemas.accessGroup.create:single", operation="create", path="/v1/schemas/{namespace}/{slug}/access-group"
    )
    def test_method_create(self) -> None:
        access_group = client.schemas.access_group.create(
            namespace="acme",
            slug="customer",
            access_group_slug="acme-api",
        )

    @smoke_case(
        "schemas.accessGroup.delete:single", operation="delete", path="/v1/schemas/{namespace}/{slug}/access-group"
    )
    def test_method_delete(self) -> None:
        access_group = client.schemas.access_group.delete(
            namespace="acme",
            slug="customer",
            access_group_slug="acme-api",
        )
