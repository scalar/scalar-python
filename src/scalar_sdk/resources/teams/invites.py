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
from ...types.teams.invite_member_response import InviteMemberResponse
from ...types.teams.email import Email
from ...types.teams.role import Role
from ...types.teams import invite_member_params
from ...types.teams.invite_resend_response import InviteResendResponse
from ...types.teams.invite_cancel_response import InviteCancelResponse

__all__ = ["InvitesResource", "AsyncInvitesResource"]


class InvitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvitesResourceWithRawResponse:
        return InvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitesResourceWithStreamingResponse:
        return InvitesResourceWithStreamingResponse(self)

    def member(
        self,
        *,
        email: Email,
        role: Role,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InviteMemberResponse:
        """
        Invite someone to the current team by email.

        Args:
            email: Body parameter.
            role: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InviteMemberResponse: Default Response

        Example:
            ```python
            invite = client.teams.invites.member(
                email="user@example.com",
                role="owner",
            )
            ```
        """
        return self._post(
            "/v1/teams/invites",
            body=maybe_transform(
                {
                    "email": email,
                    "role": role,
                },
                invite_member_params.InviteMemberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteMemberResponse,
        )

    def resend(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InviteResendResponse:
        """
        Send the invite email again.

        Args:
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InviteResendResponse: Default Response

        Example:
            ```python
            invite = client.teams.invites.resend(
                uid="uidxx",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._patch(
            path_template("/v1/teams/invites/{uid}", **{"uid": uid}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteResendResponse,
        )

    def cancel(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InviteCancelResponse:
        """
        Withdraw an invite that has not been accepted.

        Args:
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InviteCancelResponse: Default Response

        Example:
            ```python
            invite = client.teams.invites.cancel(
                uid="uidxx",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._delete(
            path_template("/v1/teams/invites/{uid}", **{"uid": uid}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteCancelResponse,
        )


class AsyncInvitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitesResourceWithRawResponse:
        return AsyncInvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitesResourceWithStreamingResponse:
        return AsyncInvitesResourceWithStreamingResponse(self)

    async def member(
        self,
        *,
        email: Email,
        role: Role,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InviteMemberResponse:
        """
        Invite someone to the current team by email.

        Args:
            email: Body parameter.
            role: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InviteMemberResponse: Default Response

        Example:
            ```python
            invite = await client.teams.invites.member(
                email="user@example.com",
                role="owner",
            )
            ```
        """
        return await self._post(
            "/v1/teams/invites",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "role": role,
                },
                invite_member_params.InviteMemberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteMemberResponse,
        )

    async def resend(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InviteResendResponse:
        """
        Send the invite email again.

        Args:
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InviteResendResponse: Default Response

        Example:
            ```python
            invite = await client.teams.invites.resend(
                uid="uidxx",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._patch(
            path_template("/v1/teams/invites/{uid}", **{"uid": uid}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteResendResponse,
        )

    async def cancel(
        self,
        uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InviteCancelResponse:
        """
        Withdraw an invite that has not been accepted.

        Args:
            uid: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InviteCancelResponse: Default Response

        Example:
            ```python
            invite = await client.teams.invites.cancel(
                uid="uidxx",
            )
            ```
        """
        if uid is None or (isinstance(uid, str) and not uid):
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._delete(
            path_template("/v1/teams/invites/{uid}", **{"uid": uid}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteCancelResponse,
        )


class InvitesResourceWithRawResponse:
    def __init__(self, invites: InvitesResource) -> None:
        self._invites = invites

        self.member = to_raw_response_wrapper(
            invites.member,
        )
        self.resend = to_raw_response_wrapper(
            invites.resend,
        )
        self.cancel = to_raw_response_wrapper(
            invites.cancel,
        )


class AsyncInvitesResourceWithRawResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
        self._invites = invites

        self.member = async_to_raw_response_wrapper(
            invites.member,
        )
        self.resend = async_to_raw_response_wrapper(
            invites.resend,
        )
        self.cancel = async_to_raw_response_wrapper(
            invites.cancel,
        )


class InvitesResourceWithStreamingResponse:
    def __init__(self, invites: InvitesResource) -> None:
        self._invites = invites

        self.member = to_streamed_response_wrapper(
            invites.member,
        )
        self.resend = to_streamed_response_wrapper(
            invites.resend,
        )
        self.cancel = to_streamed_response_wrapper(
            invites.cancel,
        )


class AsyncInvitesResourceWithStreamingResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
        self._invites = invites

        self.member = async_to_streamed_response_wrapper(
            invites.member,
        )
        self.resend = async_to_streamed_response_wrapper(
            invites.resend,
        )
        self.cancel = async_to_streamed_response_wrapper(
            invites.cancel,
        )
