# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ...types.sdks.repository_link_response import RepositoryLinkResponse
from ...types.sdks import repository_link_params, repository_update_publishing_params
from ...types.sdks.repository_unlink_response import RepositoryUnlinkResponse
from ...types.sdks.repository_update_publishing_response import RepositoryUpdatePublishingResponse

__all__ = ["RepositoriesResource", "AsyncRepositoriesResource"]


class RepositoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RepositoriesResourceWithRawResponse:
        return RepositoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RepositoriesResourceWithStreamingResponse:
        return RepositoriesResourceWithStreamingResponse(self)

    def link(
        self,
        uid: str,
        *,
        language: Literal[
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
        ],
        repository_id: int,
        base_branch: str,
        prerelease_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryLinkResponse:
        """
        Link one language target to a GitHub repository, so builds sync there.

        Args:
            uid: Path parameter.
            language: Body parameter.
            repository_id: Body parameter.
            base_branch: Body parameter.
            prerelease_type: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryLinkResponse: Default Response

        Example:
            ```python
            repository = client.sdks.repositories.link(
                uid="UakgbKJ5m9gl0JDMbcJqL",
                language="typescript",
                repository_id=123456789,
                base_branch="main",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._post(
            path_template("/v1/sdks/{uid}/repositories", **{"uid": uid}),
            body=maybe_transform(
                {
                    "language": language,
                    "repository_id": repository_id,
                    "base_branch": base_branch,
                    "prerelease_type": prerelease_type,
                },
                repository_link_params.RepositoryLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryLinkResponse,
        )

    def unlink(
        self,
        language: Literal[
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
        ],
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryUnlinkResponse:
        """
        Unlink one language target from its repository.

        Args:
            language: Path parameter.
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryUnlinkResponse: Default Response

        Example:
            ```python
            repository = client.sdks.repositories.unlink(
                uid="UakgbKJ5m9gl0JDMbcJqL",
                language="typescript",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if language is None or (isinstance(language, str) and not language):
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return self._delete(
            path_template("/v1/sdks/{uid}/repositories/{language}", **{"uid": uid, "language": language}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryUnlinkResponse,
        )

    def update_publishing(
        self,
        language: Literal[
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
        ],
        *,
        uid: str,
        publish_on_merge: bool,
        auth_method: Literal["oidc", "access-token"] | Omit = omit,
        access: Literal["public", "restricted"] | Omit = omit,
        tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryUpdatePublishingResponse:
        """
        Toggle publish-on-merge and the release settings for a linked target.

        Args:
            language: Path parameter.
            uid: Path parameter.
            publish_on_merge: Body parameter.
            auth_method: Body parameter.
            access: Body parameter.
            tag: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryUpdatePublishingResponse: Default Response

        Example:
            ```python
            repository = client.sdks.repositories.update_publishing(
                uid="UakgbKJ5m9gl0JDMbcJqL",
                language="typescript",
                publish_on_merge=True,
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if language is None or (isinstance(language, str) and not language):
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return self._post(
            path_template("/v1/sdks/{uid}/repositories/{language}/publishing", **{"uid": uid, "language": language}),
            body=maybe_transform(
                {
                    "publish_on_merge": publish_on_merge,
                    "auth_method": auth_method,
                    "access": access,
                    "tag": tag,
                },
                repository_update_publishing_params.RepositoryUpdatePublishingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryUpdatePublishingResponse,
        )


class AsyncRepositoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRepositoriesResourceWithRawResponse:
        return AsyncRepositoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRepositoriesResourceWithStreamingResponse:
        return AsyncRepositoriesResourceWithStreamingResponse(self)

    async def link(
        self,
        uid: str,
        *,
        language: Literal[
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
        ],
        repository_id: int,
        base_branch: str,
        prerelease_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryLinkResponse:
        """
        Link one language target to a GitHub repository, so builds sync there.

        Args:
            uid: Path parameter.
            language: Body parameter.
            repository_id: Body parameter.
            base_branch: Body parameter.
            prerelease_type: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryLinkResponse: Default Response

        Example:
            ```python
            repository = await client.sdks.repositories.link(
                uid="UakgbKJ5m9gl0JDMbcJqL",
                language="typescript",
                repository_id=123456789,
                base_branch="main",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._post(
            path_template("/v1/sdks/{uid}/repositories", **{"uid": uid}),
            body=await async_maybe_transform(
                {
                    "language": language,
                    "repository_id": repository_id,
                    "base_branch": base_branch,
                    "prerelease_type": prerelease_type,
                },
                repository_link_params.RepositoryLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryLinkResponse,
        )

    async def unlink(
        self,
        language: Literal[
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
        ],
        *,
        uid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryUnlinkResponse:
        """
        Unlink one language target from its repository.

        Args:
            language: Path parameter.
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryUnlinkResponse: Default Response

        Example:
            ```python
            repository = await client.sdks.repositories.unlink(
                uid="UakgbKJ5m9gl0JDMbcJqL",
                language="typescript",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if language is None or (isinstance(language, str) and not language):
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return await self._delete(
            path_template("/v1/sdks/{uid}/repositories/{language}", **{"uid": uid, "language": language}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryUnlinkResponse,
        )

    async def update_publishing(
        self,
        language: Literal[
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
        ],
        *,
        uid: str,
        publish_on_merge: bool,
        auth_method: Literal["oidc", "access-token"] | Omit = omit,
        access: Literal["public", "restricted"] | Omit = omit,
        tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepositoryUpdatePublishingResponse:
        """
        Toggle publish-on-merge and the release settings for a linked target.

        Args:
            language: Path parameter.
            uid: Path parameter.
            publish_on_merge: Body parameter.
            auth_method: Body parameter.
            access: Body parameter.
            tag: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepositoryUpdatePublishingResponse: Default Response

        Example:
            ```python
            repository = await client.sdks.repositories.update_publishing(
                uid="UakgbKJ5m9gl0JDMbcJqL",
                language="typescript",
                publish_on_merge=True,
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        if language is None or (isinstance(language, str) and not language):
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return await self._post(
            path_template("/v1/sdks/{uid}/repositories/{language}/publishing", **{"uid": uid, "language": language}),
            body=await async_maybe_transform(
                {
                    "publish_on_merge": publish_on_merge,
                    "auth_method": auth_method,
                    "access": access,
                    "tag": tag,
                },
                repository_update_publishing_params.RepositoryUpdatePublishingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepositoryUpdatePublishingResponse,
        )


class RepositoriesResourceWithRawResponse:
    def __init__(self, repositories: RepositoriesResource) -> None:
        self._repositories = repositories

        self.link = to_raw_response_wrapper(
            repositories.link,
        )
        self.unlink = to_raw_response_wrapper(
            repositories.unlink,
        )
        self.update_publishing = to_raw_response_wrapper(
            repositories.update_publishing,
        )


class AsyncRepositoriesResourceWithRawResponse:
    def __init__(self, repositories: AsyncRepositoriesResource) -> None:
        self._repositories = repositories

        self.link = async_to_raw_response_wrapper(
            repositories.link,
        )
        self.unlink = async_to_raw_response_wrapper(
            repositories.unlink,
        )
        self.update_publishing = async_to_raw_response_wrapper(
            repositories.update_publishing,
        )


class RepositoriesResourceWithStreamingResponse:
    def __init__(self, repositories: RepositoriesResource) -> None:
        self._repositories = repositories

        self.link = to_streamed_response_wrapper(
            repositories.link,
        )
        self.unlink = to_streamed_response_wrapper(
            repositories.unlink,
        )
        self.update_publishing = to_streamed_response_wrapper(
            repositories.update_publishing,
        )


class AsyncRepositoriesResourceWithStreamingResponse:
    def __init__(self, repositories: AsyncRepositoriesResource) -> None:
        self._repositories = repositories

        self.link = async_to_streamed_response_wrapper(
            repositories.link,
        )
        self.unlink = async_to_streamed_response_wrapper(
            repositories.unlink,
        )
        self.update_publishing = async_to_streamed_response_wrapper(
            repositories.update_publishing,
        )
