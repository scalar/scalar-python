# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.authentication_exchange_personal_token_response import AuthenticationExchangePersonalTokenResponse
from ..types import authentication_exchange_personal_token_params
from ..types.authentication_list_current_user_response import AuthenticationListCurrentUserResponse

__all__ = ["AuthenticationResource", "AsyncAuthenticationResource"]


class AuthenticationResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AuthenticationResourceWithRawResponse:
        return AuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticationResourceWithStreamingResponse:
        return AuthenticationResourceWithStreamingResponse(self)

    def exchange_personal_token(
        self,
        *,
        personal_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticationExchangePersonalTokenResponse:
        """
        Exchange an API key for an access token.
        
        Args:
            personal_token: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AuthenticationExchangePersonalTokenResponse: Default Response
        
        Example:
            ```python
            authentication = client.authentication.exchange_personal_token(
                personal_token="",
            )
            ```
        """
        return self._post(
            "/v1/auth/exchange",
            body=maybe_transform(
            {"personal_token": personal_token},
            authentication_exchange_personal_token_params.AuthenticationExchangePersonalTokenParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AuthenticationExchangePersonalTokenResponse,
        )

    def list_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticationListCurrentUserResponse:
        """
        Get the authenticated user, including their available teams and theme.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AuthenticationListCurrentUserResponse: Default Response
        
        Example:
            ```python
            authentication = client.authentication.list_current_user()
            ```
        """
        return self._get(
            "/v1/auth/me",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AuthenticationListCurrentUserResponse,
        )


class AsyncAuthenticationResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncAuthenticationResourceWithRawResponse:
        return AsyncAuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticationResourceWithStreamingResponse:
        return AsyncAuthenticationResourceWithStreamingResponse(self)

    async def exchange_personal_token(
        self,
        *,
        personal_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticationExchangePersonalTokenResponse:
        """
        Exchange an API key for an access token.
        
        Args:
            personal_token: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AuthenticationExchangePersonalTokenResponse: Default Response
        
        Example:
            ```python
            authentication = await client.authentication.exchange_personal_token(
                personal_token="",
            )
            ```
        """
        return await self._post(
            "/v1/auth/exchange",
            body=await async_maybe_transform(
            {"personal_token": personal_token},
            authentication_exchange_personal_token_params.AuthenticationExchangePersonalTokenParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AuthenticationExchangePersonalTokenResponse,
        )

    async def list_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticationListCurrentUserResponse:
        """
        Get the authenticated user, including their available teams and theme.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AuthenticationListCurrentUserResponse: Default Response
        
        Example:
            ```python
            authentication = await client.authentication.list_current_user()
            ```
        """
        return await self._get(
            "/v1/auth/me",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AuthenticationListCurrentUserResponse,
        )


class AuthenticationResourceWithRawResponse:
    def __init__(self, authentication: AuthenticationResource) -> None:
        self._authentication = authentication

        self.exchange_personal_token = to_raw_response_wrapper(
            authentication.exchange_personal_token,
        )
        self.list_current_user = to_raw_response_wrapper(
            authentication.list_current_user,
        )


class AsyncAuthenticationResourceWithRawResponse:
    def __init__(self, authentication: AsyncAuthenticationResource) -> None:
        self._authentication = authentication

        self.exchange_personal_token = async_to_raw_response_wrapper(
            authentication.exchange_personal_token,
        )
        self.list_current_user = async_to_raw_response_wrapper(
            authentication.list_current_user,
        )


class AuthenticationResourceWithStreamingResponse:
    def __init__(self, authentication: AuthenticationResource) -> None:
        self._authentication = authentication

        self.exchange_personal_token = to_streamed_response_wrapper(
            authentication.exchange_personal_token,
        )
        self.list_current_user = to_streamed_response_wrapper(
            authentication.list_current_user,
        )


class AsyncAuthenticationResourceWithStreamingResponse:
    def __init__(self, authentication: AsyncAuthenticationResource) -> None:
        self._authentication = authentication

        self.exchange_personal_token = async_to_streamed_response_wrapper(
            authentication.exchange_personal_token,
        )
        self.list_current_user = async_to_streamed_response_wrapper(
            authentication.list_current_user,
        )
