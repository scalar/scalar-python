# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.login_portal_retrieve_response import LoginPortalRetrieveResponse
from ..types.login_portal_update_response import LoginPortalUpdateResponse
from ..types import login_portal_update_params
from ..types.login_portal_delete_response import LoginPortalDeleteResponse
from ..types.login_portal_create_response import LoginPortalCreateResponse
from ..types.login_portal_email import LoginPortalEmail
from ..types.login_portal_page import LoginPortalPage
from ..types import login_portal_create_params
from ..types.login_portal_list_response import LoginPortalListResponse, LoginPortal

__all__ = ["LoginPortalsResource", "AsyncLoginPortalsResource"]


class LoginPortalsResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> LoginPortalsResourceWithRawResponse:
        return LoginPortalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoginPortalsResourceWithStreamingResponse:
        return LoginPortalsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginPortalRetrieveResponse:
        """
        Get a login portal by slug.
        
        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            LoginPortalRetrieveResponse: Default Response
        
        Example:
            ```python
            login_portal = client.login_portals.retrieve(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/v1/login-portals/{slug}", **{"slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LoginPortalRetrieveResponse,
        )

    def update(
        self,
        slug: str,
        *,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginPortalUpdateResponse:
        """
        Update metadata for a login portal.
        
        Args:
            slug: Path parameter.
            title: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            LoginPortalUpdateResponse: Default Response
        
        Example:
            ```python
            login_portal = client.login_portals.update(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._patch(
            path_template("/v1/login-portals/{slug}", **{"slug": slug}),
            body=maybe_transform(
            {"title": title},
            login_portal_update_params.LoginPortalUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LoginPortalUpdateResponse,
        )

    def delete(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginPortalDeleteResponse:
        """
        Delete a login portal.
        
        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            LoginPortalDeleteResponse: Default Response
        
        Example:
            ```python
            login_portal = client.login_portals.delete(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/login-portals/{slug}", **{"slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LoginPortalDeleteResponse,
        )

    def create(
        self,
        *,
        title: str,
        slug: str,
        email: LoginPortalEmail,
        page: LoginPortalPage,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginPortalCreateResponse:
        """
        Create a login portal for the current team.
        
        Args:
            title: Body parameter.
            slug: Body parameter.
            email: Body parameter.
            page: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            LoginPortalCreateResponse: Default Response
        
        Example:
            ```python
            login_portal = client.login_portals.create(
                title="",
                slug="",
                email={"logo": "", "logo_size": "100", "button_text": "Login", "message": "Click to access private documentation hosted by scalar.com", "title": "Private Docs", "main_color": "#2a2f45", "main_background": "#f6f6f6", "card_color": "2a2f45", "card_background": "#fff", "button_color": "#fff", "button_background": "#0f0f0f"},
                page={"title": "Scalar Private Docs", "description": "Login to access your documentation", "head": "", "script": "", "theme": "", "company_name": "", "logo": "", "logo_url": "", "favicon": "", "terms_link": "", "privacy_link": "", "form_title": "Scalar Private Docs", "form_description": "Login to access your documentation", "form_image": ""},
            )
            ```
        """
        return self._post(
            "/v1/login-portals",
            body=maybe_transform(
            {
            "title": title,
            "slug": slug,
            "email": email,
            "page": page,
        },
            login_portal_create_params.LoginPortalCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LoginPortalCreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginPortalListResponse:
        """
        List all login portals for the current team.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            LoginPortalListResponse: Default Response
        
        Example:
            ```python
            login_portal = client.login_portals.list()
            ```
        """
        return self._get(
            "/v1/login-portals",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LoginPortalListResponse,
        )


class AsyncLoginPortalsResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncLoginPortalsResourceWithRawResponse:
        return AsyncLoginPortalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoginPortalsResourceWithStreamingResponse:
        return AsyncLoginPortalsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginPortalRetrieveResponse:
        """
        Get a login portal by slug.
        
        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            LoginPortalRetrieveResponse: Default Response
        
        Example:
            ```python
            login_portal = await client.login_portals.retrieve(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/v1/login-portals/{slug}", **{"slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LoginPortalRetrieveResponse,
        )

    async def update(
        self,
        slug: str,
        *,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginPortalUpdateResponse:
        """
        Update metadata for a login portal.
        
        Args:
            slug: Path parameter.
            title: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            LoginPortalUpdateResponse: Default Response
        
        Example:
            ```python
            login_portal = await client.login_portals.update(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._patch(
            path_template("/v1/login-portals/{slug}", **{"slug": slug}),
            body=await async_maybe_transform(
            {"title": title},
            login_portal_update_params.LoginPortalUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LoginPortalUpdateResponse,
        )

    async def delete(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginPortalDeleteResponse:
        """
        Delete a login portal.
        
        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            LoginPortalDeleteResponse: Default Response
        
        Example:
            ```python
            login_portal = await client.login_portals.delete(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/login-portals/{slug}", **{"slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LoginPortalDeleteResponse,
        )

    async def create(
        self,
        *,
        title: str,
        slug: str,
        email: LoginPortalEmail,
        page: LoginPortalPage,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginPortalCreateResponse:
        """
        Create a login portal for the current team.
        
        Args:
            title: Body parameter.
            slug: Body parameter.
            email: Body parameter.
            page: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            LoginPortalCreateResponse: Default Response
        
        Example:
            ```python
            login_portal = await client.login_portals.create(
                title="",
                slug="",
                email={"logo": "", "logo_size": "100", "button_text": "Login", "message": "Click to access private documentation hosted by scalar.com", "title": "Private Docs", "main_color": "#2a2f45", "main_background": "#f6f6f6", "card_color": "2a2f45", "card_background": "#fff", "button_color": "#fff", "button_background": "#0f0f0f"},
                page={"title": "Scalar Private Docs", "description": "Login to access your documentation", "head": "", "script": "", "theme": "", "company_name": "", "logo": "", "logo_url": "", "favicon": "", "terms_link": "", "privacy_link": "", "form_title": "Scalar Private Docs", "form_description": "Login to access your documentation", "form_image": ""},
            )
            ```
        """
        return await self._post(
            "/v1/login-portals",
            body=await async_maybe_transform(
            {
            "title": title,
            "slug": slug,
            "email": email,
            "page": page,
        },
            login_portal_create_params.LoginPortalCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LoginPortalCreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginPortalListResponse:
        """
        List all login portals for the current team.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            LoginPortalListResponse: Default Response
        
        Example:
            ```python
            login_portal = await client.login_portals.list()
            ```
        """
        return await self._get(
            "/v1/login-portals",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LoginPortalListResponse,
        )


class LoginPortalsResourceWithRawResponse:
    def __init__(self, login_portals: LoginPortalsResource) -> None:
        self._login_portals = login_portals

        self.retrieve = to_raw_response_wrapper(
            login_portals.retrieve,
        )
        self.update = to_raw_response_wrapper(
            login_portals.update,
        )
        self.delete = to_raw_response_wrapper(
            login_portals.delete,
        )
        self.create = to_raw_response_wrapper(
            login_portals.create,
        )
        self.list = to_raw_response_wrapper(
            login_portals.list,
        )


class AsyncLoginPortalsResourceWithRawResponse:
    def __init__(self, login_portals: AsyncLoginPortalsResource) -> None:
        self._login_portals = login_portals

        self.retrieve = async_to_raw_response_wrapper(
            login_portals.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            login_portals.update,
        )
        self.delete = async_to_raw_response_wrapper(
            login_portals.delete,
        )
        self.create = async_to_raw_response_wrapper(
            login_portals.create,
        )
        self.list = async_to_raw_response_wrapper(
            login_portals.list,
        )


class LoginPortalsResourceWithStreamingResponse:
    def __init__(self, login_portals: LoginPortalsResource) -> None:
        self._login_portals = login_portals

        self.retrieve = to_streamed_response_wrapper(
            login_portals.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            login_portals.update,
        )
        self.delete = to_streamed_response_wrapper(
            login_portals.delete,
        )
        self.create = to_streamed_response_wrapper(
            login_portals.create,
        )
        self.list = to_streamed_response_wrapper(
            login_portals.list,
        )


class AsyncLoginPortalsResourceWithStreamingResponse:
    def __init__(self, login_portals: AsyncLoginPortalsResource) -> None:
        self._login_portals = login_portals

        self.retrieve = async_to_streamed_response_wrapper(
            login_portals.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            login_portals.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            login_portals.delete,
        )
        self.create = async_to_streamed_response_wrapper(
            login_portals.create,
        )
        self.list = async_to_streamed_response_wrapper(
            login_portals.list,
        )
