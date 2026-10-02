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
from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from ...types.access_group_create_response import AccessGroupCreateResponse
from ...types.access_group_name import AccessGroupName
from ...types.slug import Slug
from ...types import access_group_create_params, access_group_update_params
from ...types.access_group_retrieve_response import AccessGroupRetrieveResponse
from ...types.access_group_update_response import AccessGroupUpdateResponse
from ...types.access_group_delete_response import AccessGroupDeleteResponse

__all__ = ["AccessGroupsResource", "AsyncAccessGroupsResource"]


class AccessGroupsResource(SyncAPIResource):
    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccessGroupsResourceWithRawResponse:
        return AccessGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessGroupsResourceWithStreamingResponse:
        return AccessGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: AccessGroupName | Omit = omit,
        slug: Slug | Omit = omit,
        allowed_domains: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessGroupCreateResponse:
        """
        Create a group for the current team. Requires docs edit permission and the access groups billing feature. Domains are exact email domains, without wildcards or implicit subdomain matching.

        Args:
            name: Body parameter.
            slug: Body parameter.
            allowed_domains: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccessGroupCreateResponse: Default Response

        Example:
            ```python
            access_group = client.access_groups.create()
            ```
        """
        return self._post(
            "/v1/access-groups",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "allowed_domains": allowed_domains,
                },
                access_group_create_params.AccessGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupCreateResponse,
        )

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
    ) -> AccessGroupRetrieveResponse:
        """
        Get a group and its email and domain allowlists by slug.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccessGroupRetrieveResponse: Default Response

        Example:
            ```python
            access_group = client.access_groups.retrieve(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/v1/access-groups/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupRetrieveResponse,
        )

    def update(
        self,
        path_slug: str,
        *,
        name: AccessGroupName | Omit = omit,
        body_slug: Slug | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessGroupUpdateResponse:
        """
        Update group metadata. Requires docs edit permission. After changing the slug, use the new slug in subsequent requests.

        Args:
            path_slug: Path parameter.
            name: Body parameter.
            body_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccessGroupUpdateResponse: Default Response

        Example:
            ```python
            access_group = client.access_groups.update(
                path_slug="slug",
            )
            ```
        """
        if path_slug is None or (isinstance(path_slug, str) and not path_slug):
            raise ValueError(f"Expected a non-empty value for `path_slug` but received {path_slug!r}")
        return self._patch(
            path_template("/v1/access-groups/{slug}", **{"slug": path_slug}),
            body=maybe_transform(
                {
                    "name": name,
                    "body_slug": body_slug,
                },
                access_group_update_params.AccessGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupUpdateResponse,
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
    ) -> AccessGroupDeleteResponse:
        """
        Delete a group and remove its project assignments. Requires docs edit permission.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccessGroupDeleteResponse: Default Response

        Example:
            ```python
            access_group = client.access_groups.delete(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/access-groups/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupDeleteResponse,
        )


class AsyncAccessGroupsResource(AsyncAPIResource):
    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccessGroupsResourceWithRawResponse:
        return AsyncAccessGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessGroupsResourceWithStreamingResponse:
        return AsyncAccessGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: AccessGroupName | Omit = omit,
        slug: Slug | Omit = omit,
        allowed_domains: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessGroupCreateResponse:
        """
        Create a group for the current team. Requires docs edit permission and the access groups billing feature. Domains are exact email domains, without wildcards or implicit subdomain matching.

        Args:
            name: Body parameter.
            slug: Body parameter.
            allowed_domains: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccessGroupCreateResponse: Default Response

        Example:
            ```python
            access_group = await client.access_groups.create()
            ```
        """
        return await self._post(
            "/v1/access-groups",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "allowed_domains": allowed_domains,
                },
                access_group_create_params.AccessGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupCreateResponse,
        )

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
    ) -> AccessGroupRetrieveResponse:
        """
        Get a group and its email and domain allowlists by slug.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccessGroupRetrieveResponse: Default Response

        Example:
            ```python
            access_group = await client.access_groups.retrieve(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/v1/access-groups/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupRetrieveResponse,
        )

    async def update(
        self,
        path_slug: str,
        *,
        name: AccessGroupName | Omit = omit,
        body_slug: Slug | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessGroupUpdateResponse:
        """
        Update group metadata. Requires docs edit permission. After changing the slug, use the new slug in subsequent requests.

        Args:
            path_slug: Path parameter.
            name: Body parameter.
            body_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccessGroupUpdateResponse: Default Response

        Example:
            ```python
            access_group = await client.access_groups.update(
                path_slug="slug",
            )
            ```
        """
        if path_slug is None or (isinstance(path_slug, str) and not path_slug):
            raise ValueError(f"Expected a non-empty value for `path_slug` but received {path_slug!r}")
        return await self._patch(
            path_template("/v1/access-groups/{slug}", **{"slug": path_slug}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "body_slug": body_slug,
                },
                access_group_update_params.AccessGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupUpdateResponse,
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
    ) -> AccessGroupDeleteResponse:
        """
        Delete a group and remove its project assignments. Requires docs edit permission.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccessGroupDeleteResponse: Default Response

        Example:
            ```python
            access_group = await client.access_groups.delete(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/access-groups/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessGroupDeleteResponse,
        )


class AccessGroupsResourceWithRawResponse:
    def __init__(self, access_groups: AccessGroupsResource) -> None:
        self._access_groups = access_groups

        self.create = to_raw_response_wrapper(
            access_groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            access_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            access_groups.update,
        )
        self.delete = to_raw_response_wrapper(
            access_groups.delete,
        )

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._access_groups.domains)


class AsyncAccessGroupsResourceWithRawResponse:
    def __init__(self, access_groups: AsyncAccessGroupsResource) -> None:
        self._access_groups = access_groups

        self.create = async_to_raw_response_wrapper(
            access_groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            access_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            access_groups.update,
        )
        self.delete = async_to_raw_response_wrapper(
            access_groups.delete,
        )

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._access_groups.domains)


class AccessGroupsResourceWithStreamingResponse:
    def __init__(self, access_groups: AccessGroupsResource) -> None:
        self._access_groups = access_groups

        self.create = to_streamed_response_wrapper(
            access_groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            access_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            access_groups.update,
        )
        self.delete = to_streamed_response_wrapper(
            access_groups.delete,
        )

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._access_groups.domains)


class AsyncAccessGroupsResourceWithStreamingResponse:
    def __init__(self, access_groups: AsyncAccessGroupsResource) -> None:
        self._access_groups = access_groups

        self.create = async_to_streamed_response_wrapper(
            access_groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            access_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            access_groups.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            access_groups.delete,
        )

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._access_groups.domains)
