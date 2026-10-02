# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional
from typing_extensions import Literal

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
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from .repositories import (
    RepositoriesResource,
    AsyncRepositoriesResource,
    RepositoriesResourceWithRawResponse,
    AsyncRepositoriesResourceWithRawResponse,
    RepositoriesResourceWithStreamingResponse,
    AsyncRepositoriesResourceWithStreamingResponse,
)
from ...types.sdk_list_response import SdkListResponse
from ...types import sdk_list_params, sdk_create_params, sdk_update_params, sdk_build_params
from ...types.shared.uid import UID
from ...types.shared.nanoid import Nanoid
from ...types.slug import Slug
from ...types.sdk import Sdk
from ...types.sdk_update_response import SdkUpdateResponse
from ...types.sdk_delete_response import SdkDeleteResponse
from ...types.sdk_build_response import SdkBuildResponse

__all__ = ["SdksResource", "AsyncSdksResource"]


class SdksResource(SyncAPIResource):
    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def repositories(self) -> RepositoriesResource:
        return RepositoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SdksResourceWithRawResponse:
        return SdksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SdksResourceWithStreamingResponse:
        return SdksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SdkListResponse:
        """
        List every SDK on the team.

        Args:
            limit: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SdkListResponse: Default Response

        Example:
            ```python
            sdk = client.sdks.list()
            ```
        """
        return self._get(
            "/v1/sdks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, sdk_list_params.SdkListParams),
            ),
            cast_to=SdkListResponse,
        )

    def create(
        self,
        *,
        api_uid: Nanoid,
        languages: List[
            Literal[
                "typescript",
                "python",
                "cli",
                "csharp",
                "java",
                "ruby",
                "php",
                "go",
                "rust",
                "kotlin",
                "swift",
                "cpp",
                "dart",
            ]
        ],
        title: str | Omit = omit,
        slug: Slug | Omit = omit,
        class_name: str | Omit = omit,
        config: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UID:
        """
        Create an SDK from an API document, targeting one or more languages.

        Args:
            api_uid: Body parameter.
            languages: Body parameter.
            title: Body parameter.
            slug: Body parameter.
            class_name: Body parameter.
            config: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UID: Default Response

        Example:
            ```python
            sdk = client.sdks.create(
                api_uid="UakgbKJ5m9gl0JDMbcJqL",
                languages=["typescript"],
            )
            ```
        """
        return self._post(
            "/v1/sdks",
            body=maybe_transform(
                {
                    "api_uid": api_uid,
                    "languages": languages,
                    "title": title,
                    "slug": slug,
                    "class_name": class_name,
                    "config": config,
                },
                sdk_create_params.SdkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UID,
        )

    def retrieve(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Sdk:
        """
        Get a single SDK by its uid.

        Args:
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Sdk: Default Response

        Example:
            ```python
            sdk = client.sdks.retrieve(
                uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get(
            path_template("/v1/sdks/{uid}", **{"uid": uid}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sdk,
        )

    def update(
        self,
        uid: str,
        *,
        title: str | Omit = omit,
        slug: Slug | Omit = omit,
        is_private: bool | Omit = omit,
        config: str | Omit = omit,
        api_uid: Optional[Nanoid] | Omit = omit,
        api_version: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SdkUpdateResponse:
        """
        Update SDK metadata, its linked API, or its config.

        Args:
            uid: Path parameter.
            title: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            config: Body parameter.
            api_uid: Body parameter.
            api_version: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SdkUpdateResponse: Default Response

        Example:
            ```python
            sdk = client.sdks.update(
                uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._patch(
            path_template("/v1/sdks/{uid}", **{"uid": uid}),
            body=maybe_transform(
                {
                    "title": title,
                    "slug": slug,
                    "is_private": is_private,
                    "config": config,
                    "api_uid": api_uid,
                    "api_version": api_version,
                },
                sdk_update_params.SdkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SdkUpdateResponse,
        )

    def delete(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SdkDeleteResponse:
        """
        Delete an SDK and every version it holds.

        Args:
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SdkDeleteResponse: Default Response

        Example:
            ```python
            sdk = client.sdks.delete(
                uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._delete(
            path_template("/v1/sdks/{uid}", **{"uid": uid}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SdkDeleteResponse,
        )

    def build(
        self,
        uid: str,
        *,
        version: str | Omit = omit,
        languages: List[
            Literal[
                "typescript",
                "python",
                "cli",
                "csharp",
                "java",
                "ruby",
                "php",
                "go",
                "rust",
                "kotlin",
                "swift",
                "cpp",
                "dart",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SdkBuildResponse:
        """
        Start a build. Omit `version` to build the current work — the open draft, else the latest version — and the resolved version comes back in the response.

        Args:
            uid: Path parameter.
            version: Body parameter.
            languages: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SdkBuildResponse: Default Response

        Example:
            ```python
            sdk = client.sdks.build(
                uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._post(
            path_template("/v1/sdks/{uid}/build", **{"uid": uid}),
            body=maybe_transform(
                {
                    "version": version,
                    "languages": languages,
                },
                sdk_build_params.SdkBuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SdkBuildResponse,
        )


class AsyncSdksResource(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def repositories(self) -> AsyncRepositoriesResource:
        return AsyncRepositoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSdksResourceWithRawResponse:
        return AsyncSdksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSdksResourceWithStreamingResponse:
        return AsyncSdksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SdkListResponse:
        """
        List every SDK on the team.

        Args:
            limit: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SdkListResponse: Default Response

        Example:
            ```python
            sdk = await client.sdks.list()
            ```
        """
        return await self._get(
            "/v1/sdks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"limit": limit}, sdk_list_params.SdkListParams),
            ),
            cast_to=SdkListResponse,
        )

    async def create(
        self,
        *,
        api_uid: Nanoid,
        languages: List[
            Literal[
                "typescript",
                "python",
                "cli",
                "csharp",
                "java",
                "ruby",
                "php",
                "go",
                "rust",
                "kotlin",
                "swift",
                "cpp",
                "dart",
            ]
        ],
        title: str | Omit = omit,
        slug: Slug | Omit = omit,
        class_name: str | Omit = omit,
        config: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UID:
        """
        Create an SDK from an API document, targeting one or more languages.

        Args:
            api_uid: Body parameter.
            languages: Body parameter.
            title: Body parameter.
            slug: Body parameter.
            class_name: Body parameter.
            config: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UID: Default Response

        Example:
            ```python
            sdk = await client.sdks.create(
                api_uid="UakgbKJ5m9gl0JDMbcJqL",
                languages=["typescript"],
            )
            ```
        """
        return await self._post(
            "/v1/sdks",
            body=await async_maybe_transform(
                {
                    "api_uid": api_uid,
                    "languages": languages,
                    "title": title,
                    "slug": slug,
                    "class_name": class_name,
                    "config": config,
                },
                sdk_create_params.SdkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UID,
        )

    async def retrieve(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Sdk:
        """
        Get a single SDK by its uid.

        Args:
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Sdk: Default Response

        Example:
            ```python
            sdk = await client.sdks.retrieve(
                uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._get(
            path_template("/v1/sdks/{uid}", **{"uid": uid}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sdk,
        )

    async def update(
        self,
        uid: str,
        *,
        title: str | Omit = omit,
        slug: Slug | Omit = omit,
        is_private: bool | Omit = omit,
        config: str | Omit = omit,
        api_uid: Optional[Nanoid] | Omit = omit,
        api_version: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SdkUpdateResponse:
        """
        Update SDK metadata, its linked API, or its config.

        Args:
            uid: Path parameter.
            title: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            config: Body parameter.
            api_uid: Body parameter.
            api_version: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SdkUpdateResponse: Default Response

        Example:
            ```python
            sdk = await client.sdks.update(
                uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._patch(
            path_template("/v1/sdks/{uid}", **{"uid": uid}),
            body=await async_maybe_transform(
                {
                    "title": title,
                    "slug": slug,
                    "is_private": is_private,
                    "config": config,
                    "api_uid": api_uid,
                    "api_version": api_version,
                },
                sdk_update_params.SdkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SdkUpdateResponse,
        )

    async def delete(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SdkDeleteResponse:
        """
        Delete an SDK and every version it holds.

        Args:
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SdkDeleteResponse: Default Response

        Example:
            ```python
            sdk = await client.sdks.delete(
                uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._delete(
            path_template("/v1/sdks/{uid}", **{"uid": uid}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SdkDeleteResponse,
        )

    async def build(
        self,
        uid: str,
        *,
        version: str | Omit = omit,
        languages: List[
            Literal[
                "typescript",
                "python",
                "cli",
                "csharp",
                "java",
                "ruby",
                "php",
                "go",
                "rust",
                "kotlin",
                "swift",
                "cpp",
                "dart",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SdkBuildResponse:
        """
        Start a build. Omit `version` to build the current work — the open draft, else the latest version — and the resolved version comes back in the response.

        Args:
            uid: Path parameter.
            version: Body parameter.
            languages: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SdkBuildResponse: Default Response

        Example:
            ```python
            sdk = await client.sdks.build(
                uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._post(
            path_template("/v1/sdks/{uid}/build", **{"uid": uid}),
            body=await async_maybe_transform(
                {
                    "version": version,
                    "languages": languages,
                },
                sdk_build_params.SdkBuildParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SdkBuildResponse,
        )


class SdksResourceWithRawResponse:
    def __init__(self, sdks: SdksResource) -> None:
        self._sdks = sdks

        self.list = to_raw_response_wrapper(
            sdks.list,
        )
        self.create = to_raw_response_wrapper(
            sdks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sdks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sdks.update,
        )
        self.delete = to_raw_response_wrapper(
            sdks.delete,
        )
        self.build = to_raw_response_wrapper(
            sdks.build,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._sdks.versions)

    @cached_property
    def repositories(self) -> RepositoriesResourceWithRawResponse:
        return RepositoriesResourceWithRawResponse(self._sdks.repositories)


class AsyncSdksResourceWithRawResponse:
    def __init__(self, sdks: AsyncSdksResource) -> None:
        self._sdks = sdks

        self.list = async_to_raw_response_wrapper(
            sdks.list,
        )
        self.create = async_to_raw_response_wrapper(
            sdks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sdks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sdks.update,
        )
        self.delete = async_to_raw_response_wrapper(
            sdks.delete,
        )
        self.build = async_to_raw_response_wrapper(
            sdks.build,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._sdks.versions)

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithRawResponse:
        return AsyncRepositoriesResourceWithRawResponse(self._sdks.repositories)


class SdksResourceWithStreamingResponse:
    def __init__(self, sdks: SdksResource) -> None:
        self._sdks = sdks

        self.list = to_streamed_response_wrapper(
            sdks.list,
        )
        self.create = to_streamed_response_wrapper(
            sdks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sdks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sdks.update,
        )
        self.delete = to_streamed_response_wrapper(
            sdks.delete,
        )
        self.build = to_streamed_response_wrapper(
            sdks.build,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._sdks.versions)

    @cached_property
    def repositories(self) -> RepositoriesResourceWithStreamingResponse:
        return RepositoriesResourceWithStreamingResponse(self._sdks.repositories)


class AsyncSdksResourceWithStreamingResponse:
    def __init__(self, sdks: AsyncSdksResource) -> None:
        self._sdks = sdks

        self.list = async_to_streamed_response_wrapper(
            sdks.list,
        )
        self.create = async_to_streamed_response_wrapper(
            sdks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sdks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sdks.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            sdks.delete,
        )
        self.build = async_to_streamed_response_wrapper(
            sdks.build,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._sdks.versions)

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithStreamingResponse:
        return AsyncRepositoriesResourceWithStreamingResponse(self._sdks.repositories)
