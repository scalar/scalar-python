# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAccessGroups:
    @smoke_case("accessGroups.create:required", operation="create", path="/v1/access-groups")
    def test_method_create(self) -> None:
        access_group = client.access_groups.create()

    @smoke_case("accessGroups.create:all", operation="create", path="/v1/access-groups")
    def test_method_create_with_all_params(self) -> None:
        access_group = client.access_groups.create(
            name="Engineering",
            slug="engineering",
            allowed_domains="example.com",
        )

    @smoke_case("accessGroups.retrieve:single", operation="retrieve", path="/v1/access-groups/{slug}")
    def test_method_retrieve(self) -> None:
        access_group = client.access_groups.retrieve(
            slug="acme-api",
        )

    @smoke_case("accessGroups.update:required", operation="update", path="/v1/access-groups/{slug}")
    def test_method_update(self) -> None:
        access_group = client.access_groups.update(
            path_slug="acme-api",
        )

    @smoke_case("accessGroups.update:all", operation="update", path="/v1/access-groups/{slug}")
    def test_method_update_with_all_params(self) -> None:
        access_group = client.access_groups.update(
            path_slug="acme-api",
            name="Engineering",
            body_slug="engineering",
        )

    @smoke_case("accessGroups.delete:single", operation="delete", path="/v1/access-groups/{slug}")
    def test_method_delete(self) -> None:
        access_group = client.access_groups.delete(
            slug="acme-api",
        )
