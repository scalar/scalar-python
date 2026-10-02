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
client = Scalar(max_retries=2, timeout=10)


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
    registry = client.registry.delete_api_document_version(
        namespace="namespace",
        slug="slug",
        semver="semver",
    )


def _smoke_case_10() -> None:
    registry = client.registry.list_api_document_version_metadata(
        namespace="namespace",
        slug="slug",
        semver="semver",
    )


def _smoke_case_11() -> None:
    registry = client.registry.create_api_document_version(
        namespace="namespace",
        slug="slug",
        version="x",
        document="",
    )


def _smoke_case_12() -> None:
    registry = client.registry.create_api_document_version(
        namespace="namespace",
        slug="slug",
        version="x",
        document="",
        force=False,
    )


def _smoke_case_13() -> None:
    registry = client.registry.create_api_document_access_group(
        namespace="namespace",
        slug="slug",
        access_group_slug="x",
    )


def _smoke_case_14() -> None:
    registry = client.registry.delete_api_document_access_group(
        namespace="namespace",
        slug="slug",
        access_group_slug="x",
    )


def _smoke_case_15() -> None:
    schema = client.schemas.list(
        namespace="namespace",
    )


def _smoke_case_16() -> None:
    schema = client.schemas.create(
        namespace="namespace",
        title="",
        version="x",
        slug="",
        document="",
    )


def _smoke_case_17() -> None:
    schema = client.schemas.create(
        namespace="namespace",
        title="",
        description="",
        version="x",
        slug="",
        is_private=False,
        document="",
    )


def _smoke_case_18() -> None:
    schema = client.schemas.update(
        namespace="namespace",
        slug="slug",
    )


def _smoke_case_19() -> None:
    schema = client.schemas.update(
        namespace="namespace",
        slug="slug",
        title="",
        description="",
        is_private=False,
    )


def _smoke_case_20() -> None:
    schema = client.schemas.delete(
        namespace="namespace",
        slug="slug",
    )


def _smoke_case_21() -> None:
    version = client.schemas.version.retrieve(
        namespace="namespace",
        slug="slug",
        semver="semver",
    )


def _smoke_case_22() -> None:
    version = client.schemas.version.delete(
        namespace="namespace",
        slug="slug",
        semver="semver",
    )


def _smoke_case_23() -> None:
    version = client.schemas.version.create(
        namespace="namespace",
        slug="slug",
        version="x",
        document="",
    )


def _smoke_case_24() -> None:
    version = client.schemas.version.create(
        namespace="namespace",
        slug="slug",
        version="x",
        document="",
        force=False,
    )


def _smoke_case_25() -> None:
    access_group = client.schemas.access_group.create(
        namespace="namespace",
        slug="slug",
        access_group_slug="x",
    )


def _smoke_case_26() -> None:
    access_group = client.schemas.access_group.delete(
        namespace="namespace",
        slug="slug",
        access_group_slug="x",
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


def _smoke_case_32() -> None:
    login_portal = client.login_portals.list()


def _smoke_case_33() -> None:
    access_group = client.access_groups.create()


def _smoke_case_34() -> None:
    access_group = client.access_groups.create(
        name="",
        slug="x",
        allowed_domains={},
    )


def _smoke_case_35() -> None:
    access_group = client.access_groups.retrieve(
        slug="slug",
    )


def _smoke_case_36() -> None:
    access_group = client.access_groups.update(
        path_slug="slug",
    )


def _smoke_case_37() -> None:
    access_group = client.access_groups.update(
        path_slug="slug",
        name="",
        body_slug="x",
    )


def _smoke_case_38() -> None:
    access_group = client.access_groups.delete(
        slug="slug",
    )


def _smoke_case_39() -> None:
    domain = client.access_groups.domains.create(
        slug="slug",
        domain="",
    )


def _smoke_case_40() -> None:
    domain = client.access_groups.domains.delete(
        slug="slug",
        domain="",
    )


def _smoke_case_41() -> None:
    rule = client.rules.list_rulesets(
        namespace="namespace",
    )


def _smoke_case_42() -> None:
    rule = client.rules.create_ruleset(
        namespace="namespace",
        title="",
        slug="",
        document="",
    )


def _smoke_case_43() -> None:
    rule = client.rules.create_ruleset(
        namespace="namespace",
        title="",
        description="",
        slug="",
        is_private=False,
        document="",
    )


def _smoke_case_44() -> None:
    rule = client.rules.update_ruleset(
        path_namespace="namespace",
        path_slug="slug",
    )


def _smoke_case_45() -> None:
    rule = client.rules.update_ruleset(
        path_namespace="namespace",
        path_slug="slug",
        body_namespace="",
        body_slug="",
        title="",
        description="",
        is_private=False,
    )


def _smoke_case_46() -> None:
    rule = client.rules.delete_ruleset(
        namespace="namespace",
        slug="slug",
    )


def _smoke_case_47() -> None:
    rule = client.rules.retrieve_ruleset_document(
        namespace="namespace",
        slug="slug",
    )


def _smoke_case_48() -> None:
    rule = client.rules.create_ruleset_access_group(
        namespace="namespace",
        slug="slug",
        access_group_slug="x",
    )


def _smoke_case_49() -> None:
    rule = client.rules.delete_ruleset_access_group(
        namespace="namespace",
        slug="slug",
        access_group_slug="x",
    )


def _smoke_case_50() -> None:
    theme = client.themes.list()


def _smoke_case_51() -> None:
    theme = client.themes.create(
        name="",
        slug="",
        document="",
    )


def _smoke_case_52() -> None:
    theme = client.themes.create(
        name="",
        description="",
        slug="",
        document="",
    )


def _smoke_case_53() -> None:
    theme = client.themes.update(
        slug="slug",
    )


def _smoke_case_54() -> None:
    theme = client.themes.update(
        slug="slug",
        name="",
        description="",
    )


def _smoke_case_55() -> None:
    theme = client.themes.replace_document(
        slug="slug",
        document="",
    )


def _smoke_case_56() -> None:
    theme = client.themes.delete(
        slug="slug",
    )


def _smoke_case_57() -> None:
    theme = client.themes.retrieve(
        slug="slug",
    )


def _smoke_case_58() -> None:
    team = client.teams.list()


def _smoke_case_59() -> None:
    member = client.teams.members.list()


def _smoke_case_60() -> None:
    member = client.teams.members.update(
        uid="uidxx",
        role="owner",
    )


def _smoke_case_61() -> None:
    member = client.teams.members.delete(
        uid="uidxx",
    )


def _smoke_case_62() -> None:
    invite = client.teams.invites.member(
        email="user@example.com",
        role="owner",
    )


def _smoke_case_63() -> None:
    invite = client.teams.invites.resend(
        uid="uidxx",
    )


def _smoke_case_64() -> None:
    invite = client.teams.invites.cancel(
        uid="uidxx",
    )


def _smoke_case_65() -> None:
    scalar_doc = client.scalar_docs.list_guides()


def _smoke_case_66() -> None:
    scalar_doc = client.scalar_docs.create_guide(
        name="",
        is_private=False,
        allowed_users=[],
        allowed_domains=[],
    )


def _smoke_case_67() -> None:
    scalar_doc = client.scalar_docs.create_guide(
        name="",
        slug="x",
        is_private=False,
        allowed_users=[],
        allowed_domains=[],
    )


def _smoke_case_68() -> None:
    scalar_doc = client.scalar_docs.publish_guide(
        slug="slug",
    )


def _smoke_case_69() -> None:
    scalar_doc = client.scalar_docs.list_projects()


def _smoke_case_70() -> None:
    scalar_doc = client.scalar_docs.list_projects(
        limit=1,
    )


def _smoke_case_71() -> None:
    scalar_doc = client.scalar_docs.create_project(
        name="",
        provider="forgejo",
    )


def _smoke_case_72() -> None:
    scalar_doc = client.scalar_docs.create_project(
        name="",
        slug="x",
        is_private=False,
        blank=False,
        provider="forgejo",
        github_repository={"installation_id": 0, "repo_id": 0},
        bitbucket_repository={"workspace_uuid": "", "repo_uuid": ""},
    )


def _smoke_case_73() -> None:
    scalar_doc = client.scalar_docs.retrieve_project(
        slug="slug",
    )


def _smoke_case_74() -> None:
    scalar_doc = client.scalar_docs.update_project(
        slug="slug",
    )


def _smoke_case_75() -> None:
    scalar_doc = client.scalar_docs.update_project(
        slug="slug",
        name="",
        is_private=False,
        access_groups=["xxxxx"],
        login_portal_uid="xxxxx",
        active_theme_id="xxxxx",
        agent_enabled=False,
        analytics_enabled=False,
    )


def _smoke_case_76() -> None:
    scalar_doc = client.scalar_docs.delete_project(
        slug="slug",
    )


def _smoke_case_77() -> None:
    scalar_doc = client.scalar_docs.publish_project(
        slug="slug",
    )


def _smoke_case_78() -> None:
    scalar_doc = client.scalar_docs.publish_project(
        slug="slug",
        commit_sha="",
        preview=False,
        config_path="",
    )


def _smoke_case_79() -> None:
    scalar_doc = client.scalar_docs.list_project_config(
        slug="slug",
    )


def _smoke_case_80() -> None:
    scalar_doc = client.scalar_docs.list_project_config(
        slug="slug",
        ref="ref",
    )


def _smoke_case_81() -> None:
    scalar_doc = client.scalar_docs.update_project_config(
        slug="slug",
        content="",
    )


def _smoke_case_82() -> None:
    scalar_doc = client.scalar_docs.update_project_config(
        slug="slug",
        content="",
        ref="",
        base_token="",
        message="",
        path="",
    )


def _smoke_case_83() -> None:
    scalar_doc = client.scalar_docs.list_project_domain(
        slug="slug",
    )


def _smoke_case_84() -> None:
    scalar_doc = client.scalar_docs.list_project_domain_status(
        slug="slug",
    )


def _smoke_case_85() -> None:
    namespace = client.namespaces.list()


def _smoke_case_86() -> None:
    authentication = client.authentication.exchange_personal_token(
        personal_token="",
    )


def _smoke_case_87() -> None:
    authentication = client.authentication.list_current_user()


def _smoke_case_88() -> None:
    sdk = client.sdks.list()


def _smoke_case_89() -> None:
    sdk = client.sdks.list(
        limit=1,
    )


def _smoke_case_90() -> None:
    sdk = client.sdks.create(
        api_uid="xxxxx",
        languages=["typescript"],
    )


def _smoke_case_91() -> None:
    sdk = client.sdks.create(
        api_uid="xxxxx",
        languages=["typescript"],
        title="",
        slug="x",
        class_name="",
        config="",
    )


def _smoke_case_92() -> None:
    sdk = client.sdks.retrieve(
        uid="uidxx",
    )


def _smoke_case_93() -> None:
    sdk = client.sdks.update(
        uid="uidxx",
    )


def _smoke_case_94() -> None:
    sdk = client.sdks.update(
        uid="uidxx",
        title="",
        slug="x",
        is_private=False,
        config="",
        api_uid="xxxxx",
        api_version="",
    )


def _smoke_case_95() -> None:
    sdk = client.sdks.delete(
        uid="uidxx",
    )


def _smoke_case_96() -> None:
    sdk = client.sdks.build(
        uid="uidxx",
    )


def _smoke_case_97() -> None:
    sdk = client.sdks.build(
        uid="uidxx",
        version="",
        languages=["typescript"],
    )


def _smoke_case_98() -> None:
    version = client.sdks.versions.create(
        uid="uidxx",
        version="",
        api_version="",
    )


def _smoke_case_99() -> None:
    version = client.sdks.versions.delete(
        uid="uidxx",
        version="version",
    )


def _smoke_case_100() -> None:
    repository = client.sdks.repositories.link(
        uid="uidxx",
        language="typescript",
        repository_id=0,
        base_branch="",
    )


def _smoke_case_101() -> None:
    repository = client.sdks.repositories.link(
        uid="uidxx",
        language="typescript",
        repository_id=0,
        base_branch="",
        prerelease_type="",
    )


def _smoke_case_102() -> None:
    repository = client.sdks.repositories.unlink(
        uid="uidxx",
        language="typescript",
    )


def _smoke_case_103() -> None:
    repository = client.sdks.repositories.update_publishing(
        uid="uidxx",
        language="typescript",
        publish_on_merge=False,
    )


def _smoke_case_104() -> None:
    repository = client.sdks.repositories.update_publishing(
        uid="uidxx",
        language="typescript",
        publish_on_merge=False,
        auth_method="oidc",
        access="public",
        tag="",
    )


def _smoke_case_105() -> None:
    server = client.mcp.servers.list()


def _smoke_case_106() -> None:
    server = client.mcp.servers.create(
        name="x",
    )


def _smoke_case_107() -> None:
    server = client.mcp.servers.create(
        name="x",
        slug="x",
        version_uids=[""],
        project_uids=[""],
    )


def _smoke_case_108() -> None:
    server = client.mcp.servers.retrieve(
        id="id",
    )


def _smoke_case_109() -> None:
    server = client.mcp.servers.update(
        id="id",
    )


def _smoke_case_110() -> None:
    server = client.mcp.servers.update(
        id="id",
        name="x",
        slug="x",
        auto_add_operations=False,
        operations=[""],
        docs_pages=[""],
    )


def _smoke_case_111() -> None:
    server = client.mcp.servers.delete(
        id="id",
    )


def _smoke_case_112() -> None:
    installation = client.mcp.servers.installations.list(
        id="id",
    )


def _smoke_case_113() -> None:
    installation = client.mcp.servers.installations.create(
        id="id",
        name="x",
        document_auth={},
    )


def _smoke_case_114() -> None:
    installation = client.mcp.servers.installations.create(
        id="id",
        name="x",
        slug="x",
        document_auth={},
    )


def _smoke_case_115() -> None:
    installation = client.mcp.servers.installations.retrieve(
        id="id",
        installation_id="installationId",
    )


def _smoke_case_116() -> None:
    installation = client.mcp.servers.installations.update(
        id="id",
        installation_id="installationId",
    )


def _smoke_case_117() -> None:
    installation = client.mcp.servers.installations.update(
        id="id",
        installation_id="installationId",
        name="x",
        slug="x",
        is_private=False,
        login_portal_uid="",
        document_auth={},
        mcp_version="",
    )


def _smoke_case_118() -> None:
    installation = client.mcp.servers.installations.delete(
        id="id",
        installation_id="installationId",
    )


def _smoke_case_119() -> None:
    installation = client.mcp.servers.installations.create_access_group(
        id="id",
        installation_id="installationId",
        access_group_uid="xxxxx",
    )


def _smoke_case_120() -> None:
    installation = client.mcp.servers.installations.delete_access_group(
        id="id",
        installation_id="installationId",
        access_group_uid="xxxxx",
    )


def _smoke_case_121() -> None:
    o_auth = client.o_auth.oauth_authorize()


def _smoke_case_122() -> None:
    o_auth = client.o_auth.oauth_token(
        grant_type="",
    )


def _smoke_case_123() -> None:
    o_auth = client.o_auth.oauth_token(
        grant_type="",
        client_id="",
        client_secret="",
        code="",
        redirect_uri="",
        code_verifier="",
        refresh_token="",
        scope="",
    )


def _smoke_case_124() -> None:
    o_auth = client.o_auth.oauth_revoke(
        token="",
    )


def _smoke_case_125() -> None:
    o_auth = client.o_auth.oauth_revoke(
        token="",
        token_type_hint="",
        client_id="",
        client_secret="",
    )


def _smoke_case_126() -> None:
    o_auth = client.o_auth.oauth_authorization_server_metadata()


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
        "run": _smoke_case_8,
    },
    {
        "operation": "deleteApiDocumentVersion",
        "method": "DELETE",
        "path": "/v1/apis/{namespace}/{slug}/version/{semver}",
        "run": _smoke_case_9,
    },
    {
        "operation": "listApiDocumentVersionMetadata",
        "method": "GET",
        "path": "/v1/apis/{namespace}/{slug}/version/{semver}/metadata",
        "run": _smoke_case_10,
    },
    {
        "operation": "createApiDocumentVersion",
        "method": "POST",
        "path": "/v1/apis/{namespace}/{slug}/version",
        "label": "required params",
        "run": _smoke_case_11,
    },
    {
        "operation": "createApiDocumentVersion",
        "method": "POST",
        "path": "/v1/apis/{namespace}/{slug}/version",
        "label": "all params",
        "run": _smoke_case_12,
    },
    {
        "operation": "createApiDocumentAccessGroup",
        "method": "POST",
        "path": "/v1/apis/{namespace}/{slug}/access-group",
        "run": _smoke_case_13,
    },
    {
        "operation": "deleteApiDocumentAccessGroup",
        "method": "DELETE",
        "path": "/v1/apis/{namespace}/{slug}/access-group",
        "run": _smoke_case_14,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/schemas/{namespace}",
        "run": _smoke_case_15,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/schemas/{namespace}",
        "label": "required params",
        "run": _smoke_case_16,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/schemas/{namespace}",
        "label": "all params",
        "run": _smoke_case_17,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/schemas/{namespace}/{slug}",
        "label": "required params",
        "run": _smoke_case_18,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/schemas/{namespace}/{slug}",
        "label": "all params",
        "run": _smoke_case_19,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/schemas/{namespace}/{slug}",
        "run": _smoke_case_20,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/schemas/{namespace}/{slug}/version/{semver}",
        "run": _smoke_case_21,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/schemas/{namespace}/{slug}/version/{semver}",
        "run": _smoke_case_22,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/schemas/{namespace}/{slug}/version",
        "label": "required params",
        "run": _smoke_case_23,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/schemas/{namespace}/{slug}/version",
        "label": "all params",
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
        "operation": "create",
        "method": "POST",
        "path": "/v1/access-groups",
        "label": "required params",
        "run": _smoke_case_33,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/access-groups",
        "label": "all params",
        "run": _smoke_case_34,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/access-groups/{slug}",
        "run": _smoke_case_35,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/access-groups/{slug}",
        "label": "required params",
        "run": _smoke_case_36,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/access-groups/{slug}",
        "label": "all params",
        "run": _smoke_case_37,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/access-groups/{slug}",
        "run": _smoke_case_38,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/access-groups/{slug}/domains",
        "run": _smoke_case_39,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/access-groups/{slug}/domains",
        "run": _smoke_case_40,
    },
    {
        "operation": "listRulesets",
        "method": "GET",
        "path": "/v1/rulesets/{namespace}",
        "run": _smoke_case_41,
    },
    {
        "operation": "createRuleset",
        "method": "POST",
        "path": "/v1/rulesets/{namespace}",
        "label": "required params",
        "run": _smoke_case_42,
    },
    {
        "operation": "createRuleset",
        "method": "POST",
        "path": "/v1/rulesets/{namespace}",
        "label": "all params",
        "run": _smoke_case_43,
    },
    {
        "operation": "updateRuleset",
        "method": "PATCH",
        "path": "/v1/rulesets/{namespace}/{slug}",
        "label": "required params",
        "run": _smoke_case_44,
    },
    {
        "operation": "updateRuleset",
        "method": "PATCH",
        "path": "/v1/rulesets/{namespace}/{slug}",
        "label": "all params",
        "run": _smoke_case_45,
    },
    {
        "operation": "deleteRuleset",
        "method": "DELETE",
        "path": "/v1/rulesets/{namespace}/{slug}",
        "run": _smoke_case_46,
    },
    {
        "operation": "retrieveRulesetDocument",
        "method": "GET",
        "path": "/v1/rulesets/{namespace}/{slug}",
        "run": _smoke_case_47,
    },
    {
        "operation": "createRulesetAccessGroup",
        "method": "POST",
        "path": "/v1/rulesets/{namespace}/{slug}/access-group",
        "run": _smoke_case_48,
    },
    {
        "operation": "deleteRulesetAccessGroup",
        "method": "DELETE",
        "path": "/v1/rulesets/{namespace}/{slug}/access-group",
        "run": _smoke_case_49,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/themes",
        "run": _smoke_case_50,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/themes",
        "label": "required params",
        "run": _smoke_case_51,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/themes",
        "label": "all params",
        "run": _smoke_case_52,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/themes/{slug}",
        "label": "required params",
        "run": _smoke_case_53,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/themes/{slug}",
        "label": "all params",
        "run": _smoke_case_54,
    },
    {
        "operation": "replaceDocument",
        "method": "PUT",
        "path": "/v1/themes/{slug}",
        "run": _smoke_case_55,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/themes/{slug}",
        "run": _smoke_case_56,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/themes/{slug}",
        "run": _smoke_case_57,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/teams",
        "run": _smoke_case_58,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/teams/members",
        "run": _smoke_case_59,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/teams/members/{uid}",
        "run": _smoke_case_60,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/teams/members/{uid}",
        "run": _smoke_case_61,
    },
    {
        "operation": "member",
        "method": "POST",
        "path": "/v1/teams/invites",
        "run": _smoke_case_62,
    },
    {
        "operation": "resend",
        "method": "PATCH",
        "path": "/v1/teams/invites/{uid}",
        "run": _smoke_case_63,
    },
    {
        "operation": "cancel",
        "method": "DELETE",
        "path": "/v1/teams/invites/{uid}",
        "run": _smoke_case_64,
    },
    {
        "operation": "listGuides",
        "method": "GET",
        "path": "/v1/guides",
        "run": _smoke_case_65,
    },
    {
        "operation": "createGuide",
        "method": "POST",
        "path": "/v1/guides",
        "label": "required params",
        "run": _smoke_case_66,
    },
    {
        "operation": "createGuide",
        "method": "POST",
        "path": "/v1/guides",
        "label": "all params",
        "run": _smoke_case_67,
    },
    {
        "operation": "publishGuide",
        "method": "POST",
        "path": "/v1/guides/{slug}/publish",
        "run": _smoke_case_68,
    },
    {
        "operation": "listProjects",
        "method": "GET",
        "path": "/v1/docs",
        "label": "required params",
        "run": _smoke_case_69,
    },
    {
        "operation": "listProjects",
        "method": "GET",
        "path": "/v1/docs",
        "label": "all params",
        "run": _smoke_case_70,
    },
    {
        "operation": "createProject",
        "method": "POST",
        "path": "/v1/docs",
        "label": "required params",
        "run": _smoke_case_71,
    },
    {
        "operation": "createProject",
        "method": "POST",
        "path": "/v1/docs",
        "label": "all params",
        "run": _smoke_case_72,
    },
    {
        "operation": "retrieveProject",
        "method": "GET",
        "path": "/v1/docs/{slug}",
        "run": _smoke_case_73,
    },
    {
        "operation": "updateProject",
        "method": "PATCH",
        "path": "/v1/docs/{slug}",
        "label": "required params",
        "run": _smoke_case_74,
    },
    {
        "operation": "updateProject",
        "method": "PATCH",
        "path": "/v1/docs/{slug}",
        "label": "all params",
        "run": _smoke_case_75,
    },
    {
        "operation": "deleteProject",
        "method": "DELETE",
        "path": "/v1/docs/{slug}",
        "run": _smoke_case_76,
    },
    {
        "operation": "publishProject",
        "method": "POST",
        "path": "/v1/docs/{slug}/publish",
        "label": "required params",
        "run": _smoke_case_77,
    },
    {
        "operation": "publishProject",
        "method": "POST",
        "path": "/v1/docs/{slug}/publish",
        "label": "all params",
        "run": _smoke_case_78,
    },
    {
        "operation": "listProjectConfig",
        "method": "GET",
        "path": "/v1/docs/{slug}/config",
        "label": "required params",
        "run": _smoke_case_79,
    },
    {
        "operation": "listProjectConfig",
        "method": "GET",
        "path": "/v1/docs/{slug}/config",
        "label": "all params",
        "run": _smoke_case_80,
    },
    {
        "operation": "updateProjectConfig",
        "method": "PUT",
        "path": "/v1/docs/{slug}/config",
        "label": "required params",
        "run": _smoke_case_81,
    },
    {
        "operation": "updateProjectConfig",
        "method": "PUT",
        "path": "/v1/docs/{slug}/config",
        "label": "all params",
        "run": _smoke_case_82,
    },
    {
        "operation": "listProjectDomain",
        "method": "GET",
        "path": "/v1/docs/{slug}/domain",
        "run": _smoke_case_83,
    },
    {
        "operation": "listProjectDomainStatus",
        "method": "GET",
        "path": "/v1/docs/{slug}/domain/status",
        "run": _smoke_case_84,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/namespaces",
        "run": _smoke_case_85,
    },
    {
        "operation": "exchangePersonalToken",
        "method": "POST",
        "path": "/v1/auth/exchange",
        "run": _smoke_case_86,
    },
    {
        "operation": "listCurrentUser",
        "method": "GET",
        "path": "/v1/auth/me",
        "run": _smoke_case_87,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/sdks",
        "label": "required params",
        "run": _smoke_case_88,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/sdks",
        "label": "all params",
        "run": _smoke_case_89,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/sdks",
        "label": "required params",
        "run": _smoke_case_90,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/sdks",
        "label": "all params",
        "run": _smoke_case_91,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/sdks/{uid}",
        "run": _smoke_case_92,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/sdks/{uid}",
        "label": "required params",
        "run": _smoke_case_93,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/sdks/{uid}",
        "label": "all params",
        "run": _smoke_case_94,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/sdks/{uid}",
        "run": _smoke_case_95,
    },
    {
        "operation": "build",
        "method": "POST",
        "path": "/v1/sdks/{uid}/build",
        "label": "required params",
        "run": _smoke_case_96,
    },
    {
        "operation": "build",
        "method": "POST",
        "path": "/v1/sdks/{uid}/build",
        "label": "all params",
        "run": _smoke_case_97,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/sdks/{uid}/versions",
        "run": _smoke_case_98,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/sdks/{uid}/versions/{version}",
        "run": _smoke_case_99,
    },
    {
        "operation": "link",
        "method": "POST",
        "path": "/v1/sdks/{uid}/repositories",
        "label": "required params",
        "run": _smoke_case_100,
    },
    {
        "operation": "link",
        "method": "POST",
        "path": "/v1/sdks/{uid}/repositories",
        "label": "all params",
        "run": _smoke_case_101,
    },
    {
        "operation": "unlink",
        "method": "DELETE",
        "path": "/v1/sdks/{uid}/repositories/{language}",
        "run": _smoke_case_102,
    },
    {
        "operation": "updatePublishing",
        "method": "POST",
        "path": "/v1/sdks/{uid}/repositories/{language}/publishing",
        "label": "required params",
        "run": _smoke_case_103,
    },
    {
        "operation": "updatePublishing",
        "method": "POST",
        "path": "/v1/sdks/{uid}/repositories/{language}/publishing",
        "label": "all params",
        "run": _smoke_case_104,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/mcp/servers",
        "run": _smoke_case_105,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/mcp/servers",
        "label": "required params",
        "run": _smoke_case_106,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/mcp/servers",
        "label": "all params",
        "run": _smoke_case_107,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/mcp/servers/{id}",
        "run": _smoke_case_108,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/mcp/servers/{id}",
        "label": "required params",
        "run": _smoke_case_109,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/mcp/servers/{id}",
        "label": "all params",
        "run": _smoke_case_110,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/mcp/servers/{id}",
        "run": _smoke_case_111,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/mcp/servers/{id}/installations",
        "run": _smoke_case_112,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/mcp/servers/{id}/installations",
        "label": "required params",
        "run": _smoke_case_113,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/mcp/servers/{id}/installations",
        "label": "all params",
        "run": _smoke_case_114,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/mcp/servers/{id}/installations/{installationId}",
        "run": _smoke_case_115,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/mcp/servers/{id}/installations/{installationId}",
        "label": "required params",
        "run": _smoke_case_116,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/mcp/servers/{id}/installations/{installationId}",
        "label": "all params",
        "run": _smoke_case_117,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/mcp/servers/{id}/installations/{installationId}",
        "run": _smoke_case_118,
    },
    {
        "operation": "createAccessGroup",
        "method": "POST",
        "path": "/v1/mcp/servers/{id}/installations/{installationId}/access-group",
        "run": _smoke_case_119,
    },
    {
        "operation": "deleteAccessGroup",
        "method": "DELETE",
        "path": "/v1/mcp/servers/{id}/installations/{installationId}/access-group",
        "run": _smoke_case_120,
    },
    {
        "operation": "oauthAuthorize",
        "method": "GET",
        "path": "/v1/oauth/authorize",
        "run": _smoke_case_121,
    },
    {
        "operation": "oauthToken",
        "method": "POST",
        "path": "/v1/oauth/token",
        "label": "required params",
        "run": _smoke_case_122,
    },
    {
        "operation": "oauthToken",
        "method": "POST",
        "path": "/v1/oauth/token",
        "label": "all params",
        "run": _smoke_case_123,
    },
    {
        "operation": "oauthRevoke",
        "method": "POST",
        "path": "/v1/oauth/revoke",
        "label": "required params",
        "run": _smoke_case_124,
    },
    {
        "operation": "oauthRevoke",
        "method": "POST",
        "path": "/v1/oauth/revoke",
        "label": "all params",
        "run": _smoke_case_125,
    },
    {
        "operation": "oauthAuthorizationServerMetadata",
        "method": "GET",
        "path": "/.well-known/oauth-authorization-server",
        "run": _smoke_case_126,
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
