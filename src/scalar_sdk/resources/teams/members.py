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
from ...types.teams.member_list_response import MemberListResponse
from ...types.teams.member_update_response import MemberUpdateResponse
from ...types.teams.role import Role
from ...types.teams import member_update_params
from ...types.teams.member_delete_response import MemberDeleteResponse

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListResponse:
        """
        List the members of the current team, along with the invites still outstanding.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberListResponse: Default Response

        Example:
            ```python
            member = client.teams.members.list()
            ```
        """
        return self._get(
            "/v1/teams/members",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListResponse,
        )

    def update(
        self,
        uid: str,
        *,
        role: Role,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberUpdateResponse:
        """
        Change what a member of the current team is allowed to do.

        Args:
            uid: Path parameter.
            role: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberUpdateResponse: Default Response

        Example:
            ```python
            member = client.teams.members.update(
                uid="UakgbKJ5m9gl0JDMbcJqL",
                role="owner",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._patch(
            path_template("/v1/teams/members/{uid}", **{"uid": uid}),
            body=maybe_transform(
                {"role": role},
                member_update_params.MemberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberUpdateResponse,
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
    ) -> MemberDeleteResponse:
        """
        Remove someone from the current team.

        Args:
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberDeleteResponse: Default Response

        Example:
            ```python
            member = client.teams.members.delete(
                uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._delete(
            path_template("/v1/teams/members/{uid}", **{"uid": uid}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberDeleteResponse,
        )


class AsyncMembersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListResponse:
        """
        List the members of the current team, along with the invites still outstanding.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberListResponse: Default Response

        Example:
            ```python
            member = await client.teams.members.list()
            ```
        """
        return await self._get(
            "/v1/teams/members",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListResponse,
        )

    async def update(
        self,
        uid: str,
        *,
        role: Role,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberUpdateResponse:
        """
        Change what a member of the current team is allowed to do.

        Args:
            uid: Path parameter.
            role: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberUpdateResponse: Default Response

        Example:
            ```python
            member = await client.teams.members.update(
                uid="UakgbKJ5m9gl0JDMbcJqL",
                role="owner",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._patch(
            path_template("/v1/teams/members/{uid}", **{"uid": uid}),
            body=await async_maybe_transform(
                {"role": role},
                member_update_params.MemberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberUpdateResponse,
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
    ) -> MemberDeleteResponse:
        """
        Remove someone from the current team.

        Args:
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MemberDeleteResponse: Default Response

        Example:
            ```python
            member = await client.teams.members.delete(
                uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._delete(
            path_template("/v1/teams/members/{uid}", **{"uid": uid}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberDeleteResponse,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_raw_response_wrapper(
            members.list,
        )
        self.update = to_raw_response_wrapper(
            members.update,
        )
        self.delete = to_raw_response_wrapper(
            members.delete,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_raw_response_wrapper(
            members.list,
        )
        self.update = async_to_raw_response_wrapper(
            members.update,
        )
        self.delete = async_to_raw_response_wrapper(
            members.delete,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_streamed_response_wrapper(
            members.list,
        )
        self.update = to_streamed_response_wrapper(
            members.update,
        )
        self.delete = to_streamed_response_wrapper(
            members.delete,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_streamed_response_wrapper(
            members.list,
        )
        self.update = async_to_streamed_response_wrapper(
            members.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            members.delete,
        )
