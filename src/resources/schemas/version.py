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
from ...types.schemas.version_retrieve_schema_response import VersionRetrieveSchemaResponse
from ...types.schemas.version_delete_schema_response import VersionDeleteSchemaResponse
from ...types.schemas.version_create_schema_response import VersionCreateSchemaResponse
from ...types.schemas import version_create_schema_params

__all__ = ["VersionResource", "AsyncVersionResource"]


class VersionResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> VersionResourceWithRawResponse:
        return VersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionResourceWithStreamingResponse:
        return VersionResourceWithStreamingResponse(self)

    def retrieve_schema(
        self,
        namespace: str,
        slug: str,
        semver: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionRetrieveSchemaResponse:
        """Get a specific schema version document."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return self._get(
            path_template("/v1/schemas/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=VersionRetrieveSchemaResponse,
        )

    def delete_schema(
        self,
        namespace: str,
        slug: str,
        semver: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VersionDeleteSchemaResponse:
        """Delete a schema version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return self._delete(
            path_template("/v1/schemas/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=VersionDeleteSchemaResponse,
        )

    def create_schema(
        self,
        namespace: str,
        slug: str,
        *,
        version: str,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VersionCreateSchemaResponse:
        """Create a schema version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/v1/schemas/{namespace}/{slug}/version", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {
            "version": version,
            "document": document,
        },
            version_create_schema_params.VersionCreateSchemaParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=VersionCreateSchemaResponse,
        )


class AsyncVersionResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncVersionResourceWithRawResponse:
        return AsyncVersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionResourceWithStreamingResponse:
        return AsyncVersionResourceWithStreamingResponse(self)

    async def retrieve_schema(
        self,
        namespace: str,
        slug: str,
        semver: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionRetrieveSchemaResponse:
        """Get a specific schema version document."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return await self._get(
            path_template("/v1/schemas/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=VersionRetrieveSchemaResponse,
        )

    async def delete_schema(
        self,
        namespace: str,
        slug: str,
        semver: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VersionDeleteSchemaResponse:
        """Delete a schema version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not semver:
            raise ValueError(f"Expected a non-empty value for `semver` but received {semver!r}")
        return await self._delete(
            path_template("/v1/schemas/{namespace}/{slug}/version/{semver}", **{"namespace": namespace, "slug": slug, "semver": semver}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=VersionDeleteSchemaResponse,
        )

    async def create_schema(
        self,
        namespace: str,
        slug: str,
        *,
        version: str,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VersionCreateSchemaResponse:
        """Create a schema version."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/v1/schemas/{namespace}/{slug}/version", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {
            "version": version,
            "document": document,
        },
            version_create_schema_params.VersionCreateSchemaParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=VersionCreateSchemaResponse,
        )


class VersionResourceWithRawResponse:
    def __init__(self, version: VersionResource) -> None:
        self._version = version

        self.retrieve_schema = to_raw_response_wrapper(
            version.retrieve_schema,
        )
        self.delete_schema = to_raw_response_wrapper(
            version.delete_schema,
        )
        self.create_schema = to_raw_response_wrapper(
            version.create_schema,
        )


class AsyncVersionResourceWithRawResponse:
    def __init__(self, version: AsyncVersionResource) -> None:
        self._version = version

        self.retrieve_schema = async_to_raw_response_wrapper(
            version.retrieve_schema,
        )
        self.delete_schema = async_to_raw_response_wrapper(
            version.delete_schema,
        )
        self.create_schema = async_to_raw_response_wrapper(
            version.create_schema,
        )


class VersionResourceWithStreamingResponse:
    def __init__(self, version: VersionResource) -> None:
        self._version = version

        self.retrieve_schema = to_streamed_response_wrapper(
            version.retrieve_schema,
        )
        self.delete_schema = to_streamed_response_wrapper(
            version.delete_schema,
        )
        self.create_schema = to_streamed_response_wrapper(
            version.create_schema,
        )


class AsyncVersionResourceWithStreamingResponse:
    def __init__(self, version: AsyncVersionResource) -> None:
        self._version = version

        self.retrieve_schema = async_to_streamed_response_wrapper(
            version.retrieve_schema,
        )
        self.delete_schema = async_to_streamed_response_wrapper(
            version.delete_schema,
        )
        self.create_schema = async_to_streamed_response_wrapper(
            version.create_schema,
        )
