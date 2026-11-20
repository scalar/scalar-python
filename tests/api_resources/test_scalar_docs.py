# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestScalarDocs:
    @smoke_case("scalarDocs.listGuides:single", operation="listGuides", path="/v1/guides")
    def test_method_list_guides(self) -> None:
        scalar_doc = client.scalar_docs.list_guides()

    @smoke_case("scalarDocs.createGuide:required", operation="createGuide", path="/v1/guides")
    def test_method_create_guide(self) -> None:
        scalar_doc = client.scalar_docs.create_guide(
            name="Acme Documentation",
            is_private=False,
            allowed_users=[],
            allowed_domains=[],
        )

    @smoke_case("scalarDocs.createGuide:all", operation="createGuide", path="/v1/guides")
    def test_method_create_guide_with_all_params(self) -> None:
        scalar_doc = client.scalar_docs.create_guide(
            name="Acme Documentation",
            slug="acme-docs",
            is_private=False,
            allowed_users=[],
            allowed_domains=[],
        )

    @smoke_case("scalarDocs.publishGuide:single", operation="publishGuide", path="/v1/guides/{slug}/publish")
    def test_method_publish_guide(self) -> None:
        scalar_doc = client.scalar_docs.publish_guide(
            slug="acme-docs",
        )

    @smoke_case("scalarDocs.listProjects:required", operation="listProjects", path="/v1/docs")
    def test_method_list_projects(self) -> None:
        scalar_doc = client.scalar_docs.list_projects()

    @smoke_case("scalarDocs.listProjects:all", operation="listProjects", path="/v1/docs")
    def test_method_list_projects_with_all_params(self) -> None:
        scalar_doc = client.scalar_docs.list_projects(
            limit=20,
        )

    @smoke_case("scalarDocs.createProject:required", operation="createProject", path="/v1/docs")
    def test_method_create_project(self) -> None:
        scalar_doc = client.scalar_docs.create_project(
            name="Acme Documentation",
            provider="forgejo",
        )

    @smoke_case("scalarDocs.createProject:all", operation="createProject", path="/v1/docs")
    def test_method_create_project_with_all_params(self) -> None:
        scalar_doc = client.scalar_docs.create_project(
            name="Acme Documentation",
            slug="acme-docs",
            is_private=False,
            blank=True,
            provider="forgejo",
            github_repository={"installation_id": 84, "repo_id": 123456789},
            bitbucket_repository={
                "workspace_uuid": "{12345678-1234-4234-8234-123456789abc}",
                "repo_uuid": "{abcdef01-1234-4234-8234-123456789abc}",
            },
        )

    @smoke_case("scalarDocs.retrieveProject:single", operation="retrieveProject", path="/v1/docs/{slug}")
    def test_method_retrieve_project(self) -> None:
        scalar_doc = client.scalar_docs.retrieve_project(
            slug="acme-docs",
        )

    @smoke_case("scalarDocs.updateProject:required", operation="updateProject", path="/v1/docs/{slug}")
    def test_method_update_project(self) -> None:
        scalar_doc = client.scalar_docs.update_project(
            slug="acme-docs",
        )

    @smoke_case("scalarDocs.updateProject:all", operation="updateProject", path="/v1/docs/{slug}")
    def test_method_update_project_with_all_params(self) -> None:
        scalar_doc = client.scalar_docs.update_project(
            slug="acme-docs",
            name="Acme Documentation",
            is_private=False,
            access_groups=["UakgbKJ5m9gl0JDMbcJqL"],
            login_portal_uid="LakgbKJ5m9gl0JDMbcJqL",
            active_theme_id="TakgbKJ5m9gl0JDMbcJqL",
            agent_enabled=True,
            analytics_enabled=True,
        )

    @smoke_case("scalarDocs.deleteProject:single", operation="deleteProject", path="/v1/docs/{slug}")
    def test_method_delete_project(self) -> None:
        scalar_doc = client.scalar_docs.delete_project(
            slug="acme-docs",
        )

    @smoke_case("scalarDocs.publishProject:required", operation="publishProject", path="/v1/docs/{slug}/publish")
    def test_method_publish_project(self) -> None:
        scalar_doc = client.scalar_docs.publish_project(
            slug="acme-docs",
        )

    @smoke_case("scalarDocs.publishProject:all", operation="publishProject", path="/v1/docs/{slug}/publish")
    def test_method_publish_project_with_all_params(self) -> None:
        scalar_doc = client.scalar_docs.publish_project(
            slug="acme-docs",
            commit_sha="0123456789abcdef0123456789abcdef01234567",
            preview=False,
            config_path="scalar.config.json",
        )

    @smoke_case("scalarDocs.listProjectConfig:required", operation="listProjectConfig", path="/v1/docs/{slug}/config")
    def test_method_list_project_config(self) -> None:
        scalar_doc = client.scalar_docs.list_project_config(
            slug="acme-docs",
        )

    @smoke_case("scalarDocs.listProjectConfig:all", operation="listProjectConfig", path="/v1/docs/{slug}/config")
    def test_method_list_project_config_with_all_params(self) -> None:
        scalar_doc = client.scalar_docs.list_project_config(
            slug="acme-docs",
            ref="main",
        )

    @smoke_case(
        "scalarDocs.updateProjectConfig:required", operation="updateProjectConfig", path="/v1/docs/{slug}/config"
    )
    def test_method_update_project_config(self) -> None:
        scalar_doc = client.scalar_docs.update_project_config(
            slug="acme-docs",
            content='{"name":"Acme Documentation"}',
        )

    @smoke_case("scalarDocs.updateProjectConfig:all", operation="updateProjectConfig", path="/v1/docs/{slug}/config")
    def test_method_update_project_config_with_all_params(self) -> None:
        scalar_doc = client.scalar_docs.update_project_config(
            slug="acme-docs",
            content='{"name":"Acme Documentation"}',
            ref="main",
            base_token="example-edit-token",
            message="Update documentation configuration",
            path="scalar.config.json",
        )

    @smoke_case("scalarDocs.listProjectDomain:single", operation="listProjectDomain", path="/v1/docs/{slug}/domain")
    def test_method_list_project_domain(self) -> None:
        scalar_doc = client.scalar_docs.list_project_domain(
            slug="acme-docs",
        )

    @smoke_case(
        "scalarDocs.listProjectDomainStatus:single",
        operation="listProjectDomainStatus",
        path="/v1/docs/{slug}/domain/status",
    )
    def test_method_list_project_domain_status(self) -> None:
        scalar_doc = client.scalar_docs.list_project_domain_status(
            slug="acme-docs",
        )
