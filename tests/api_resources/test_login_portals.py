# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestLoginPortals:
    @smoke_case("loginPortals.retrieve:single", operation="retrieve", path="/v1/login-portals/{slug}")
    def test_method_retrieve(self) -> None:
        login_portal = client.login_portals.retrieve(
            slug="acme-login",
        )

    @smoke_case("loginPortals.update:required", operation="update", path="/v1/login-portals/{slug}")
    def test_method_update(self) -> None:
        login_portal = client.login_portals.update(
            slug="acme-login",
        )

    @smoke_case("loginPortals.update:all", operation="update", path="/v1/login-portals/{slug}")
    def test_method_update_with_all_params(self) -> None:
        login_portal = client.login_portals.update(
            slug="acme-login",
            title="Acme Private Documentation",
        )

    @smoke_case("loginPortals.delete:single", operation="delete", path="/v1/login-portals/{slug}")
    def test_method_delete(self) -> None:
        login_portal = client.login_portals.delete(
            slug="acme-login",
        )

    @smoke_case("loginPortals.create:single", operation="create", path="/v1/login-portals")
    def test_method_create(self) -> None:
        login_portal = client.login_portals.create(
            title="Acme Private Documentation",
            slug="acme-login",
            email={
                "logo": "",
                "logo_size": "100",
                "button_text": "Login",
                "message": "Click to access private documentation hosted by scalar.com",
                "title": "Private Docs",
                "main_color": "#2a2f45",
                "main_background": "#f6f6f6",
                "card_color": "#2a2f45",
                "card_background": "#fff",
                "button_color": "#fff",
                "button_background": "#0f0f0f",
            },
            page={
                "title": "Scalar Private Docs",
                "description": "Login to access your documentation",
                "head": "",
                "script": "",
                "theme": "",
                "company_name": "",
                "logo": "",
                "logo_url": "",
                "favicon": "",
                "terms_link": "",
                "privacy_link": "",
                "form_title": "Scalar Private Docs",
                "form_description": "Login to access your documentation",
                "form_image": "",
            },
        )

    @smoke_case("loginPortals.list:single", operation="list", path="/v1/login-portals")
    def test_method_list(self) -> None:
        login_portal = client.login_portals.list()
