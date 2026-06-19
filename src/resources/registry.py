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
from ..types.registry_list_all_api_documents_response import RegistryListAllApiDocumentsResponse
from ..types.registry_list_api_documents_response import RegistryListApiDocumentsResponse
from ..types.registry_create_api_document_response import RegistryCreateApiDocumentResponse
from ..types import registry_create_api_document_params
from ..types.registry_update_api_document_response import RegistryUpdateApiDocumentResponse
from ..types import registry_update_api_document_params
from ..types.registry_delete_api_document_response import RegistryDeleteApiDocumentResponse
from ..types.registry_retrieve_api_document_version_response import RegistryRetrieveApiDocumentVersionResponse
from ..types.registry_update_api_document_version_response import RegistryUpdateApiDocumentVersionResponse
from ..types import registry_update_api_document_version_params
from ..types.registry_delete_api_document_version_response import RegistryDeleteApiDocumentVersionResponse
from ..types.registry_list_api_document_version_metadata_response import RegistryListApiDocumentVersionMetadataResponse
from ..types.registry_create_api_document_version_response import RegistryCreateApiDocumentVersionResponse
from ..types import registry_create_api_document_version_params
from ..types.registry_create_api_document_access_group_response import RegistryCreateApiDocumentAccessGroupResponse
from ..types import registry_create_api_document_access_group_params
from ..types.registry_delete_api_document_access_group_response import RegistryDeleteApiDocumentAccessGroupResponse
from ..types import registry_delete_api_document_access_group_params

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
    ) -> RegistryListAllApiDocumentsResponse:
        """List all API documents across every namespace the caller can access."""
        return self._get(
            "/v1/apis",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListAllApiDocumentsResponse,
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
    ) -> RegistryListApiDocumentsResponse:
        """List API documents in a namespace."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._get(
            path_template("/v1/apis/{namespace}", **{"namespace": namespace}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListApiDocumentsResponse,
        )

    def create_api_document(
        self,
        namespace: str,
        *,
        title: str,
        description: str | Omit = omit,
        version: str,
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
        idempotency_key: str | None = None,
    ) -> RegistryCreateApiDocumentResponse:
        """Create an API document."""
        if not namespace:
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
            registry_create_api_document_params.RegistryCreateApiDocumentParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryCreateApiDocumentResponse,
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
        idempotency_key: str | None = None,
    ) -> RegistryUpdateApiDocumentResponse:
        """Update metadata for an API document."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
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
            registry_update_api_document_params.RegistryUpdateApiDocumentParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryUpdateApiDocumentResponse,
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
        idempotency_key: str | None = None,
    ) -> RegistryDeleteApiDocumentResponse:
        """Delete an API document and all versions."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/apis/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryDeleteApiDocumentResponse,
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
    ) -> RegistryRetrieveApiDocumentVersionResponse:
        """Get a specific API document version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return self._get(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryRetrieveApiDocumentVersionResponse,
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
        idempotency_key: str | None = None,
    ) -> RegistryUpdateApiDocumentVersionResponse:
        """Update the registry file content for an API document version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return self._patch(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            body=maybe_transform(
            {
            "document": document,
            "last_known_version_sha": last_known_version_sha,
        },
            registry_update_api_document_version_params.RegistryUpdateApiDocumentVersionParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryUpdateApiDocumentVersionResponse,
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
        idempotency_key: str | None = None,
    ) -> RegistryDeleteApiDocumentVersionResponse:
        """Delete a specific API document version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return self._delete(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryDeleteApiDocumentVersionResponse,
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
    ) -> RegistryListApiDocumentVersionMetadataResponse:
        """Get metadata (uid, content shas, version sha, tags) for a specific API document version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return self._get(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}/metadata", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListApiDocumentVersionMetadataResponse,
        )

    def create_api_document_version(
        self,
        slug: str,
        *,
        namespace: str,
        version: str,
        document: str,
        force: bool | Omit = omit,
        last_known_version_sha: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RegistryCreateApiDocumentVersionResponse:
        """Create a new API document version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
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
            registry_create_api_document_version_params.RegistryCreateApiDocumentVersionParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryCreateApiDocumentVersionResponse,
        )

    def create_api_document_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RegistryCreateApiDocumentAccessGroupResponse:
        """Add an access group to an API document."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/v1/apis/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            registry_create_api_document_access_group_params.RegistryCreateApiDocumentAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryCreateApiDocumentAccessGroupResponse,
        )

    def delete_api_document_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RegistryDeleteApiDocumentAccessGroupResponse:
        """Remove an access group from an API document."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/apis/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            registry_delete_api_document_access_group_params.RegistryDeleteApiDocumentAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryDeleteApiDocumentAccessGroupResponse,
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
    ) -> RegistryListAllApiDocumentsResponse:
        """List all API documents across every namespace the caller can access."""
        return await self._get(
            "/v1/apis",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListAllApiDocumentsResponse,
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
    ) -> RegistryListApiDocumentsResponse:
        """List API documents in a namespace."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._get(
            path_template("/v1/apis/{namespace}", **{"namespace": namespace}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListApiDocumentsResponse,
        )

    async def create_api_document(
        self,
        namespace: str,
        *,
        title: str,
        description: str | Omit = omit,
        version: str,
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
        idempotency_key: str | None = None,
    ) -> RegistryCreateApiDocumentResponse:
        """Create an API document."""
        if not namespace:
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
            registry_create_api_document_params.RegistryCreateApiDocumentParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryCreateApiDocumentResponse,
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
        idempotency_key: str | None = None,
    ) -> RegistryUpdateApiDocumentResponse:
        """Update metadata for an API document."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
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
            registry_update_api_document_params.RegistryUpdateApiDocumentParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryUpdateApiDocumentResponse,
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
        idempotency_key: str | None = None,
    ) -> RegistryDeleteApiDocumentResponse:
        """Delete an API document and all versions."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/apis/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryDeleteApiDocumentResponse,
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
    ) -> RegistryRetrieveApiDocumentVersionResponse:
        """Get a specific API document version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return await self._get(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryRetrieveApiDocumentVersionResponse,
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
        idempotency_key: str | None = None,
    ) -> RegistryUpdateApiDocumentVersionResponse:
        """Update the registry file content for an API document version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return await self._patch(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            body=await async_maybe_transform(
            {
            "document": document,
            "last_known_version_sha": last_known_version_sha,
        },
            registry_update_api_document_version_params.RegistryUpdateApiDocumentVersionParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryUpdateApiDocumentVersionResponse,
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
        idempotency_key: str | None = None,
    ) -> RegistryDeleteApiDocumentVersionResponse:
        """Delete a specific API document version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return await self._delete(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryDeleteApiDocumentVersionResponse,
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
    ) -> RegistryListApiDocumentVersionMetadataResponse:
        """Get metadata (uid, content shas, version sha, tags) for a specific API document version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return await self._get(
            path_template("/v1/apis/{namespace}/{slug}/version/{semver}/metadata", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RegistryListApiDocumentVersionMetadataResponse,
        )

    async def create_api_document_version(
        self,
        slug: str,
        *,
        namespace: str,
        version: str,
        document: str,
        force: bool | Omit = omit,
        last_known_version_sha: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RegistryCreateApiDocumentVersionResponse:
        """Create a new API document version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
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
            registry_create_api_document_version_params.RegistryCreateApiDocumentVersionParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryCreateApiDocumentVersionResponse,
        )

    async def create_api_document_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RegistryCreateApiDocumentAccessGroupResponse:
        """Add an access group to an API document."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/v1/apis/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            registry_create_api_document_access_group_params.RegistryCreateApiDocumentAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryCreateApiDocumentAccessGroupResponse,
        )

    async def delete_api_document_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RegistryDeleteApiDocumentAccessGroupResponse:
        """Remove an access group from an API document."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/apis/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            registry_delete_api_document_access_group_params.RegistryDeleteApiDocumentAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RegistryDeleteApiDocumentAccessGroupResponse,
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
