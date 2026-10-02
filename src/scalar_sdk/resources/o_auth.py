# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.o_auth_oauth_authorize_response import OAuthOauthAuthorizeResponse
from ..types.o_auth_oauth_token_response import OAuthOauthTokenResponse
from ..types import o_auth_oauth_token_params, o_auth_oauth_revoke_params
from ..types.o_auth_oauth_revoke_response import OAuthOauthRevokeResponse
from ..types.oauth_authorization_server_metadata import OauthAuthorizationServerMetadata

__all__ = ["OAuthResource", "AsyncOAuthResource"]


class OAuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthResourceWithRawResponse:
        return OAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthResourceWithStreamingResponse:
        return OAuthResourceWithStreamingResponse(self)

    def oauth_authorize(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthOauthAuthorizeResponse:
        """
        Authorization endpoint (RFC 6749 §4.1.1 with PKCE, RFC 7636). Validates the request and sends the user to the Scalar dashboard to approve it; the user returns to `redirect_uri` with a `code` to exchange at the token endpoint. Only `response_type=code` with `code_challenge_method=S256` is supported.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OAuthOauthAuthorizeResponse: Default Response

        Example:
            ```python
            o_auth = client.o_auth.oauth_authorize()
            ```
        """
        return self._get(
            "/v1/oauth/authorize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthOauthAuthorizeResponse,
        )

    def oauth_token(
        self,
        *,
        grant_type: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        code: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        code_verifier: str | Omit = omit,
        refresh_token: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthOauthTokenResponse:
        """
        Token endpoint (RFC 6749 §4.1.3 and §6). Accepts `application/x-www-form-urlencoded`. Confidential clients authenticate with HTTP Basic or `client_secret` in the body; public clients send `client_id` alone. The `authorization_code` grant needs `code`, `redirect_uri` and `code_verifier`; the `refresh_token` grant needs `refresh_token` and may narrow `scope`.

        Args:
            grant_type: Body parameter.
            client_id: Body parameter.
            client_secret: Body parameter.
            code: Body parameter.
            redirect_uri: Body parameter.
            code_verifier: Body parameter.
            refresh_token: Body parameter.
            scope: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OAuthOauthTokenResponse: Default Response

        Example:
            ```python
            o_auth = client.o_auth.oauth_token(
                grant_type="",
            )
            ```
        """
        return self._post(
            "/v1/oauth/token",
            body=maybe_transform(
                {
                    "grant_type": grant_type,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code,
                    "redirect_uri": redirect_uri,
                    "code_verifier": code_verifier,
                    "refresh_token": refresh_token,
                    "scope": scope,
                },
                o_auth_oauth_token_params.OAuthOauthTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthOauthTokenResponse,
        )

    def oauth_revoke(
        self,
        *,
        token: str,
        token_type_hint: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthOauthRevokeResponse:
        """
        Revocation endpoint (RFC 7009). Revokes the refresh token and every token issued alongside it. The client authenticates as it does at the token endpoint. Responds 200 whether or not the token was live, as the RFC requires.

        Args:
            token: Body parameter.
            token_type_hint: Body parameter.
            client_id: Body parameter.
            client_secret: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OAuthOauthRevokeResponse: Default Response

        Example:
            ```python
            o_auth = client.o_auth.oauth_revoke(
                token="",
            )
            ```
        """
        return self._post(
            "/v1/oauth/revoke",
            body=maybe_transform(
                {
                    "token": token,
                    "token_type_hint": token_type_hint,
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                o_auth_oauth_revoke_params.OAuthOauthRevokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthOauthRevokeResponse,
        )

    def oauth_authorization_server_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OauthAuthorizationServerMetadata:
        """
        Discovery document for OAuth clients (RFC 8414): where the endpoints are and what they support.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OauthAuthorizationServerMetadata: Default Response

        Example:
            ```python
            o_auth = client.o_auth.oauth_authorization_server_metadata()
            ```
        """
        return self._get(
            "/.well-known/oauth-authorization-server",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OauthAuthorizationServerMetadata,
        )


class AsyncOAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthResourceWithRawResponse:
        return AsyncOAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthResourceWithStreamingResponse:
        return AsyncOAuthResourceWithStreamingResponse(self)

    async def oauth_authorize(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthOauthAuthorizeResponse:
        """
        Authorization endpoint (RFC 6749 §4.1.1 with PKCE, RFC 7636). Validates the request and sends the user to the Scalar dashboard to approve it; the user returns to `redirect_uri` with a `code` to exchange at the token endpoint. Only `response_type=code` with `code_challenge_method=S256` is supported.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OAuthOauthAuthorizeResponse: Default Response

        Example:
            ```python
            o_auth = await client.o_auth.oauth_authorize()
            ```
        """
        return await self._get(
            "/v1/oauth/authorize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthOauthAuthorizeResponse,
        )

    async def oauth_token(
        self,
        *,
        grant_type: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        code: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        code_verifier: str | Omit = omit,
        refresh_token: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthOauthTokenResponse:
        """
        Token endpoint (RFC 6749 §4.1.3 and §6). Accepts `application/x-www-form-urlencoded`. Confidential clients authenticate with HTTP Basic or `client_secret` in the body; public clients send `client_id` alone. The `authorization_code` grant needs `code`, `redirect_uri` and `code_verifier`; the `refresh_token` grant needs `refresh_token` and may narrow `scope`.

        Args:
            grant_type: Body parameter.
            client_id: Body parameter.
            client_secret: Body parameter.
            code: Body parameter.
            redirect_uri: Body parameter.
            code_verifier: Body parameter.
            refresh_token: Body parameter.
            scope: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OAuthOauthTokenResponse: Default Response

        Example:
            ```python
            o_auth = await client.o_auth.oauth_token(
                grant_type="",
            )
            ```
        """
        return await self._post(
            "/v1/oauth/token",
            body=await async_maybe_transform(
                {
                    "grant_type": grant_type,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code,
                    "redirect_uri": redirect_uri,
                    "code_verifier": code_verifier,
                    "refresh_token": refresh_token,
                    "scope": scope,
                },
                o_auth_oauth_token_params.OAuthOauthTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthOauthTokenResponse,
        )

    async def oauth_revoke(
        self,
        *,
        token: str,
        token_type_hint: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthOauthRevokeResponse:
        """
        Revocation endpoint (RFC 7009). Revokes the refresh token and every token issued alongside it. The client authenticates as it does at the token endpoint. Responds 200 whether or not the token was live, as the RFC requires.

        Args:
            token: Body parameter.
            token_type_hint: Body parameter.
            client_id: Body parameter.
            client_secret: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OAuthOauthRevokeResponse: Default Response

        Example:
            ```python
            o_auth = await client.o_auth.oauth_revoke(
                token="",
            )
            ```
        """
        return await self._post(
            "/v1/oauth/revoke",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "token_type_hint": token_type_hint,
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                o_auth_oauth_revoke_params.OAuthOauthRevokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthOauthRevokeResponse,
        )

    async def oauth_authorization_server_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OauthAuthorizationServerMetadata:
        """
        Discovery document for OAuth clients (RFC 8414): where the endpoints are and what they support.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OauthAuthorizationServerMetadata: Default Response

        Example:
            ```python
            o_auth = await client.o_auth.oauth_authorization_server_metadata()
            ```
        """
        return await self._get(
            "/.well-known/oauth-authorization-server",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OauthAuthorizationServerMetadata,
        )


class OAuthResourceWithRawResponse:
    def __init__(self, o_auth: OAuthResource) -> None:
        self._o_auth = o_auth

        self.oauth_authorize = to_raw_response_wrapper(
            o_auth.oauth_authorize,
        )
        self.oauth_token = to_raw_response_wrapper(
            o_auth.oauth_token,
        )
        self.oauth_revoke = to_raw_response_wrapper(
            o_auth.oauth_revoke,
        )
        self.oauth_authorization_server_metadata = to_raw_response_wrapper(
            o_auth.oauth_authorization_server_metadata,
        )


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, o_auth: AsyncOAuthResource) -> None:
        self._o_auth = o_auth

        self.oauth_authorize = async_to_raw_response_wrapper(
            o_auth.oauth_authorize,
        )
        self.oauth_token = async_to_raw_response_wrapper(
            o_auth.oauth_token,
        )
        self.oauth_revoke = async_to_raw_response_wrapper(
            o_auth.oauth_revoke,
        )
        self.oauth_authorization_server_metadata = async_to_raw_response_wrapper(
            o_auth.oauth_authorization_server_metadata,
        )


class OAuthResourceWithStreamingResponse:
    def __init__(self, o_auth: OAuthResource) -> None:
        self._o_auth = o_auth

        self.oauth_authorize = to_streamed_response_wrapper(
            o_auth.oauth_authorize,
        )
        self.oauth_token = to_streamed_response_wrapper(
            o_auth.oauth_token,
        )
        self.oauth_revoke = to_streamed_response_wrapper(
            o_auth.oauth_revoke,
        )
        self.oauth_authorization_server_metadata = to_streamed_response_wrapper(
            o_auth.oauth_authorization_server_metadata,
        )


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, o_auth: AsyncOAuthResource) -> None:
        self._o_auth = o_auth

        self.oauth_authorize = async_to_streamed_response_wrapper(
            o_auth.oauth_authorize,
        )
        self.oauth_token = async_to_streamed_response_wrapper(
            o_auth.oauth_token,
        )
        self.oauth_revoke = async_to_streamed_response_wrapper(
            o_auth.oauth_revoke,
        )
        self.oauth_authorization_server_metadata = async_to_streamed_response_wrapper(
            o_auth.oauth_authorization_server_metadata,
        )
