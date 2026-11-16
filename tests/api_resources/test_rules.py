# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestRules:
    @smoke_case("rules.listRulesets:single", operation="listRulesets", path="/v1/rulesets/{namespace}")
    def test_method_list_rulesets(self) -> None:
        rule = client.rules.list_rulesets(
            namespace="acme",
        )

    @smoke_case("rules.createRuleset:required", operation="createRuleset", path="/v1/rulesets/{namespace}")
    def test_method_create_ruleset(self) -> None:
        rule = client.rules.create_ruleset(
            namespace="acme",
            title="Acme API Rules",
            slug="acme-rules",
            document='extends: ["spectral:oas"]\nrules:\n  info-contact: warn\n',
        )

    @smoke_case("rules.createRuleset:all", operation="createRuleset", path="/v1/rulesets/{namespace}")
    def test_method_create_ruleset_with_all_params(self) -> None:
        rule = client.rules.create_ruleset(
            namespace="acme",
            title="Acme API Rules",
            description="API for managing Acme products and orders.",
            slug="acme-rules",
            is_private=False,
            document='extends: ["spectral:oas"]\nrules:\n  info-contact: warn\n',
        )

    @smoke_case("rules.updateRuleset:required", operation="updateRuleset", path="/v1/rulesets/{namespace}/{slug}")
    def test_method_update_ruleset(self) -> None:
        rule = client.rules.update_ruleset(
            path_namespace="acme",
            path_slug="acme-rules",
        )

    @smoke_case("rules.updateRuleset:all", operation="updateRuleset", path="/v1/rulesets/{namespace}/{slug}")
    def test_method_update_ruleset_with_all_params(self) -> None:
        rule = client.rules.update_ruleset(
            path_namespace="acme",
            path_slug="acme-rules",
            body_namespace="acme",
            body_slug="acme-rules",
            title="Acme API Rules",
            description="API for managing Acme products and orders.",
            is_private=False,
        )

    @smoke_case("rules.deleteRuleset:single", operation="deleteRuleset", path="/v1/rulesets/{namespace}/{slug}")
    def test_method_delete_ruleset(self) -> None:
        rule = client.rules.delete_ruleset(
            namespace="acme",
            slug="acme-rules",
        )

    @smoke_case(
        "rules.retrieveRulesetDocument:single",
        operation="retrieveRulesetDocument",
        path="/v1/rulesets/{namespace}/{slug}",
    )
    def test_method_retrieve_ruleset_document(self) -> None:
        rule = client.rules.retrieve_ruleset_document(
            namespace="acme",
            slug="acme-rules",
        )

    @smoke_case(
        "rules.createRulesetAccessGroup:single",
        operation="createRulesetAccessGroup",
        path="/v1/rulesets/{namespace}/{slug}/access-group",
    )
    def test_method_create_ruleset_access_group(self) -> None:
        rule = client.rules.create_ruleset_access_group(
            namespace="acme",
            slug="acme-rules",
            access_group_slug="acme-api",
        )

    @smoke_case(
        "rules.deleteRulesetAccessGroup:single",
        operation="deleteRulesetAccessGroup",
        path="/v1/rulesets/{namespace}/{slug}/access-group",
    )
    def test_method_delete_ruleset_access_group(self) -> None:
        rule = client.rules.delete_ruleset_access_group(
            namespace="acme",
            slug="acme-rules",
            access_group_slug="acme-api",
        )
