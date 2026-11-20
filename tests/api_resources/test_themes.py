# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestThemes:
    @smoke_case("themes.list:single", operation="list", path="/v1/themes")
    def test_method_list(self) -> None:
        theme = client.themes.list()

    @smoke_case("themes.create:required", operation="create", path="/v1/themes")
    def test_method_create(self) -> None:
        theme = client.themes.create(
            name="Acme Theme",
            slug="acme-theme",
            document=":root { --scalar-color-1: #1f2937; }",
        )

    @smoke_case("themes.create:all", operation="create", path="/v1/themes")
    def test_method_create_with_all_params(self) -> None:
        theme = client.themes.create(
            name="Acme Theme",
            description="API for managing Acme products and orders.",
            slug="acme-theme",
            document=":root { --scalar-color-1: #1f2937; }",
        )

    @smoke_case("themes.update:required", operation="update", path="/v1/themes/{slug}")
    def test_method_update(self) -> None:
        theme = client.themes.update(
            slug="acme-theme",
        )

    @smoke_case("themes.update:all", operation="update", path="/v1/themes/{slug}")
    def test_method_update_with_all_params(self) -> None:
        theme = client.themes.update(
            slug="acme-theme",
            name="Acme Theme",
            description="API for managing Acme products and orders.",
        )

    @smoke_case("themes.replaceDocument:single", operation="replaceDocument", path="/v1/themes/{slug}")
    def test_method_replace_document(self) -> None:
        theme = client.themes.replace_document(
            slug="acme-theme",
            document=":root { --scalar-color-1: #1f2937; }",
        )

    @smoke_case("themes.delete:single", operation="delete", path="/v1/themes/{slug}")
    def test_method_delete(self) -> None:
        theme = client.themes.delete(
            slug="acme-theme",
        )

    @smoke_case("themes.retrieve:single", operation="retrieve", path="/v1/themes/{slug}")
    def test_method_retrieve(self) -> None:
        theme = client.themes.retrieve(
            slug="acme-theme",
        )
