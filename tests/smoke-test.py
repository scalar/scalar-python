# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke test: calls every generated operation once to confirm the SDK can reach each endpoint.
# Run it from this repo with `python tests/smoke-test.py`. The generator also runs this file
# against a mock server and reads the JSON report produced via SCALAR_SMOKE_REPORT.
from __future__ import annotations

import json
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, TypedDict

from scalar_sdk import Scalar

# The shared smoke-test runner injects base URL and credentials through the same
# environment variables the generated client reads in normal use.
client = Scalar(max_retries=0, timeout=30)


class SmokeResult(TypedDict, total=False):
    operation: str
    method: str
    path: str
    label: str
    status: str
    durationMs: int
    error: str


class _SmokeCaseBase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


# `label` says which of an operation's two calls this is — "required params" or "all params".
# It sits in a total=False extension because it is absent when the operation contributed a
# single case, while the fields above are always present.
class SmokeCase(_SmokeCaseBase, total=False):
    label: str


def _smoke_case_0() -> None:
    registry = client.registry.list_all_api_documents()


def _smoke_case_1() -> None:
    registry = client.registry.list_api_documents(
        namespace="namespace",
    )


def _smoke_case_2() -> None:
    registry = client.registry.create_api_document(
        namespace="namespace",
        title="",
        version="x",
        slug="",
        document="",
    )


def _smoke_case_3() -> None:
    registry = client.registry.create_api_document(
        namespace="namespace",
        title="",
        description="",
        version="x",
        slug="",
        ruleset="",
        is_private=False,
        document="",
    )


def _smoke_case_4() -> None:
    registry = client.registry.update_api_document(
        namespace="namespace",
        slug="slug",
    )


def _smoke_case_5() -> None:
    registry = client.registry.update_api_document(
        namespace="namespace",
        slug="slug",
        title="",
        description="",
        is_private=False,
        ruleset="",
    )


def _smoke_case_6() -> None:
    registry = client.registry.delete_api_document(
        namespace="namespace",
        slug="slug",
    )


def _smoke_case_7() -> None:
    registry = client.registry.retrieve_api_document_version(
        namespace="namespace",
        slug="slug",
        semver="semver",
    )


def _smoke_case_8() -> None:
    registry = client.registry.update_api_document_version(
        namespace="namespace",
        slug="slug",
        semver="semver",
        document="",
    )


def _smoke_case_9() -> None:
    registry = client.registry.update_api_document_version(
        namespace="namespace",
        slug="slug",
        semver="semver",
        document="",
        last_known_version_sha="",
    )


def _smoke_case_10() -> None:
    registry = client.registry.delete_api_document_version(
        namespace="namespace",
        slug="slug",
        semver="semver",
    )


def _smoke_case_11() -> None:
    registry = client.registry.list_api_document_version_metadata(
        namespace="namespace",
        slug="slug",
        semver="semver",
    )


def _smoke_case_12() -> None:
    registry = client.registry.create_api_document_version(
        namespace="namespace",
        slug="slug",
        version="x",
        document="",
    )


def _smoke_case_13() -> None:
    registry = client.registry.create_api_document_version(
        namespace="namespace",
        slug="slug",
        version="x",
        document="",
        force=False,
        last_known_version_sha="",
    )


def _smoke_case_14() -> None:
    registry = client.registry.create_api_document_access_group(
        namespace="namespace",
        slug="slug",
        access_group_slug="xxx",
    )


def _smoke_case_15() -> None:
    registry = client.registry.delete_api_document_access_group(
        namespace="namespace",
        slug="slug",
        access_group_slug="xxx",
    )


def _smoke_case_16() -> None:
    schema = client.schemas.list(
        namespace="namespace",
    )


def _smoke_case_17() -> None:
    schema = client.schemas.create(
        namespace="namespace",
        title="",
        version="x",
        slug="",
        document="",
    )


def _smoke_case_18() -> None:
    schema = client.schemas.create(
        namespace="namespace",
        title="",
        description="",
        version="x",
        slug="",
        is_private=False,
        document="",
    )


def _smoke_case_19() -> None:
    schema = client.schemas.update(
        namespace="namespace",
        slug="slug",
    )


def _smoke_case_20() -> None:
    schema = client.schemas.update(
        namespace="namespace",
        slug="slug",
        title="",
        description="",
        is_private=False,
    )


def _smoke_case_21() -> None:
    schema = client.schemas.delete(
        namespace="namespace",
        slug="slug",
    )


def _smoke_case_22() -> None:
    version = client.schemas.version.retrieve(
        namespace="namespace",
        slug="slug",
        semver="semver",
    )


def _smoke_case_23() -> None:
    version = client.schemas.version.delete(
        namespace="namespace",
        slug="slug",
        semver="semver",
    )


def _smoke_case_24() -> None:
    version = client.schemas.version.create(
        namespace="namespace",
        slug="slug",
        version="x",
        document="",
    )


def _smoke_case_25() -> None:
    access_group = client.schemas.access_group.create(
        namespace="namespace",
        slug="slug",
        access_group_slug="xxx",
    )


def _smoke_case_26() -> None:
    access_group = client.schemas.access_group.delete(
        namespace="namespace",
        slug="slug",
        access_group_slug="xxx",
    )


def _smoke_case_27() -> None:
    login_portal = client.login_portals.retrieve(
        slug="slug",
    )


def _smoke_case_28() -> None:
    login_portal = client.login_portals.update(
        slug="slug",
    )


def _smoke_case_29() -> None:
    login_portal = client.login_portals.update(
        slug="slug",
        title="",
    )


def _smoke_case_30() -> None:
    login_portal = client.login_portals.delete(
        slug="slug",
    )


def _smoke_case_31() -> None:
    login_portal = client.login_portals.create(
        title="",
        slug="",
        email={
            "logo": "",
            "logo_size": "100",
            "button_text": "Login",
            "message": "Click to access private documentation hosted by scalar.com",
            "title": "Private Docs",
            "main_color": "#2a2f45",
            "main_background": "#f6f6f6",
            "card_color": "2a2f45",
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


def _smoke_case_32() -> None:
    login_portal = client.login_portals.list()


def _smoke_case_33() -> None:
    rule = client.rules.list_rulesets(
        namespace="namespace",
    )


def _smoke_case_34() -> None:
    rule = client.rules.create_ruleset(
        namespace="namespace",
        title="",
        slug="",
        document="",
    )


def _smoke_case_35() -> None:
    rule = client.rules.create_ruleset(
        namespace="namespace",
        title="",
        description="",
        slug="",
        is_private=False,
        document="",
    )


def _smoke_case_36() -> None:
    rule = client.rules.update_ruleset(
        path_namespace="namespace",
        path_slug="slug",
    )


def _smoke_case_37() -> None:
    rule = client.rules.update_ruleset(
        path_namespace="namespace",
        path_slug="slug",
        body_namespace="",
        body_slug="",
        title="",
        description="",
        is_private=False,
    )


def _smoke_case_38() -> None:
    rule = client.rules.delete_ruleset(
        namespace="namespace",
        slug="slug",
    )


def _smoke_case_39() -> None:
    rule = client.rules.retrieve_ruleset_document(
        namespace="namespace",
        slug="slug",
    )


def _smoke_case_40() -> None:
    rule = client.rules.create_ruleset_access_group(
        namespace="namespace",
        slug="slug",
        access_group_slug="xxx",
    )


def _smoke_case_41() -> None:
    rule = client.rules.delete_ruleset_access_group(
        namespace="namespace",
        slug="slug",
        access_group_slug="xxx",
    )


def _smoke_case_42() -> None:
    theme = client.themes.list()


def _smoke_case_43() -> None:
    theme = client.themes.create(
        name="",
        slug="",
        document="",
    )


def _smoke_case_44() -> None:
    theme = client.themes.create(
        name="",
        description="",
        slug="",
        document="",
    )


def _smoke_case_45() -> None:
    theme = client.themes.update(
        slug="slug",
    )


def _smoke_case_46() -> None:
    theme = client.themes.update(
        slug="slug",
        name="",
        description="",
    )


def _smoke_case_47() -> None:
    theme = client.themes.replace_document(
        slug="slug",
        document="",
    )


def _smoke_case_48() -> None:
    theme = client.themes.delete(
        slug="slug",
    )


def _smoke_case_49() -> None:
    theme = client.themes.retrieve(
        slug="slug",
    )


def _smoke_case_50() -> None:
    team = client.teams.list()


def _smoke_case_51() -> None:
    scalar_doc = client.scalar_docs.list_guides()


def _smoke_case_52() -> None:
    scalar_doc = client.scalar_docs.create_guide(
        name="",
        is_private=False,
        allowed_users=[],
        allowed_domains=[],
    )


def _smoke_case_53() -> None:
    scalar_doc = client.scalar_docs.create_guide(
        name="",
        slug="xxx",
        is_private=False,
        allowed_users=[],
        allowed_domains=[],
    )


def _smoke_case_54() -> None:
    scalar_doc = client.scalar_docs.publish_guide(
        slug="slug",
    )


def _smoke_case_55() -> None:
    namespace = client.namespaces.list()


def _smoke_case_56() -> None:
    authentication = client.authentication.exchange_personal_token(
        personal_token="",
    )


def _smoke_case_57() -> None:
    authentication = client.authentication.list_current_user()


cases: list[SmokeCase] = [
    {
        "operation": "listAllApiDocuments",
        "method": "GET",
        "path": "/v1/apis",
        "run": _smoke_case_0,
    },
    {
        "operation": "listApiDocuments",
        "method": "GET",
        "path": "/v1/apis/{namespace}",
        "run": _smoke_case_1,
    },
    {
        "operation": "createApiDocument",
        "method": "POST",
        "path": "/v1/apis/{namespace}",
        "label": "required params",
        "run": _smoke_case_2,
    },
    {
        "operation": "createApiDocument",
        "method": "POST",
        "path": "/v1/apis/{namespace}",
        "label": "all params",
        "run": _smoke_case_3,
    },
    {
        "operation": "updateApiDocument",
        "method": "PATCH",
        "path": "/v1/apis/{namespace}/{slug}",
        "label": "required params",
        "run": _smoke_case_4,
    },
    {
        "operation": "updateApiDocument",
        "method": "PATCH",
        "path": "/v1/apis/{namespace}/{slug}",
        "label": "all params",
        "run": _smoke_case_5,
    },
    {
        "operation": "deleteApiDocument",
        "method": "DELETE",
        "path": "/v1/apis/{namespace}/{slug}",
        "run": _smoke_case_6,
    },
    {
        "operation": "retrieveApiDocumentVersion",
        "method": "GET",
        "path": "/v1/apis/{namespace}/{slug}/version/{semver}",
        "run": _smoke_case_7,
    },
    {
        "operation": "updateApiDocumentVersion",
        "method": "PATCH",
        "path": "/v1/apis/{namespace}/{slug}/version/{semver}",
        "label": "required params",
        "run": _smoke_case_8,
    },
    {
        "operation": "updateApiDocumentVersion",
        "method": "PATCH",
        "path": "/v1/apis/{namespace}/{slug}/version/{semver}",
        "label": "all params",
        "run": _smoke_case_9,
    },
    {
        "operation": "deleteApiDocumentVersion",
        "method": "DELETE",
        "path": "/v1/apis/{namespace}/{slug}/version/{semver}",
        "run": _smoke_case_10,
    },
    {
        "operation": "listApiDocumentVersionMetadata",
        "method": "GET",
        "path": "/v1/apis/{namespace}/{slug}/version/{semver}/metadata",
        "run": _smoke_case_11,
    },
    {
        "operation": "createApiDocumentVersion",
        "method": "POST",
        "path": "/v1/apis/{namespace}/{slug}/version",
        "label": "required params",
        "run": _smoke_case_12,
    },
    {
        "operation": "createApiDocumentVersion",
        "method": "POST",
        "path": "/v1/apis/{namespace}/{slug}/version",
        "label": "all params",
        "run": _smoke_case_13,
    },
    {
        "operation": "createApiDocumentAccessGroup",
        "method": "POST",
        "path": "/v1/apis/{namespace}/{slug}/access-group",
        "run": _smoke_case_14,
    },
    {
        "operation": "deleteApiDocumentAccessGroup",
        "method": "DELETE",
        "path": "/v1/apis/{namespace}/{slug}/access-group",
        "run": _smoke_case_15,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/schemas/{namespace}",
        "run": _smoke_case_16,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/schemas/{namespace}",
        "label": "required params",
        "run": _smoke_case_17,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/schemas/{namespace}",
        "label": "all params",
        "run": _smoke_case_18,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/schemas/{namespace}/{slug}",
        "label": "required params",
        "run": _smoke_case_19,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/schemas/{namespace}/{slug}",
        "label": "all params",
        "run": _smoke_case_20,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/schemas/{namespace}/{slug}",
        "run": _smoke_case_21,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/schemas/{namespace}/{slug}/version/{semver}",
        "run": _smoke_case_22,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/schemas/{namespace}/{slug}/version/{semver}",
        "run": _smoke_case_23,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/schemas/{namespace}/{slug}/version",
        "run": _smoke_case_24,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/schemas/{namespace}/{slug}/access-group",
        "run": _smoke_case_25,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/schemas/{namespace}/{slug}/access-group",
        "run": _smoke_case_26,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/login-portals/{slug}",
        "run": _smoke_case_27,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/login-portals/{slug}",
        "label": "required params",
        "run": _smoke_case_28,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/login-portals/{slug}",
        "label": "all params",
        "run": _smoke_case_29,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/login-portals/{slug}",
        "run": _smoke_case_30,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/login-portals",
        "run": _smoke_case_31,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/login-portals",
        "run": _smoke_case_32,
    },
    {
        "operation": "listRulesets",
        "method": "GET",
        "path": "/v1/rulesets/{namespace}",
        "run": _smoke_case_33,
    },
    {
        "operation": "createRuleset",
        "method": "POST",
        "path": "/v1/rulesets/{namespace}",
        "label": "required params",
        "run": _smoke_case_34,
    },
    {
        "operation": "createRuleset",
        "method": "POST",
        "path": "/v1/rulesets/{namespace}",
        "label": "all params",
        "run": _smoke_case_35,
    },
    {
        "operation": "updateRuleset",
        "method": "PATCH",
        "path": "/v1/rulesets/{namespace}/{slug}",
        "label": "required params",
        "run": _smoke_case_36,
    },
    {
        "operation": "updateRuleset",
        "method": "PATCH",
        "path": "/v1/rulesets/{namespace}/{slug}",
        "label": "all params",
        "run": _smoke_case_37,
    },
    {
        "operation": "deleteRuleset",
        "method": "DELETE",
        "path": "/v1/rulesets/{namespace}/{slug}",
        "run": _smoke_case_38,
    },
    {
        "operation": "retrieveRulesetDocument",
        "method": "GET",
        "path": "/v1/rulesets/{namespace}/{slug}",
        "run": _smoke_case_39,
    },
    {
        "operation": "createRulesetAccessGroup",
        "method": "POST",
        "path": "/v1/rulesets/{namespace}/{slug}/access-group",
        "run": _smoke_case_40,
    },
    {
        "operation": "deleteRulesetAccessGroup",
        "method": "DELETE",
        "path": "/v1/rulesets/{namespace}/{slug}/access-group",
        "run": _smoke_case_41,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/themes",
        "run": _smoke_case_42,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/themes",
        "label": "required params",
        "run": _smoke_case_43,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/themes",
        "label": "all params",
        "run": _smoke_case_44,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/themes/{slug}",
        "label": "required params",
        "run": _smoke_case_45,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/themes/{slug}",
        "label": "all params",
        "run": _smoke_case_46,
    },
    {
        "operation": "replaceDocument",
        "method": "PUT",
        "path": "/v1/themes/{slug}",
        "run": _smoke_case_47,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/themes/{slug}",
        "run": _smoke_case_48,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/themes/{slug}",
        "run": _smoke_case_49,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/teams",
        "run": _smoke_case_50,
    },
    {
        "operation": "listGuides",
        "method": "GET",
        "path": "/v1/guides",
        "run": _smoke_case_51,
    },
    {
        "operation": "createGuide",
        "method": "POST",
        "path": "/v1/guides",
        "label": "required params",
        "run": _smoke_case_52,
    },
    {
        "operation": "createGuide",
        "method": "POST",
        "path": "/v1/guides",
        "label": "all params",
        "run": _smoke_case_53,
    },
    {
        "operation": "publishGuide",
        "method": "POST",
        "path": "/v1/guides/{slug}/publish",
        "run": _smoke_case_54,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/namespaces",
        "run": _smoke_case_55,
    },
    {
        "operation": "exchangePersonalToken",
        "method": "POST",
        "path": "/v1/auth/exchange",
        "run": _smoke_case_56,
    },
    {
        "operation": "listCurrentUser",
        "method": "GET",
        "path": "/v1/auth/me",
        "run": _smoke_case_57,
    },
]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [case for case in cases if any(needle in case["operation"] or needle in case["path"] for needle in needles)]


def _smoke_concurrency(case_count: int) -> int:
    override = os.environ.get("SCALAR_SMOKE_CONCURRENCY")
    if override:
        try:
            parsed = int(override)
            if parsed > 0:
                return min(parsed, case_count)
        except ValueError:
            pass
    return min(DEFAULT_SMOKE_CONCURRENCY, case_count)


def _case_identity(case: SmokeCase) -> SmokeResult:
    # `label` is carried through only when the operation contributed both of its calls, so a
    # single-case operation reports exactly as it did before there were two.
    identity: SmokeResult = {
        "operation": case["operation"],
        "method": case["method"],
        "path": case["path"],
    }
    label = case.get("label")
    if label:
        identity["label"] = label
    return identity


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    identity = _case_identity(case)
    try:
        case["run"]()
        return {
            **identity,
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            **identity,
            "status": "failed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
            "error": traceback.format_exc(),
        }


def main() -> None:
    selected = _selected_cases()
    if selected:
        # Keep enough parallelism to catch generated SDK concurrency bugs without overwhelming
        # CI runners or the in-process mock server for large SDKs.
        with ThreadPoolExecutor(max_workers=_smoke_concurrency(len(selected))) as executor:
            results = list(executor.map(_run_case, selected))
    else:
        results = []
    failed = [result for result in results if result["status"] == "failed"]

    report_path = os.environ.get("SCALAR_SMOKE_REPORT")
    if report_path:
        Path(report_path).write_text(
            json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8"
        )
    else:
        for result in results:
            suffix = f" [{result['label']}]" if result.get("label") else ""
            if result["status"] == "passed":
                print(
                    f"PASS {result['operation']}{suffix} ({result['method']} {result['path']}) {result['durationMs']}ms"
                )
            else:
                print(
                    f"FAIL {result['operation']}{suffix} ({result['method']} {result['path']})\n{result.get('error', '')}",
                    file=sys.stderr,
                )
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
