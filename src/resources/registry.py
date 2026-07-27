# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.registry_list_all_api_documents_response import RegistryListAllAPIDocumentsResponse
from ..types.registry_list_api_documents_response import RegistryListAPIDocumentsResponse
from ..types.registry_create_api_document_response import RegistryCreateAPIDocumentResponse
from ..types.version import Version
from ..types import registry_create_api_document_params, registry_update_api_document_params, registry_update_api_document_version_params, registry_create_api_document_version_params, registry_create_api_document_access_group_params, registry_delete_api_document_access_group_params
from ..types.registry_update_api_document_response import RegistryUpdateAPIDocumentResponse
from ..types.registry_delete_api_document_response import RegistryDeleteAPIDocumentResponse
from ..types.registry_update_api_document_version_response import RegistryUpdateAPIDocumentVersionResponse
from ..types.registry_delete_api_document_version_response import RegistryDeleteAPIDocumentVersionResponse
from ..types.registry_list_api_document_version_metadata_response import RegistryListAPIDocumentVersionMetadataResponse
from ..types.registry_create_api_document_version_response import RegistryCreateAPIDocumentVersionResponse
from ..types.registry_create_api_document_access_group_response import RegistryCreateAPIDocumentAccessGroupResponse
from ..types.slug import Slug
from ..types.registry_delete_api_document_access_group_response import RegistryDeleteAPIDocumentAccessGroupResponse

__all__ = ["RegistryResource", "AsyncRegistryResource"]


class RegistryResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> RegistryResourceWithRawResponse:
        return RegistryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegistryResourceWithStreamingResponse:
        return RegistryResourceWithStreamingResponse(self)

    def list_all_api_documents(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryListAllAPIDocumentsResponse:
        """
        List all API documents across every namespace the caller can access.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryListAllAPIDocumentsResponse: Default Response
        
        Example:
            ```python
            registry = client.registry.list_all_api_documents()
            ```
        """
        return self._get(
            "/v1/apis",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListAllAPIDocumentsResponse,
        )

    def list_api_documents(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryListAPIDocumentsResponse:
        """
        List API documents in a namespace.
        
        Args:
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryListAPIDocumentsResponse: Default Response
        
        Example:
            ```python
            registry = client.registry.list_api_documents(
                namespace="namespace",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._get(
            path_template("/v1/apis/{namespace}", **{"namespace": namespace}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListAPIDocumentsResponse,
        )

    def create_api_document(
        self,
        namespace: str,
        *,
        title: str,
        description: str | Omit = omit,
        version: Version,
        slug: str,
        ruleset: str | Omit = omit,
        is_private: bool | Omit = omit,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryCreateAPIDocumentResponse:
        """
        Create an API document.
        
        Args:
            namespace: Path parameter.
            title: Body parameter.
            description: Body parameter.
            version: Body parameter.
            slug: Body parameter.
            ruleset: Body parameter.
            is_private: Body parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryCreateAPIDocumentResponse: Default Response
        
        Example:
            ```python
            registry = client.registry.create_api_document(
                namespace="namespace",
                title="",
                version="x",
                slug="",
                document="",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._post(
            path_template("/v1/apis/{namespace}", **{"namespace": namespace}),
            body=maybe_transform(
            {
            "title": title,
            "description": description,
            "version": version,
            "slug": slug,
            "ruleset": ruleset,
            "is_private": is_private,
            "document": document,
        },
            registry_create_api_document_params.RegistryCreateAPIDocumentParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryCreateAPIDocumentResponse,
        )

    def update_api_document(
        self,
        slug: str,
        *,
        namespace: str,
        title: str | Omit = omit,
        description: str | Omit = omit,
        is_private: bool | Omit = omit,
        ruleset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUpdateAPIDocumentResponse:
        """
        Update metadata for an API document.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            title: Body parameter.
            description: Body parameter.
            is_private: Body parameter.
            ruleset: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryUpdateAPIDocumentResponse: Default Response
        
        Example:
            ```python
            registry = client.registry.update_api_document(
                namespace="namespace",
                slug="slug",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._patch(
            path_template("/v1/apis/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {
            "title": title,
            "description": description,
            "is_private": is_private,
            "ruleset": ruleset,
        },
            registry_update_api_document_params.RegistryUpdateAPIDocumentParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryUpdateAPIDocumentResponse,
        )

    def delete_api_document(
        self,
        slug: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryDeleteAPIDocumentResponse:
        """
        Delete an API document and all versions.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryDeleteAPIDocumentResponse: Default Response
        
        Example:
            ```python
            registry = client.registry.delete_api_document(
                namespace="namespace",
                slug="slug",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/apis/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryDeleteAPIDocumentResponse,
        )

    def retrieve_api_document_version(
        self,
        semver: str,
        *,
        namespace: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Get a specific API document version.
        
        Args:
            semver: Path parameter.
            namespace: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            str: Default Response
        
        Example:
            ```python
            registry = client.registry.retrieve_api_document_version(
                namespace="namespace",
                slug="slug",
                semver="semver",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if semver is None or (isinstance(semver, str) and not semver):
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )

    def update_api_document_version(
        self,
        semver: str,
        *,
        namespace: str,
        slug: str,
        document: str,
        last_known_version_sha: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUpdateAPIDocumentVersionResponse:
        """
        Update the registry file content for an API document version.
        
        Args:
            semver: Path parameter.
            namespace: Path parameter.
            slug: Path parameter.
            document: Body parameter.
            last_known_version_sha: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryUpdateAPIDocumentVersionResponse: Default Response
        
        Example:
            ```python
            registry = client.registry.update_api_document_version(
                namespace="namespace",
                slug="slug",
                semver="semver",
                document="",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if semver is None or (isinstance(semver, str) and not semver):
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return self._patch(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            body=maybe_transform(
            {
            "document": document,
            "last_known_version_sha": last_known_version_sha,
        },
            registry_update_api_document_version_params.RegistryUpdateAPIDocumentVersionParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryUpdateAPIDocumentVersionResponse,
        )

    def delete_api_document_version(
        self,
        semver: str,
        *,
        namespace: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryDeleteAPIDocumentVersionResponse:
        """
        Delete a specific API document version.
        
        Args:
            semver: Path parameter.
            namespace: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryDeleteAPIDocumentVersionResponse: Default Response
        
        Example:
            ```python
            registry = client.registry.delete_api_document_version(
                namespace="namespace",
                slug="slug",
                semver="semver",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if semver is None or (isinstance(semver, str) and not semver):
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return self._delete(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryDeleteAPIDocumentVersionResponse,
        )

    def list_api_document_version_metadata(
        self,
        semver: str,
        *,
        namespace: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryListAPIDocumentVersionMetadataResponse:
        """
        Get metadata (uid, content shas, version sha, tags) for a specific API document version.
        
        Args:
            semver: Path parameter.
            namespace: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryListAPIDocumentVersionMetadataResponse: Default Response
        
        Example:
            ```python
            registry = client.registry.list_api_document_version_metadata(
                namespace="namespace",
                slug="slug",
                semver="semver",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if semver is None or (isinstance(semver, str) and not semver):
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return self._get(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}/metadata", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListAPIDocumentVersionMetadataResponse,
        )

    def create_api_document_version(
        self,
        slug: str,
        *,
        namespace: str,
        version: Version,
        document: str,
        force: bool | Omit = omit,
        last_known_version_sha: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryCreateAPIDocumentVersionResponse:
        """
        Create a new API document version.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            version: Body parameter.
            document: Body parameter.
            force: Body parameter.
            last_known_version_sha: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryCreateAPIDocumentVersionResponse: Default Response
        
        Example:
            ```python
            registry = client.registry.create_api_document_version(
                namespace="namespace",
                slug="slug",
                version="x",
                document="",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/v1/apis/{namespace}/{slug}/version", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {
            "version": version,
            "document": document,
            "force": force,
            "last_known_version_sha": last_known_version_sha,
        },
            registry_create_api_document_version_params.RegistryCreateAPIDocumentVersionParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryCreateAPIDocumentVersionResponse,
        )

    def create_api_document_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: Slug,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryCreateAPIDocumentAccessGroupResponse:
        """
        Add an access group to an API document.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryCreateAPIDocumentAccessGroupResponse: Default Response
        
        Example:
            ```python
            registry = client.registry.create_api_document_access_group(
                namespace="namespace",
                slug="slug",
                access_group_slug="xxx",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/v1/apis/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            registry_create_api_document_access_group_params.RegistryCreateAPIDocumentAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryCreateAPIDocumentAccessGroupResponse,
        )

    def delete_api_document_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: Slug,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryDeleteAPIDocumentAccessGroupResponse:
        """
        Remove an access group from an API document.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryDeleteAPIDocumentAccessGroupResponse: Default Response
        
        Example:
            ```python
            registry = client.registry.delete_api_document_access_group(
                namespace="namespace",
                slug="slug",
                access_group_slug="xxx",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/apis/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            registry_delete_api_document_access_group_params.RegistryDeleteAPIDocumentAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryDeleteAPIDocumentAccessGroupResponse,
        )


class AsyncRegistryResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncRegistryResourceWithRawResponse:
        return AsyncRegistryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegistryResourceWithStreamingResponse:
        return AsyncRegistryResourceWithStreamingResponse(self)

    async def list_all_api_documents(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryListAllAPIDocumentsResponse:
        """
        List all API documents across every namespace the caller can access.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryListAllAPIDocumentsResponse: Default Response
        
        Example:
            ```python
            registry = await client.registry.list_all_api_documents()
            ```
        """
        return await self._get(
            "/v1/apis",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListAllAPIDocumentsResponse,
        )

    async def list_api_documents(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryListAPIDocumentsResponse:
        """
        List API documents in a namespace.
        
        Args:
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryListAPIDocumentsResponse: Default Response
        
        Example:
            ```python
            registry = await client.registry.list_api_documents(
                namespace="namespace",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._get(
            path_template("/v1/apis/{namespace}", **{"namespace": namespace}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListAPIDocumentsResponse,
        )

    async def create_api_document(
        self,
        namespace: str,
        *,
        title: str,
        description: str | Omit = omit,
        version: Version,
        slug: str,
        ruleset: str | Omit = omit,
        is_private: bool | Omit = omit,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryCreateAPIDocumentResponse:
        """
        Create an API document.
        
        Args:
            namespace: Path parameter.
            title: Body parameter.
            description: Body parameter.
            version: Body parameter.
            slug: Body parameter.
            ruleset: Body parameter.
            is_private: Body parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryCreateAPIDocumentResponse: Default Response
        
        Example:
            ```python
            registry = await client.registry.create_api_document(
                namespace="namespace",
                title="",
                version="x",
                slug="",
                document="",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._post(
            path_template("/v1/apis/{namespace}", **{"namespace": namespace}),
            body=await async_maybe_transform(
            {
            "title": title,
            "description": description,
            "version": version,
            "slug": slug,
            "ruleset": ruleset,
            "is_private": is_private,
            "document": document,
        },
            registry_create_api_document_params.RegistryCreateAPIDocumentParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryCreateAPIDocumentResponse,
        )

    async def update_api_document(
        self,
        slug: str,
        *,
        namespace: str,
        title: str | Omit = omit,
        description: str | Omit = omit,
        is_private: bool | Omit = omit,
        ruleset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUpdateAPIDocumentResponse:
        """
        Update metadata for an API document.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            title: Body parameter.
            description: Body parameter.
            is_private: Body parameter.
            ruleset: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryUpdateAPIDocumentResponse: Default Response
        
        Example:
            ```python
            registry = await client.registry.update_api_document(
                namespace="namespace",
                slug="slug",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._patch(
            path_template("/v1/apis/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {
            "title": title,
            "description": description,
            "is_private": is_private,
            "ruleset": ruleset,
        },
            registry_update_api_document_params.RegistryUpdateAPIDocumentParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryUpdateAPIDocumentResponse,
        )

    async def delete_api_document(
        self,
        slug: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryDeleteAPIDocumentResponse:
        """
        Delete an API document and all versions.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryDeleteAPIDocumentResponse: Default Response
        
        Example:
            ```python
            registry = await client.registry.delete_api_document(
                namespace="namespace",
                slug="slug",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/apis/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryDeleteAPIDocumentResponse,
        )

    async def retrieve_api_document_version(
        self,
        semver: str,
        *,
        namespace: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Get a specific API document version.
        
        Args:
            semver: Path parameter.
            namespace: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            str: Default Response
        
        Example:
            ```python
            registry = await client.registry.retrieve_api_document_version(
                namespace="namespace",
                slug="slug",
                semver="semver",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if semver is None or (isinstance(semver, str) and not semver):
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )

    async def update_api_document_version(
        self,
        semver: str,
        *,
        namespace: str,
        slug: str,
        document: str,
        last_known_version_sha: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryUpdateAPIDocumentVersionResponse:
        """
        Update the registry file content for an API document version.
        
        Args:
            semver: Path parameter.
            namespace: Path parameter.
            slug: Path parameter.
            document: Body parameter.
            last_known_version_sha: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryUpdateAPIDocumentVersionResponse: Default Response
        
        Example:
            ```python
            registry = await client.registry.update_api_document_version(
                namespace="namespace",
                slug="slug",
                semver="semver",
                document="",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if semver is None or (isinstance(semver, str) and not semver):
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return await self._patch(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            body=await async_maybe_transform(
            {
            "document": document,
            "last_known_version_sha": last_known_version_sha,
        },
            registry_update_api_document_version_params.RegistryUpdateAPIDocumentVersionParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryUpdateAPIDocumentVersionResponse,
        )

    async def delete_api_document_version(
        self,
        semver: str,
        *,
        namespace: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryDeleteAPIDocumentVersionResponse:
        """
        Delete a specific API document version.
        
        Args:
            semver: Path parameter.
            namespace: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryDeleteAPIDocumentVersionResponse: Default Response
        
        Example:
            ```python
            registry = await client.registry.delete_api_document_version(
                namespace="namespace",
                slug="slug",
                semver="semver",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if semver is None or (isinstance(semver, str) and not semver):
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return await self._delete(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryDeleteAPIDocumentVersionResponse,
        )

    async def list_api_document_version_metadata(
        self,
        semver: str,
        *,
        namespace: str,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryListAPIDocumentVersionMetadataResponse:
        """
        Get metadata (uid, content shas, version sha, tags) for a specific API document version.
        
        Args:
            semver: Path parameter.
            namespace: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryListAPIDocumentVersionMetadataResponse: Default Response
        
        Example:
            ```python
            registry = await client.registry.list_api_document_version_metadata(
                namespace="namespace",
                slug="slug",
                semver="semver",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if semver is None or (isinstance(semver, str) and not semver):
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return await self._get(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}/metadata", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListAPIDocumentVersionMetadataResponse,
        )

    async def create_api_document_version(
        self,
        slug: str,
        *,
        namespace: str,
        version: Version,
        document: str,
        force: bool | Omit = omit,
        last_known_version_sha: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryCreateAPIDocumentVersionResponse:
        """
        Create a new API document version.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            version: Body parameter.
            document: Body parameter.
            force: Body parameter.
            last_known_version_sha: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryCreateAPIDocumentVersionResponse: Default Response
        
        Example:
            ```python
            registry = await client.registry.create_api_document_version(
                namespace="namespace",
                slug="slug",
                version="x",
                document="",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/v1/apis/{namespace}/{slug}/version", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {
            "version": version,
            "document": document,
            "force": force,
            "last_known_version_sha": last_known_version_sha,
        },
            registry_create_api_document_version_params.RegistryCreateAPIDocumentVersionParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryCreateAPIDocumentVersionResponse,
        )

    async def create_api_document_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: Slug,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryCreateAPIDocumentAccessGroupResponse:
        """
        Add an access group to an API document.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryCreateAPIDocumentAccessGroupResponse: Default Response
        
        Example:
            ```python
            registry = await client.registry.create_api_document_access_group(
                namespace="namespace",
                slug="slug",
                access_group_slug="xxx",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/v1/apis/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            registry_create_api_document_access_group_params.RegistryCreateAPIDocumentAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryCreateAPIDocumentAccessGroupResponse,
        )

    async def delete_api_document_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: Slug,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistryDeleteAPIDocumentAccessGroupResponse:
        """
        Remove an access group from an API document.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RegistryDeleteAPIDocumentAccessGroupResponse: Default Response
        
        Example:
            ```python
            registry = await client.registry.delete_api_document_access_group(
                namespace="namespace",
                slug="slug",
                access_group_slug="xxx",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/apis/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            registry_delete_api_document_access_group_params.RegistryDeleteAPIDocumentAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryDeleteAPIDocumentAccessGroupResponse,
        )


class RegistryResourceWithRawResponse:
    def __init__(self, registry: RegistryResource) -> None:
        self._registry = registry

        self.list_all_api_documents = to_raw_response_wrapper(
            registry.list_all_api_documents,
        )
        self.list_api_documents = to_raw_response_wrapper(
            registry.list_api_documents,
        )
        self.create_api_document = to_raw_response_wrapper(
            registry.create_api_document,
        )
        self.update_api_document = to_raw_response_wrapper(
            registry.update_api_document,
        )
        self.delete_api_document = to_raw_response_wrapper(
            registry.delete_api_document,
        )
        self.retrieve_api_document_version = to_raw_response_wrapper(
            registry.retrieve_api_document_version,
        )
        self.update_api_document_version = to_raw_response_wrapper(
            registry.update_api_document_version,
        )
        self.delete_api_document_version = to_raw_response_wrapper(
            registry.delete_api_document_version,
        )
        self.list_api_document_version_metadata = to_raw_response_wrapper(
            registry.list_api_document_version_metadata,
        )
        self.create_api_document_version = to_raw_response_wrapper(
            registry.create_api_document_version,
        )
        self.create_api_document_access_group = to_raw_response_wrapper(
            registry.create_api_document_access_group,
        )
        self.delete_api_document_access_group = to_raw_response_wrapper(
            registry.delete_api_document_access_group,
        )


class AsyncRegistryResourceWithRawResponse:
    def __init__(self, registry: AsyncRegistryResource) -> None:
        self._registry = registry

        self.list_all_api_documents = async_to_raw_response_wrapper(
            registry.list_all_api_documents,
        )
        self.list_api_documents = async_to_raw_response_wrapper(
            registry.list_api_documents,
        )
        self.create_api_document = async_to_raw_response_wrapper(
            registry.create_api_document,
        )
        self.update_api_document = async_to_raw_response_wrapper(
            registry.update_api_document,
        )
        self.delete_api_document = async_to_raw_response_wrapper(
            registry.delete_api_document,
        )
        self.retrieve_api_document_version = async_to_raw_response_wrapper(
            registry.retrieve_api_document_version,
        )
        self.update_api_document_version = async_to_raw_response_wrapper(
            registry.update_api_document_version,
        )
        self.delete_api_document_version = async_to_raw_response_wrapper(
            registry.delete_api_document_version,
        )
        self.list_api_document_version_metadata = async_to_raw_response_wrapper(
            registry.list_api_document_version_metadata,
        )
        self.create_api_document_version = async_to_raw_response_wrapper(
            registry.create_api_document_version,
        )
        self.create_api_document_access_group = async_to_raw_response_wrapper(
            registry.create_api_document_access_group,
        )
        self.delete_api_document_access_group = async_to_raw_response_wrapper(
            registry.delete_api_document_access_group,
        )


class RegistryResourceWithStreamingResponse:
    def __init__(self, registry: RegistryResource) -> None:
        self._registry = registry

        self.list_all_api_documents = to_streamed_response_wrapper(
            registry.list_all_api_documents,
        )
        self.list_api_documents = to_streamed_response_wrapper(
            registry.list_api_documents,
        )
        self.create_api_document = to_streamed_response_wrapper(
            registry.create_api_document,
        )
        self.update_api_document = to_streamed_response_wrapper(
            registry.update_api_document,
        )
        self.delete_api_document = to_streamed_response_wrapper(
            registry.delete_api_document,
        )
        self.retrieve_api_document_version = to_streamed_response_wrapper(
            registry.retrieve_api_document_version,
        )
        self.update_api_document_version = to_streamed_response_wrapper(
            registry.update_api_document_version,
        )
        self.delete_api_document_version = to_streamed_response_wrapper(
            registry.delete_api_document_version,
        )
        self.list_api_document_version_metadata = to_streamed_response_wrapper(
            registry.list_api_document_version_metadata,
        )
        self.create_api_document_version = to_streamed_response_wrapper(
            registry.create_api_document_version,
        )
        self.create_api_document_access_group = to_streamed_response_wrapper(
            registry.create_api_document_access_group,
        )
        self.delete_api_document_access_group = to_streamed_response_wrapper(
            registry.delete_api_document_access_group,
        )


class AsyncRegistryResourceWithStreamingResponse:
    def __init__(self, registry: AsyncRegistryResource) -> None:
        self._registry = registry

        self.list_all_api_documents = async_to_streamed_response_wrapper(
            registry.list_all_api_documents,
        )
        self.list_api_documents = async_to_streamed_response_wrapper(
            registry.list_api_documents,
        )
        self.create_api_document = async_to_streamed_response_wrapper(
            registry.create_api_document,
        )
        self.update_api_document = async_to_streamed_response_wrapper(
            registry.update_api_document,
        )
        self.delete_api_document = async_to_streamed_response_wrapper(
            registry.delete_api_document,
        )
        self.retrieve_api_document_version = async_to_streamed_response_wrapper(
            registry.retrieve_api_document_version,
        )
        self.update_api_document_version = async_to_streamed_response_wrapper(
            registry.update_api_document_version,
        )
        self.delete_api_document_version = async_to_streamed_response_wrapper(
            registry.delete_api_document_version,
        )
        self.list_api_document_version_metadata = async_to_streamed_response_wrapper(
            registry.list_api_document_version_metadata,
        )
        self.create_api_document_version = async_to_streamed_response_wrapper(
            registry.create_api_document_version,
        )
        self.create_api_document_access_group = async_to_streamed_response_wrapper(
            registry.create_api_document_access_group,
        )
        self.delete_api_document_access_group = async_to_streamed_response_wrapper(
            registry.delete_api_document_access_group,
        )
