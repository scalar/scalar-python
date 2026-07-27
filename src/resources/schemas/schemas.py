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
    VersionResourceWithRawResponse,
    AsyncVersionResourceWithRawResponse,
    VersionResourceWithStreamingResponse,
    AsyncVersionResourceWithStreamingResponse,
)
from .access_group import (
    AccessGroupResource,
    AsyncAccessGroupResource,
    AccessGroupResourceWithRawResponse,
    AsyncAccessGroupResourceWithRawResponse,
    AccessGroupResourceWithStreamingResponse,
    AsyncAccessGroupResourceWithStreamingResponse,
)
from ...types.schema_list_response import SchemaListResponse
from ...types.schema_create_response import SchemaCreateResponse
from ...types.version import Version
from ...types import schema_create_params, schema_update_params
from ...types.schema_update_response import SchemaUpdateResponse
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
        """
        List schemas in a namespace.
        
        Args:
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            SchemaListResponse: Default Response
        
        Example:
            ```python
            schema = client.schemas.list(
                namespace="namespace",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
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
        version: Version,
        slug: str,
        is_private: bool | Omit = omit,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaCreateResponse:
        """
        Create a schema in a namespace.
        
        Args:
            namespace: Path parameter.
            title: Body parameter.
            description: Body parameter.
            version: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            SchemaCreateResponse: Default Response
        
        Example:
            ```python
            schema = client.schemas.create(
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
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SchemaCreateResponse,
        )

    def update(
        self,
        slug: str,
        *,
        namespace: str,
        title: str | Omit = omit,
        description: str | Omit = omit,
        is_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaUpdateResponse:
        """
        Update schema metadata.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            title: Body parameter.
            description: Body parameter.
            is_private: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            SchemaUpdateResponse: Default Response
        
        Example:
            ```python
            schema = client.schemas.update(
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
            path_template("/v1/schemas/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {
            "title": title,
            "description": description,
            "is_private": is_private,
        },
            schema_update_params.SchemaUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SchemaUpdateResponse,
        )

    def delete(
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
    ) -> SchemaDeleteResponse:
        """
        Delete a schema and all related versions.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            SchemaDeleteResponse: Default Response
        
        Example:
            ```python
            schema = client.schemas.delete(
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
            path_template("/v1/schemas/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
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
        """
        List schemas in a namespace.
        
        Args:
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            SchemaListResponse: Default Response
        
        Example:
            ```python
            schema = await client.schemas.list(
                namespace="namespace",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
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
        version: Version,
        slug: str,
        is_private: bool | Omit = omit,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaCreateResponse:
        """
        Create a schema in a namespace.
        
        Args:
            namespace: Path parameter.
            title: Body parameter.
            description: Body parameter.
            version: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            SchemaCreateResponse: Default Response
        
        Example:
            ```python
            schema = await client.schemas.create(
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
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SchemaCreateResponse,
        )

    async def update(
        self,
        slug: str,
        *,
        namespace: str,
        title: str | Omit = omit,
        description: str | Omit = omit,
        is_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaUpdateResponse:
        """
        Update schema metadata.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            title: Body parameter.
            description: Body parameter.
            is_private: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            SchemaUpdateResponse: Default Response
        
        Example:
            ```python
            schema = await client.schemas.update(
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
            path_template("/v1/schemas/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {
            "title": title,
            "description": description,
            "is_private": is_private,
        },
            schema_update_params.SchemaUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SchemaUpdateResponse,
        )

    async def delete(
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
    ) -> SchemaDeleteResponse:
        """
        Delete a schema and all related versions.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            SchemaDeleteResponse: Default Response
        
        Example:
            ```python
            schema = await client.schemas.delete(
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
            path_template("/v1/schemas/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
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
    def version(self) -> VersionResourceWithRawResponse:
        return VersionResourceWithRawResponse(self._schemas.version)

    @cached_property
    def access_group(self) -> AccessGroupResourceWithRawResponse:
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
    def version(self) -> AsyncVersionResourceWithRawResponse:
        return AsyncVersionResourceWithRawResponse(self._schemas.version)

    @cached_property
    def access_group(self) -> AsyncAccessGroupResourceWithRawResponse:
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
    def version(self) -> VersionResourceWithStreamingResponse:
        return VersionResourceWithStreamingResponse(self._schemas.version)

    @cached_property
    def access_group(self) -> AccessGroupResourceWithStreamingResponse:
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
    def version(self) -> AsyncVersionResourceWithStreamingResponse:
        return AsyncVersionResourceWithStreamingResponse(self._schemas.version)

    @cached_property
    def access_group(self) -> AsyncAccessGroupResourceWithStreamingResponse:
        return AsyncAccessGroupResourceWithStreamingResponse(self._schemas.access_group)
