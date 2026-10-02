# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ...._types import SequenceNotStr

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .installations import (
    InstallationsResource,
    AsyncInstallationsResource,
    InstallationsResourceWithRawResponse,
    AsyncInstallationsResourceWithRawResponse,
    InstallationsResourceWithStreamingResponse,
    AsyncInstallationsResourceWithStreamingResponse,
)
from ....types.mcp.server_list_response import ServerListResponse
from ....types.mcp.server_create_response import ServerCreateResponse
from ....types.slug import Slug
from ....types.mcp import server_create_params, server_update_params
from ....types.mcp.mcp_server import McpServer
from ....types.mcp.server_delete_response import ServerDeleteResponse

__all__ = ["ServersResource", "AsyncServersResource"]


class ServersResource(SyncAPIResource):
    @cached_property
    def installations(self) -> InstallationsResource:
        return InstallationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ServersResourceWithRawResponse:
        return ServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServersResourceWithStreamingResponse:
        return ServersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerListResponse:
        """
        List every MCP server on the team.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ServerListResponse: Default Response

        Example:
            ```python
            server = client.mcp.servers.list()
            ```
        """
        return self._get(
            "/v1/mcp/servers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerListResponse,
        )

    def create(
        self,
        *,
        name: str,
        slug: Slug | Omit = omit,
        version_uids: SequenceNotStr[str] | Omit = omit,
        project_uids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerCreateResponse:
        """
        Create an MCP server over one or more API document versions. The response carries the server and its first installation.

        Args:
            name: Body parameter.
            slug: Body parameter.
            version_uids: Body parameter.
            project_uids: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ServerCreateResponse: Default Response

        Example:
            ```python
            server = client.mcp.servers.create(
                name="x",
            )
            ```
        """
        return self._post(
            "/v1/mcp/servers",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "version_uids": version_uids,
                    "project_uids": project_uids,
                },
                server_create_params.ServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServer:
        """
        Get a single MCP server by its id.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpServer: Default Response

        Example:
            ```python
            server = client.mcp.servers.retrieve(
                id="id",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/mcp/servers/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServer,
        )

    def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        slug: Slug | Omit = omit,
        auto_add_operations: bool | Omit = omit,
        operations: SequenceNotStr[str] | Omit = omit,
        docs_pages: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServer:
        """
        Update MCP server metadata and which tools it exposes.

        Args:
            id: Path parameter.
            name: Body parameter.
            slug: Body parameter.
            auto_add_operations: Body parameter.
            operations: Body parameter.
            docs_pages: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpServer: Default Response

        Example:
            ```python
            server = client.mcp.servers.update(
                id="id",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/mcp/servers/{id}", **{"id": id}),
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "auto_add_operations": auto_add_operations,
                    "operations": operations,
                    "docs_pages": docs_pages,
                },
                server_update_params.ServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServer,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerDeleteResponse:
        """
        Delete an MCP server and every installation it serves.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ServerDeleteResponse: Default Response

        Example:
            ```python
            server = client.mcp.servers.delete(
                id="id",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/v1/mcp/servers/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerDeleteResponse,
        )


class AsyncServersResource(AsyncAPIResource):
    @cached_property
    def installations(self) -> AsyncInstallationsResource:
        return AsyncInstallationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncServersResourceWithRawResponse:
        return AsyncServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServersResourceWithStreamingResponse:
        return AsyncServersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerListResponse:
        """
        List every MCP server on the team.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ServerListResponse: Default Response

        Example:
            ```python
            server = await client.mcp.servers.list()
            ```
        """
        return await self._get(
            "/v1/mcp/servers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerListResponse,
        )

    async def create(
        self,
        *,
        name: str,
        slug: Slug | Omit = omit,
        version_uids: SequenceNotStr[str] | Omit = omit,
        project_uids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerCreateResponse:
        """
        Create an MCP server over one or more API document versions. The response carries the server and its first installation.

        Args:
            name: Body parameter.
            slug: Body parameter.
            version_uids: Body parameter.
            project_uids: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ServerCreateResponse: Default Response

        Example:
            ```python
            server = await client.mcp.servers.create(
                name="x",
            )
            ```
        """
        return await self._post(
            "/v1/mcp/servers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "version_uids": version_uids,
                    "project_uids": project_uids,
                },
                server_create_params.ServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServer:
        """
        Get a single MCP server by its id.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpServer: Default Response

        Example:
            ```python
            server = await client.mcp.servers.retrieve(
                id="id",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/mcp/servers/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServer,
        )

    async def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        slug: Slug | Omit = omit,
        auto_add_operations: bool | Omit = omit,
        operations: SequenceNotStr[str] | Omit = omit,
        docs_pages: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServer:
        """
        Update MCP server metadata and which tools it exposes.

        Args:
            id: Path parameter.
            name: Body parameter.
            slug: Body parameter.
            auto_add_operations: Body parameter.
            operations: Body parameter.
            docs_pages: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpServer: Default Response

        Example:
            ```python
            server = await client.mcp.servers.update(
                id="id",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/mcp/servers/{id}", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "auto_add_operations": auto_add_operations,
                    "operations": operations,
                    "docs_pages": docs_pages,
                },
                server_update_params.ServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServer,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerDeleteResponse:
        """
        Delete an MCP server and every installation it serves.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ServerDeleteResponse: Default Response

        Example:
            ```python
            server = await client.mcp.servers.delete(
                id="id",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/v1/mcp/servers/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerDeleteResponse,
        )


class ServersResourceWithRawResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.list = to_raw_response_wrapper(
            servers.list,
        )
        self.create = to_raw_response_wrapper(
            servers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            servers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            servers.update,
        )
        self.delete = to_raw_response_wrapper(
            servers.delete,
        )

    @cached_property
    def installations(self) -> InstallationsResourceWithRawResponse:
        return InstallationsResourceWithRawResponse(self._servers.installations)


class AsyncServersResourceWithRawResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.list = async_to_raw_response_wrapper(
            servers.list,
        )
        self.create = async_to_raw_response_wrapper(
            servers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            servers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            servers.update,
        )
        self.delete = async_to_raw_response_wrapper(
            servers.delete,
        )

    @cached_property
    def installations(self) -> AsyncInstallationsResourceWithRawResponse:
        return AsyncInstallationsResourceWithRawResponse(self._servers.installations)


class ServersResourceWithStreamingResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.list = to_streamed_response_wrapper(
            servers.list,
        )
        self.create = to_streamed_response_wrapper(
            servers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            servers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            servers.update,
        )
        self.delete = to_streamed_response_wrapper(
            servers.delete,
        )

    @cached_property
    def installations(self) -> InstallationsResourceWithStreamingResponse:
        return InstallationsResourceWithStreamingResponse(self._servers.installations)


class AsyncServersResourceWithStreamingResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.list = async_to_streamed_response_wrapper(
            servers.list,
        )
        self.create = async_to_streamed_response_wrapper(
            servers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            servers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            servers.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            servers.delete,
        )

    @cached_property
    def installations(self) -> AsyncInstallationsResourceWithStreamingResponse:
        return AsyncInstallationsResourceWithStreamingResponse(self._servers.installations)
