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
from ...types.sdks.version_create_response import VersionCreateResponse
from ...types.sdks import version_create_params
from ...types.sdks.version_delete_response import VersionDeleteResponse

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self)

    def create(
        self,
        uid: str,
        *,
        version: str,
        api_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionCreateResponse:
        """
        Create a new SDK version against a specific API version.

        Args:
            uid: Path parameter.
            version: Body parameter.
            api_version: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VersionCreateResponse: Default Response

        Example:
            ```python
            version = client.sdks.versions.create(
                uid="uidxx",
                version="",
                api_version="",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._post(
            path_template("/v1/sdks/{uid}/versions", **{"uid": uid}),
            body=maybe_transform(
                {
                    "version": version,
                    "api_version": api_version,
                },
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionCreateResponse,
        )

    def delete(
        self,
        version: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionDeleteResponse:
        """
        Permanently delete one version of an SDK.

        Args:
            version: Path parameter.
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VersionDeleteResponse: Default Response

        Example:
            ```python
            version = client.sdks.versions.delete(
                uid="uidxx",
                version="version",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if version is None or (isinstance(version, str) and not version):
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._delete(
            path_template("/v1/sdks/{uid}/versions/{version}", **{"uid": uid, "version": version}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionDeleteResponse,
        )


class AsyncVersionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self)

    async def create(
        self,
        uid: str,
        *,
        version: str,
        api_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionCreateResponse:
        """
        Create a new SDK version against a specific API version.

        Args:
            uid: Path parameter.
            version: Body parameter.
            api_version: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VersionCreateResponse: Default Response

        Example:
            ```python
            version = await client.sdks.versions.create(
                uid="uidxx",
                version="",
                api_version="",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._post(
            path_template("/v1/sdks/{uid}/versions", **{"uid": uid}),
            body=await async_maybe_transform(
                {
                    "version": version,
                    "api_version": api_version,
                },
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionCreateResponse,
        )

    async def delete(
        self,
        version: str,
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionDeleteResponse:
        """
        Permanently delete one version of an SDK.

        Args:
            version: Path parameter.
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VersionDeleteResponse: Default Response

        Example:
            ```python
            version = await client.sdks.versions.delete(
                uid="uidxx",
                version="version",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if version is None or (isinstance(version, str) and not version):
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return await self._delete(
            path_template("/v1/sdks/{uid}/versions/{version}", **{"uid": uid, "version": version}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionDeleteResponse,
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_raw_response_wrapper(
            versions.create,
        )
        self.delete = to_raw_response_wrapper(
            versions.delete,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_raw_response_wrapper(
            versions.create,
        )
        self.delete = async_to_raw_response_wrapper(
            versions.delete,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_streamed_response_wrapper(
            versions.create,
        )
        self.delete = to_streamed_response_wrapper(
            versions.delete,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_streamed_response_wrapper(
            versions.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            versions.delete,
        )
