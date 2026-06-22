# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .version import (
    VersionResource,
    AsyncVersionResource,
)
from .access_group import (
    AccessGroupResource,
    AsyncAccessGroupResource,
)
from ...types.schema_list_response import SchemaListResponse
from ...types.schema_create_response import SchemaCreateResponse
from ...types import schema_create_params
from ...types.schema_update_response import SchemaUpdateResponse
from ...types import schema_update_params
from ...types.schema_delete_response import SchemaDeleteResponse

__all__ = ["SchemasResource", "AsyncSchemasResource"]


class SchemasResource(SyncAPIResource):

    @cached_property
    def version(self) -> VersionResource:
        return VersionResource(self._client)

    @cached_property
    def access_group(self) -> AccessGroupResource:
        return AccessGroupResource(self._client)

    @cached_property
    def with_raw_response(self) -> SchemasResourceWithRawResponse:
        return SchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemasResourceWithStreamingResponse:
        return SchemasResourceWithStreamingResponse(self)

    def list(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaListResponse:
        """List schemas in a namespace."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._get(
            path_template("/v1/schemas/{namespace}", **{"namespace": namespace}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SchemaListResponse,
        )

    def create(
        self,
        namespace: str,
        *,
        title: str,
        description: str | Omit = omit,
        version: str,
        slug: str,
        is_private: bool | Omit = omit,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SchemaCreateResponse:
        """Create a schema in a namespace."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._post(
            path_template("/v1/schemas/{namespace}", **{"namespace": namespace}),
            body=maybe_transform(
            {
            "title": title,
            "description": description,
            "version": version,
            "slug": slug,
            "is_private": is_private,
            "document": document,
        },
            schema_create_params.SchemaCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=SchemaCreateResponse,
        )

    def update(
        self,
        namespace: str,
        slug: str,
        *,
        title: str | Omit = omit,
        description: str | Omit = omit,
        is_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SchemaUpdateResponse:
        """Update schema metadata."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._patch(
            path_template("/v1/schemas/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {
            "title": title,
            "description": description,
            "is_private": is_private,
        },
            schema_update_params.SchemaUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=SchemaUpdateResponse,
        )

    def delete(
        self,
        namespace: str,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SchemaDeleteResponse:
        """Delete a schema and all related versions."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/schemas/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=SchemaDeleteResponse,
        )


class AsyncSchemasResource(AsyncAPIResource):

    @cached_property
    def version(self) -> AsyncVersionResource:
        return AsyncVersionResource(self._client)

    @cached_property
    def access_group(self) -> AsyncAccessGroupResource:
        return AsyncAccessGroupResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSchemasResourceWithRawResponse:
        return AsyncSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemasResourceWithStreamingResponse:
        return AsyncSchemasResourceWithStreamingResponse(self)

    async def list(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaListResponse:
        """List schemas in a namespace."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._get(
            path_template("/v1/schemas/{namespace}", **{"namespace": namespace}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SchemaListResponse,
        )

    async def create(
        self,
        namespace: str,
        *,
        title: str,
        description: str | Omit = omit,
        version: str,
        slug: str,
        is_private: bool | Omit = omit,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SchemaCreateResponse:
        """Create a schema in a namespace."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._post(
            path_template("/v1/schemas/{namespace}", **{"namespace": namespace}),
            body=await async_maybe_transform(
            {
            "title": title,
            "description": description,
            "version": version,
            "slug": slug,
            "is_private": is_private,
            "document": document,
        },
            schema_create_params.SchemaCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=SchemaCreateResponse,
        )

    async def update(
        self,
        namespace: str,
        slug: str,
        *,
        title: str | Omit = omit,
        description: str | Omit = omit,
        is_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SchemaUpdateResponse:
        """Update schema metadata."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._patch(
            path_template("/v1/schemas/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {
            "title": title,
            "description": description,
            "is_private": is_private,
        },
            schema_update_params.SchemaUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=SchemaUpdateResponse,
        )

    async def delete(
        self,
        namespace: str,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SchemaDeleteResponse:
        """Delete a schema and all related versions."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/schemas/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=SchemaDeleteResponse,
        )


class SchemasResourceWithRawResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.list = to_raw_response_wrapper(
            schemas.list,
        )
        self.create = to_raw_response_wrapper(
            schemas.create,
        )
        self.update = to_raw_response_wrapper(
            schemas.update,
        )
        self.delete = to_raw_response_wrapper(
            schemas.delete,
        )

    @cached_property
    def version(self) -> "VersionResourceWithRawResponse":
        from .version import VersionResourceWithRawResponse
        return VersionResourceWithRawResponse(self._schemas.version)

    @cached_property
    def access_group(self) -> "AccessGroupResourceWithRawResponse":
        from .access_group import AccessGroupResourceWithRawResponse
        return AccessGroupResourceWithRawResponse(self._schemas.access_group)


class AsyncSchemasResourceWithRawResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.list = async_to_raw_response_wrapper(
            schemas.list,
        )
        self.create = async_to_raw_response_wrapper(
            schemas.create,
        )
        self.update = async_to_raw_response_wrapper(
            schemas.update,
        )
        self.delete = async_to_raw_response_wrapper(
            schemas.delete,
        )

    @cached_property
    def version(self) -> "AsyncVersionResourceWithRawResponse":
        from .version import AsyncVersionResourceWithRawResponse
        return AsyncVersionResourceWithRawResponse(self._schemas.version)

    @cached_property
    def access_group(self) -> "AsyncAccessGroupResourceWithRawResponse":
        from .access_group import AsyncAccessGroupResourceWithRawResponse
        return AsyncAccessGroupResourceWithRawResponse(self._schemas.access_group)


class SchemasResourceWithStreamingResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.list = to_streamed_response_wrapper(
            schemas.list,
        )
        self.create = to_streamed_response_wrapper(
            schemas.create,
        )
        self.update = to_streamed_response_wrapper(
            schemas.update,
        )
        self.delete = to_streamed_response_wrapper(
            schemas.delete,
        )

    @cached_property
    def version(self) -> "VersionResourceWithStreamingResponse":
        from .version import VersionResourceWithStreamingResponse
        return VersionResourceWithStreamingResponse(self._schemas.version)

    @cached_property
    def access_group(self) -> "AccessGroupResourceWithStreamingResponse":
        from .access_group import AccessGroupResourceWithStreamingResponse
        return AccessGroupResourceWithStreamingResponse(self._schemas.access_group)


class AsyncSchemasResourceWithStreamingResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.list = async_to_streamed_response_wrapper(
            schemas.list,
        )
        self.create = async_to_streamed_response_wrapper(
            schemas.create,
        )
        self.update = async_to_streamed_response_wrapper(
            schemas.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            schemas.delete,
        )

    @cached_property
    def version(self) -> "AsyncVersionResourceWithStreamingResponse":
        from .version import AsyncVersionResourceWithStreamingResponse
        return AsyncVersionResourceWithStreamingResponse(self._schemas.version)

    @cached_property
    def access_group(self) -> "AsyncAccessGroupResourceWithStreamingResponse":
        from .access_group import AsyncAccessGroupResourceWithStreamingResponse
        return AsyncAccessGroupResourceWithStreamingResponse(self._schemas.access_group)
