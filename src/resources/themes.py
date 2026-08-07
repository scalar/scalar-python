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
from ..types.theme_list_response import ThemeListResponse
from ..types.theme_create_response import ThemeCreateResponse
from ..types import theme_create_params, theme_update_params, theme_replace_document_params
from ..types.theme_update_response import ThemeUpdateResponse
from ..types.theme_replace_document_response import ThemeReplaceDocumentResponse
from ..types.theme_delete_response import ThemeDeleteResponse

__all__ = ["ThemesResource", "AsyncThemesResource"]


class ThemesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ThemesResourceWithRawResponse:
        return ThemesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThemesResourceWithStreamingResponse:
        return ThemesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThemeListResponse:
        """
        List all team themes.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ThemeListResponse: Default Response

        Example:
            ```python
            theme = client.themes.list()
            ```
        """
        return self._get(
            "/v1/themes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThemeListResponse,
        )

    def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        slug: str,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThemeCreateResponse:
        """
        Create a team theme.

        Args:
            name: Body parameter.
            description: Body parameter.
            slug: Body parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ThemeCreateResponse: Default Response

        Example:
            ```python
            theme = client.themes.create(
                name="",
                slug="",
                document="",
            )
            ```
        """
        return self._post(
            "/v1/themes",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "slug": slug,
                    "document": document,
                },
                theme_create_params.ThemeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThemeCreateResponse,
        )

    def update(
        self,
        slug: str,
        *,
        name: str | Omit = omit,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThemeUpdateResponse:
        """
        Update theme metadata.

        Args:
            slug: Path parameter.
            name: Body parameter.
            description: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ThemeUpdateResponse: Default Response

        Example:
            ```python
            theme = client.themes.update(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._patch(
            path_template("/v1/themes/{slug}", **{"slug": slug}),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                theme_update_params.ThemeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThemeUpdateResponse,
        )

    def replace_document(
        self,
        slug: str,
        *,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThemeReplaceDocumentResponse:
        """
        Replace the theme document.

        Args:
            slug: Path parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ThemeReplaceDocumentResponse: Default Response

        Example:
            ```python
            theme = client.themes.replace_document(
                slug="slug",
                document="",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._put(
            path_template("/v1/themes/{slug}", **{"slug": slug}),
            body=maybe_transform(
                {"document": document},
                theme_replace_document_params.ThemeReplaceDocumentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThemeReplaceDocumentResponse,
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
    ) -> ThemeDeleteResponse:
        """
        Delete a theme by slug.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ThemeDeleteResponse: Default Response

        Example:
            ```python
            theme = client.themes.delete(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/themes/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThemeDeleteResponse,
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
    ) -> str:
        """
        Get the theme document by slug.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            str: Default Response

        Example:
            ```python
            theme = client.themes.retrieve(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            path_template("/v1/themes/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncThemesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncThemesResourceWithRawResponse:
        return AsyncThemesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThemesResourceWithStreamingResponse:
        return AsyncThemesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThemeListResponse:
        """
        List all team themes.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ThemeListResponse: Default Response

        Example:
            ```python
            theme = await client.themes.list()
            ```
        """
        return await self._get(
            "/v1/themes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThemeListResponse,
        )

    async def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        slug: str,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThemeCreateResponse:
        """
        Create a team theme.

        Args:
            name: Body parameter.
            description: Body parameter.
            slug: Body parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ThemeCreateResponse: Default Response

        Example:
            ```python
            theme = await client.themes.create(
                name="",
                slug="",
                document="",
            )
            ```
        """
        return await self._post(
            "/v1/themes",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "slug": slug,
                    "document": document,
                },
                theme_create_params.ThemeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThemeCreateResponse,
        )

    async def update(
        self,
        slug: str,
        *,
        name: str | Omit = omit,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThemeUpdateResponse:
        """
        Update theme metadata.

        Args:
            slug: Path parameter.
            name: Body parameter.
            description: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ThemeUpdateResponse: Default Response

        Example:
            ```python
            theme = await client.themes.update(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._patch(
            path_template("/v1/themes/{slug}", **{"slug": slug}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                theme_update_params.ThemeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThemeUpdateResponse,
        )

    async def replace_document(
        self,
        slug: str,
        *,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThemeReplaceDocumentResponse:
        """
        Replace the theme document.

        Args:
            slug: Path parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ThemeReplaceDocumentResponse: Default Response

        Example:
            ```python
            theme = await client.themes.replace_document(
                slug="slug",
                document="",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._put(
            path_template("/v1/themes/{slug}", **{"slug": slug}),
            body=await async_maybe_transform(
                {"document": document},
                theme_replace_document_params.ThemeReplaceDocumentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThemeReplaceDocumentResponse,
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
    ) -> ThemeDeleteResponse:
        """
        Delete a theme by slug.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ThemeDeleteResponse: Default Response

        Example:
            ```python
            theme = await client.themes.delete(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/themes/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThemeDeleteResponse,
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
    ) -> str:
        """
        Get the theme document by slug.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            str: Default Response

        Example:
            ```python
            theme = await client.themes.retrieve(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/themes/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class ThemesResourceWithRawResponse:
    def __init__(self, themes: ThemesResource) -> None:
        self._themes = themes

        self.list = to_raw_response_wrapper(
            themes.list,
        )
        self.create = to_raw_response_wrapper(
            themes.create,
        )
        self.update = to_raw_response_wrapper(
            themes.update,
        )
        self.replace_document = to_raw_response_wrapper(
            themes.replace_document,
        )
        self.delete = to_raw_response_wrapper(
            themes.delete,
        )
        self.retrieve = to_raw_response_wrapper(
            themes.retrieve,
        )


class AsyncThemesResourceWithRawResponse:
    def __init__(self, themes: AsyncThemesResource) -> None:
        self._themes = themes

        self.list = async_to_raw_response_wrapper(
            themes.list,
        )
        self.create = async_to_raw_response_wrapper(
            themes.create,
        )
        self.update = async_to_raw_response_wrapper(
            themes.update,
        )
        self.replace_document = async_to_raw_response_wrapper(
            themes.replace_document,
        )
        self.delete = async_to_raw_response_wrapper(
            themes.delete,
        )
        self.retrieve = async_to_raw_response_wrapper(
            themes.retrieve,
        )


class ThemesResourceWithStreamingResponse:
    def __init__(self, themes: ThemesResource) -> None:
        self._themes = themes

        self.list = to_streamed_response_wrapper(
            themes.list,
        )
        self.create = to_streamed_response_wrapper(
            themes.create,
        )
        self.update = to_streamed_response_wrapper(
            themes.update,
        )
        self.replace_document = to_streamed_response_wrapper(
            themes.replace_document,
        )
        self.delete = to_streamed_response_wrapper(
            themes.delete,
        )
        self.retrieve = to_streamed_response_wrapper(
            themes.retrieve,
        )


class AsyncThemesResourceWithStreamingResponse:
    def __init__(self, themes: AsyncThemesResource) -> None:
        self._themes = themes

        self.list = async_to_streamed_response_wrapper(
            themes.list,
        )
        self.create = async_to_streamed_response_wrapper(
            themes.create,
        )
        self.update = async_to_streamed_response_wrapper(
            themes.update,
        )
        self.replace_document = async_to_streamed_response_wrapper(
            themes.replace_document,
        )
        self.delete = async_to_streamed_response_wrapper(
            themes.delete,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            themes.retrieve,
        )
