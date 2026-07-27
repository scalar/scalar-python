# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.slug import Slug
from ...types.schemas import access_group_create_schema_params, access_group_delete_schema_params
from ...types.schemas.access_group_delete_schema_response import AccessGroupDeleteSchemaResponse

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
        access_group_slug: Slug,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessGroupCreateSchemaResponse:
        """
        Add an access group to a schema.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccessGroupCreateSchemaResponse: Default Response
        
        Example:
            ```python
            access_group = client.schemas.access_group.create_schema(
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
            path_template("/v1/schemas/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            access_group_create_schema_params.AccessGroupCreateSchemaParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccessGroupCreateSchemaResponse,
        )

    def delete_schema(
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
    ) -> AccessGroupDeleteSchemaResponse:
        """
        Remove an access group from a schema.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccessGroupDeleteSchemaResponse: Default Response
        
        Example:
            ```python
            access_group = client.schemas.access_group.delete_schema(
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
            path_template("/v1/schemas/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            access_group_delete_schema_params.AccessGroupDeleteSchemaParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
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
        access_group_slug: Slug,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessGroupCreateSchemaResponse:
        """
        Add an access group to a schema.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccessGroupCreateSchemaResponse: Default Response
        
        Example:
            ```python
            access_group = await client.schemas.access_group.create_schema(
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
            path_template("/v1/schemas/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            access_group_create_schema_params.AccessGroupCreateSchemaParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccessGroupCreateSchemaResponse,
        )

    async def delete_schema(
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
    ) -> AccessGroupDeleteSchemaResponse:
        """
        Remove an access group from a schema.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccessGroupDeleteSchemaResponse: Default Response
        
        Example:
            ```python
            access_group = await client.schemas.access_group.delete_schema(
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
            path_template("/v1/schemas/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            access_group_delete_schema_params.AccessGroupDeleteSchemaParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
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
