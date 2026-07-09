# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import SequenceNotStr

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
from ..types.scalar_doc_list_guides_response import ScalarDocListGuidesResponse, GithubProject, ActiveDeployment, GithubProjectRepository
from ..types.scalar_doc_create_guide_response import ScalarDocCreateGuideResponse
from ..types.slug import Slug
from ..types import scalar_doc_create_guide_params
from ..types.scalar_doc_publish_guide_response import ScalarDocPublishGuideResponse

__all__ = ["ScalarDocsResource", "AsyncScalarDocsResource"]


class ScalarDocsResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> ScalarDocsResourceWithRawResponse:
        return ScalarDocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScalarDocsResourceWithStreamingResponse:
        return ScalarDocsResourceWithStreamingResponse(self)

    def list_guides(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocListGuidesResponse:
        """
        List all guide projects.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ScalarDocListGuidesResponse: Default Response
        
        Example:
            ```python
            scalar_doc = client.scalar_docs.list_guides()
            ```
        """
        return self._get(
            "/v1/guides",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ScalarDocListGuidesResponse,
        )

    def create_guide(
        self,
        *,
        name: str,
        slug: Slug | Omit = omit,
        is_private: bool,
        allowed_users: SequenceNotStr[str],
        allowed_domains: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocCreateGuideResponse:
        """
        Create a guide project.
        
        Args:
            name: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            allowed_users: Body parameter.
            allowed_domains: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ScalarDocCreateGuideResponse: Default Response
        
        Example:
            ```python
            scalar_doc = client.scalar_docs.create_guide(
                name="",
                is_private=False,
                allowed_users=[],
                allowed_domains=[],
            )
            ```
        """
        return self._post(
            "/v1/guides",
            body=maybe_transform(
            {
            "name": name,
            "slug": slug,
            "is_private": is_private,
            "allowed_users": allowed_users,
            "allowed_domains": allowed_domains,
        },
            scalar_doc_create_guide_params.ScalarDocCreateGuideParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ScalarDocCreateGuideResponse,
        )

    def publish_guide(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocPublishGuideResponse:
        """
        Start a new publish process.
        
        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ScalarDocPublishGuideResponse: Default Response
        
        Example:
            ```python
            scalar_doc = client.scalar_docs.publish_guide(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/v1/guides/{slug}/publish", **{"slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ScalarDocPublishGuideResponse,
        )


class AsyncScalarDocsResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncScalarDocsResourceWithRawResponse:
        return AsyncScalarDocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScalarDocsResourceWithStreamingResponse:
        return AsyncScalarDocsResourceWithStreamingResponse(self)

    async def list_guides(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocListGuidesResponse:
        """
        List all guide projects.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ScalarDocListGuidesResponse: Default Response
        
        Example:
            ```python
            scalar_doc = await client.scalar_docs.list_guides()
            ```
        """
        return await self._get(
            "/v1/guides",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ScalarDocListGuidesResponse,
        )

    async def create_guide(
        self,
        *,
        name: str,
        slug: Slug | Omit = omit,
        is_private: bool,
        allowed_users: SequenceNotStr[str],
        allowed_domains: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocCreateGuideResponse:
        """
        Create a guide project.
        
        Args:
            name: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            allowed_users: Body parameter.
            allowed_domains: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ScalarDocCreateGuideResponse: Default Response
        
        Example:
            ```python
            scalar_doc = await client.scalar_docs.create_guide(
                name="",
                is_private=False,
                allowed_users=[],
                allowed_domains=[],
            )
            ```
        """
        return await self._post(
            "/v1/guides",
            body=await async_maybe_transform(
            {
            "name": name,
            "slug": slug,
            "is_private": is_private,
            "allowed_users": allowed_users,
            "allowed_domains": allowed_domains,
        },
            scalar_doc_create_guide_params.ScalarDocCreateGuideParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ScalarDocCreateGuideResponse,
        )

    async def publish_guide(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocPublishGuideResponse:
        """
        Start a new publish process.
        
        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ScalarDocPublishGuideResponse: Default Response
        
        Example:
            ```python
            scalar_doc = await client.scalar_docs.publish_guide(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/v1/guides/{slug}/publish", **{"slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ScalarDocPublishGuideResponse,
        )


class ScalarDocsResourceWithRawResponse:
    def __init__(self, scalar_docs: ScalarDocsResource) -> None:
        self._scalar_docs = scalar_docs

        self.list_guides = to_raw_response_wrapper(
            scalar_docs.list_guides,
        )
        self.create_guide = to_raw_response_wrapper(
            scalar_docs.create_guide,
        )
        self.publish_guide = to_raw_response_wrapper(
            scalar_docs.publish_guide,
        )


class AsyncScalarDocsResourceWithRawResponse:
    def __init__(self, scalar_docs: AsyncScalarDocsResource) -> None:
        self._scalar_docs = scalar_docs

        self.list_guides = async_to_raw_response_wrapper(
            scalar_docs.list_guides,
        )
        self.create_guide = async_to_raw_response_wrapper(
            scalar_docs.create_guide,
        )
        self.publish_guide = async_to_raw_response_wrapper(
            scalar_docs.publish_guide,
        )


class ScalarDocsResourceWithStreamingResponse:
    def __init__(self, scalar_docs: ScalarDocsResource) -> None:
        self._scalar_docs = scalar_docs

        self.list_guides = to_streamed_response_wrapper(
            scalar_docs.list_guides,
        )
        self.create_guide = to_streamed_response_wrapper(
            scalar_docs.create_guide,
        )
        self.publish_guide = to_streamed_response_wrapper(
            scalar_docs.publish_guide,
        )


class AsyncScalarDocsResourceWithStreamingResponse:
    def __init__(self, scalar_docs: AsyncScalarDocsResource) -> None:
        self._scalar_docs = scalar_docs

        self.list_guides = async_to_streamed_response_wrapper(
            scalar_docs.list_guides,
        )
        self.create_guide = async_to_streamed_response_wrapper(
            scalar_docs.create_guide,
        )
        self.publish_guide = async_to_streamed_response_wrapper(
            scalar_docs.publish_guide,
        )
