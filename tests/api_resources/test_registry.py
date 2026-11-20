# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestRegistry:
    @smoke_case("registry.listAllApiDocuments:single", operation="listAllApiDocuments", path="/v1/apis")
    def test_method_list_all_api_documents(self) -> None:
        registry = client.registry.list_all_api_documents()

    @smoke_case("registry.listApiDocuments:single", operation="listApiDocuments", path="/v1/apis/{namespace}")
    def test_method_list_api_documents(self) -> None:
        registry = client.registry.list_api_documents(
            namespace="acme",
        )

    @smoke_case("registry.createApiDocument:required", operation="createApiDocument", path="/v1/apis/{namespace}")
    def test_method_create_api_document(self) -> None:
        registry = client.registry.create_api_document(
            namespace="acme",
            title="Acme API",
            version="1.2.0",
            slug="acme-api",
            document='{"openapi":"3.1.0","info":{"title":"Acme API","version":"1.2.0"},"paths":{}}',
        )

    @smoke_case("registry.createApiDocument:all", operation="createApiDocument", path="/v1/apis/{namespace}")
    def test_method_create_api_document_with_all_params(self) -> None:
        registry = client.registry.create_api_document(
            namespace="acme",
            title="Acme API",
            description="API for managing Acme products and orders.",
            version="1.2.0",
            slug="acme-api",
            ruleset='extends: ["spectral:oas"]',
            is_private=False,
            document='{"openapi":"3.1.0","info":{"title":"Acme API","version":"1.2.0"},"paths":{}}',
        )

    @smoke_case(
        "registry.updateApiDocument:required", operation="updateApiDocument", path="/v1/apis/{namespace}/{slug}"
    )
    def test_method_update_api_document(self) -> None:
        registry = client.registry.update_api_document(
            namespace="acme",
            slug="acme-api",
        )

    @smoke_case("registry.updateApiDocument:all", operation="updateApiDocument", path="/v1/apis/{namespace}/{slug}")
    def test_method_update_api_document_with_all_params(self) -> None:
        registry = client.registry.update_api_document(
            namespace="acme",
            slug="acme-api",
            title="Acme API",
            description="API for managing Acme products and orders.",
            is_private=False,
            ruleset='extends: ["spectral:oas"]',
        )

    @smoke_case("registry.deleteApiDocument:single", operation="deleteApiDocument", path="/v1/apis/{namespace}/{slug}")
    def test_method_delete_api_document(self) -> None:
        registry = client.registry.delete_api_document(
            namespace="acme",
            slug="acme-api",
        )

    @smoke_case(
        "registry.retrieveApiDocumentVersion:single",
        operation="retrieveApiDocumentVersion",
        path="/v1/apis/{namespace}/{slug}/version/{semver}",
    )
    def test_method_retrieve_api_document_version(self) -> None:
        registry = client.registry.retrieve_api_document_version(
            namespace="acme",
            slug="acme-api",
            semver="1.2.0",
        )

    @smoke_case(
        "registry.updateApiDocumentVersion:single",
        operation="updateApiDocumentVersion",
        path="/v1/apis/{namespace}/{slug}/version/{semver}",
    )
    def test_method_update_api_document_version(self) -> None:
        registry = client.registry.update_api_document_version(
            namespace="acme",
            slug="acme-api",
            semver="1.2.0",
            document='{"openapi":"3.1.0","info":{"title":"Acme API","version":"1.2.0"},"paths":{}}',
        )

    @smoke_case(
        "registry.deleteApiDocumentVersion:single",
        operation="deleteApiDocumentVersion",
        path="/v1/apis/{namespace}/{slug}/version/{semver}",
    )
    def test_method_delete_api_document_version(self) -> None:
        registry = client.registry.delete_api_document_version(
            namespace="acme",
            slug="acme-api",
            semver="1.2.0",
        )

    @smoke_case(
        "registry.listApiDocumentVersionMetadata:single",
        operation="listApiDocumentVersionMetadata",
        path="/v1/apis/{namespace}/{slug}/version/{semver}/metadata",
    )
    def test_method_list_api_document_version_metadata(self) -> None:
        registry = client.registry.list_api_document_version_metadata(
            namespace="acme",
            slug="acme-api",
            semver="1.2.0",
        )

    @smoke_case(
        "registry.createApiDocumentVersion:required",
        operation="createApiDocumentVersion",
        path="/v1/apis/{namespace}/{slug}/version",
    )
    def test_method_create_api_document_version(self) -> None:
        registry = client.registry.create_api_document_version(
            namespace="acme",
            slug="acme-api",
            version="1.2.0",
            document='{"openapi":"3.1.0","info":{"title":"Acme API","version":"1.2.0"},"paths":{}}',
        )

    @smoke_case(
        "registry.createApiDocumentVersion:all",
        operation="createApiDocumentVersion",
        path="/v1/apis/{namespace}/{slug}/version",
    )
    def test_method_create_api_document_version_with_all_params(self) -> None:
        registry = client.registry.create_api_document_version(
            namespace="acme",
            slug="acme-api",
            version="1.2.0",
            document='{"openapi":"3.1.0","info":{"title":"Acme API","version":"1.2.0"},"paths":{}}',
            force=False,
        )

    @smoke_case(
        "registry.createApiDocumentAccessGroup:single",
        operation="createApiDocumentAccessGroup",
        path="/v1/apis/{namespace}/{slug}/access-group",
    )
    def test_method_create_api_document_access_group(self) -> None:
        registry = client.registry.create_api_document_access_group(
            namespace="acme",
            slug="acme-api",
            access_group_slug="acme-api",
        )

    @smoke_case(
        "registry.deleteApiDocumentAccessGroup:single",
        operation="deleteApiDocumentAccessGroup",
        path="/v1/apis/{namespace}/{slug}/access-group",
    )
    def test_method_delete_api_document_access_group(self) -> None:
        registry = client.registry.delete_api_document_access_group(
            namespace="acme",
            slug="acme-api",
            access_group_slug="acme-api",
        )
