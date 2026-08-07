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
from ...types.schemas.version_delete_schema_response import VersionDeleteSchemaResponse
from ...types.schemas.version_create_schema_response import VersionCreateSchemaResponse
from ...types.version import Version
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
        Get a specific schema version document.

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
            version = client.schemas.version.retrieve_schema(
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
            path_template(
                "/v1/schemas/{namespace}/{slug}/version/{semver}",
                **{"namespace": namespace, "slug": slug, "semver": semver},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def delete_schema(
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
    ) -> VersionDeleteSchemaResponse:
        """
        Delete a schema version.

        Args:
            semver: Path parameter.
            namespace: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VersionDeleteSchemaResponse: Default Response

        Example:
            ```python
            version = client.schemas.version.delete_schema(
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
            path_template(
                "/v1/schemas/{namespace}/{slug}/version/{semver}",
                **{"namespace": namespace, "slug": slug, "semver": semver},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionDeleteSchemaResponse,
        )

    def create_schema(
        self,
        slug: str,
        *,
        namespace: str,
        version: Version,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionCreateSchemaResponse:
        """
        Create a schema version.

        Args:
            slug: Path parameter.
            namespace: Path parameter.
            version: Body parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VersionCreateSchemaResponse: Default Response

        Example:
            ```python
            version = client.schemas.version.create_schema(
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
            path_template("/v1/schemas/{namespace}/{slug}/version", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
                {
                    "version": version,
                    "document": document,
                },
                version_create_schema_params.VersionCreateSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        Get a specific schema version document.

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
            version = await client.schemas.version.retrieve_schema(
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
            path_template(
                "/v1/schemas/{namespace}/{slug}/version/{semver}",
                **{"namespace": namespace, "slug": slug, "semver": semver},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def delete_schema(
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
    ) -> VersionDeleteSchemaResponse:
        """
        Delete a schema version.

        Args:
            semver: Path parameter.
            namespace: Path parameter.
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VersionDeleteSchemaResponse: Default Response

        Example:
            ```python
            version = await client.schemas.version.delete_schema(
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
            path_template(
                "/v1/schemas/{namespace}/{slug}/version/{semver}",
                **{"namespace": namespace, "slug": slug, "semver": semver},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionDeleteSchemaResponse,
        )

    async def create_schema(
        self,
        slug: str,
        *,
        namespace: str,
        version: Version,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionCreateSchemaResponse:
        """
        Create a schema version.

        Args:
            slug: Path parameter.
            namespace: Path parameter.
            version: Body parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VersionCreateSchemaResponse: Default Response

        Example:
            ```python
            version = await client.schemas.version.create_schema(
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
            path_template("/v1/schemas/{namespace}/{slug}/version", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
                {
                    "version": version,
                    "document": document,
                },
                version_create_schema_params.VersionCreateSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
