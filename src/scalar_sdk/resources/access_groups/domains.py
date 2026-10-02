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
from ...types.access_groups.domain_create_response import DomainCreateResponse
from ...types.access_groups.email_domain import EmailDomain
from ...types.access_groups import domain_create_params, domain_delete_params
from ...types.access_groups.domain_delete_response import DomainDeleteResponse

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self)

    def create(
        self,
        slug: str,
        *,
        domain: EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainCreateResponse:
        """
        Allow an exact email domain in a group. Requires docs edit permission. A group supports up to 1000 domains.

        Args:
            slug: Path parameter.
            domain: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DomainCreateResponse: Default Response

        Example:
            ```python
            domain = client.access_groups.domains.create(
                slug="slug",
                domain="",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/v1/access-groups/{slug}/domains", **{"slug": slug}),
            body=maybe_transform(
                {"domain": domain},
                domain_create_params.DomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainCreateResponse,
        )

    def delete(
        self,
        slug: str,
        *,
        domain: EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainDeleteResponse:
        """
        Remove an exact email domain from a group. Requires docs edit permission. Other allowed domains and emails are preserved.

        Args:
            slug: Path parameter.
            domain: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DomainDeleteResponse: Default Response

        Example:
            ```python
            domain = client.access_groups.domains.delete(
                slug="slug",
                domain="",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/access-groups/{slug}/domains", **{"slug": slug}),
            body=maybe_transform(
                {"domain": domain},
                domain_delete_params.DomainDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainDeleteResponse,
        )


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self)

    async def create(
        self,
        slug: str,
        *,
        domain: EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainCreateResponse:
        """
        Allow an exact email domain in a group. Requires docs edit permission. A group supports up to 1000 domains.

        Args:
            slug: Path parameter.
            domain: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DomainCreateResponse: Default Response

        Example:
            ```python
            domain = await client.access_groups.domains.create(
                slug="slug",
                domain="",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/v1/access-groups/{slug}/domains", **{"slug": slug}),
            body=await async_maybe_transform(
                {"domain": domain},
                domain_create_params.DomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainCreateResponse,
        )

    async def delete(
        self,
        slug: str,
        *,
        domain: EmailDomain,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainDeleteResponse:
        """
        Remove an exact email domain from a group. Requires docs edit permission. Other allowed domains and emails are preserved.

        Args:
            slug: Path parameter.
            domain: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DomainDeleteResponse: Default Response

        Example:
            ```python
            domain = await client.access_groups.domains.delete(
                slug="slug",
                domain="",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/access-groups/{slug}/domains", **{"slug": slug}),
            body=await async_maybe_transform(
                {"domain": domain},
                domain_delete_params.DomainDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainDeleteResponse,
        )


class DomainsResourceWithRawResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.create = to_raw_response_wrapper(
            domains.create,
        )
        self.delete = to_raw_response_wrapper(
            domains.delete,
        )


class AsyncDomainsResourceWithRawResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.create = async_to_raw_response_wrapper(
            domains.create,
        )
        self.delete = async_to_raw_response_wrapper(
            domains.delete,
        )


class DomainsResourceWithStreamingResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.create = to_streamed_response_wrapper(
            domains.create,
        )
        self.delete = to_streamed_response_wrapper(
            domains.delete,
        )


class AsyncDomainsResourceWithStreamingResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.create = async_to_streamed_response_wrapper(
            domains.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            domains.delete,
        )
