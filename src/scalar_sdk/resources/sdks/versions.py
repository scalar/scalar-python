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
        api_version: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionCreateResponse:
        """
        Create a version label from a version of the SDK's API document and start its build. The label is the document version, and it becomes `latestVersion` when it is the highest.

        Args:
            uid: Path parameter.
            version: Body parameter.
            api_version: Removed. A request that carries it is refused with a 400.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VersionCreateResponse: Default Response

        Example:
            ```python
            version = client.sdks.versions.create(
                uid="UakgbKJ5m9gl0JDMbcJqL",
                version="1.2.0",
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
        Permanently delete one version label of an SDK and its builds. A label that is the current build of any language promoting manually is refused with 409 and nothing is deleted; promote or roll back to another build for that language first. Each other language whose current build was of that label moves to the active build of the highest remaining label that has one for the language, and has no current build when none has; `currentVersion` shows the result. Each language that moved to another build syncs it to its linked repository unless the repository already holds it. When it was `latestVersion`, that tag moves to the highest remaining label holding an active build. An SDK's last version cannot be deleted.

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
                uid="UakgbKJ5m9gl0JDMbcJqL",
                version="1.2.0",
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
        api_version: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionCreateResponse:
        """
        Create a version label from a version of the SDK's API document and start its build. The label is the document version, and it becomes `latestVersion` when it is the highest.

        Args:
            uid: Path parameter.
            version: Body parameter.
            api_version: Removed. A request that carries it is refused with a 400.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VersionCreateResponse: Default Response

        Example:
            ```python
            version = await client.sdks.versions.create(
                uid="UakgbKJ5m9gl0JDMbcJqL",
                version="1.2.0",
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
        Permanently delete one version label of an SDK and its builds. A label that is the current build of any language promoting manually is refused with 409 and nothing is deleted; promote or roll back to another build for that language first. Each other language whose current build was of that label moves to the active build of the highest remaining label that has one for the language, and has no current build when none has; `currentVersion` shows the result. Each language that moved to another build syncs it to its linked repository unless the repository already holds it. When it was `latestVersion`, that tag moves to the highest remaining label holding an active build. An SDK's last version cannot be deleted.

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
                uid="UakgbKJ5m9gl0JDMbcJqL",
                version="1.2.0",
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
