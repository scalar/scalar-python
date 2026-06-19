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
from ...types.schemas.access_group_create_schema_response import AccessGroupCreateSchemaResponse
from ...types.schemas import access_group_create_schema_params
from ...types.schemas.access_group_delete_schema_response import AccessGroupDeleteSchemaResponse
from ...types.schemas import access_group_delete_schema_params

__all__ = ["AccessGroupResource", "AsyncAccessGroupResource"]


class AccessGroupResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AccessGroupResourceWithRawResponse:
        return AccessGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessGroupResourceWithStreamingResponse:
        return AccessGroupResourceWithStreamingResponse(self)

    def create_schema(
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
    ) -> AccessGroupCreateSchemaResponse:
        """Add an access group to a schema."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/v1/schemas/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            access_group_create_schema_params.AccessGroupCreateSchemaParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=AccessGroupCreateSchemaResponse,
        )

    def delete_schema(
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
    ) -> AccessGroupDeleteSchemaResponse:
        """Remove an access group from a schema."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/schemas/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            access_group_delete_schema_params.AccessGroupDeleteSchemaParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=AccessGroupDeleteSchemaResponse,
        )


class AsyncAccessGroupResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncAccessGroupResourceWithRawResponse:
        return AsyncAccessGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessGroupResourceWithStreamingResponse:
        return AsyncAccessGroupResourceWithStreamingResponse(self)

    async def create_schema(
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
    ) -> AccessGroupCreateSchemaResponse:
        """Add an access group to a schema."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/v1/schemas/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            access_group_create_schema_params.AccessGroupCreateSchemaParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=AccessGroupCreateSchemaResponse,
        )

    async def delete_schema(
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
    ) -> AccessGroupDeleteSchemaResponse:
        """Remove an access group from a schema."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/schemas/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            access_group_delete_schema_params.AccessGroupDeleteSchemaParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=AccessGroupDeleteSchemaResponse,
        )


class AccessGroupResourceWithRawResponse:
    def __init__(self, access_group: AccessGroupResource) -> None:
        self._access_group = access_group

        self.create_schema = to_raw_response_wrapper(
            access_group.create_schema,
        )
        self.delete_schema = to_raw_response_wrapper(
            access_group.delete_schema,
        )


class AsyncAccessGroupResourceWithRawResponse:
    def __init__(self, access_group: AsyncAccessGroupResource) -> None:
        self._access_group = access_group

        self.create_schema = async_to_raw_response_wrapper(
            access_group.create_schema,
        )
        self.delete_schema = async_to_raw_response_wrapper(
            access_group.delete_schema,
        )


class AccessGroupResourceWithStreamingResponse:
    def __init__(self, access_group: AccessGroupResource) -> None:
        self._access_group = access_group

        self.create_schema = to_streamed_response_wrapper(
            access_group.create_schema,
        )
        self.delete_schema = to_streamed_response_wrapper(
            access_group.delete_schema,
        )


class AsyncAccessGroupResourceWithStreamingResponse:
    def __init__(self, access_group: AsyncAccessGroupResource) -> None:
        self._access_group = access_group

        self.create_schema = async_to_streamed_response_wrapper(
            access_group.create_schema,
        )
        self.delete_schema = async_to_streamed_response_wrapper(
            access_group.delete_schema,
        )
