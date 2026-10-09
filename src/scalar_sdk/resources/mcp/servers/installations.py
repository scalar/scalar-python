# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Optional

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
from ....types.mcp.servers.installation_list_response import InstallationListResponse
from ....types.mcp.mcp_installation import McpInstallation
from ....types.slug import Slug
from ....types.mcp.servers import (
    installation_create_params,
    installation_update_params,
    installation_create_access_group_params,
    installation_delete_access_group_params,
)
from ....types.mcp.servers.installation_delete_response import InstallationDeleteResponse
from ....types.mcp.servers.installation_create_access_group_response import InstallationCreateAccessGroupResponse
from ....types.shared.nanoid import Nanoid
from ....types.mcp.servers.installation_delete_access_group_response import InstallationDeleteAccessGroupResponse

__all__ = ["InstallationsResource", "AsyncInstallationsResource"]


class InstallationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstallationsResourceWithRawResponse:
        return InstallationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstallationsResourceWithStreamingResponse:
        return InstallationsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallationListResponse:
        """
        List the installations of an MCP server. An installation is what an MCP client connects to.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InstallationListResponse: Default Response

        Example:
            ```python
            installation = client.mcp.servers.installations.list(
                id="42",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/mcp/servers/{id}/installations", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallationListResponse,
        )

    def create(
        self,
        id: str,
        *,
        name: str,
        slug: Slug | Omit = omit,
        document_auth: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpInstallation:
        """
        Create an installation of an MCP server. `documentAuth` holds the credentials the server presents to the upstream API and is never returned.

        Args:
            id: Path parameter.
            name: Body parameter.
            slug: Body parameter.
            document_auth: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpInstallation: Default Response

        Example:
            ```python
            installation = client.mcp.servers.installations.create(
                id="42",
                name="Acme MCP",
                document_auth={},
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/mcp/servers/{id}/installations", **{"id": id}),
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "document_auth": document_auth,
                },
                installation_create_params.InstallationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpInstallation,
        )

    def retrieve(
        self,
        installation_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpInstallation:
        """
        Get a single installation of an MCP server.

        Args:
            installation_id: Path parameter.
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpInstallation: Default Response

        Example:
            ```python
            installation = client.mcp.servers.installations.retrieve(
                id="42",
                installation_id="84",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if installation_id is None or (isinstance(installation_id, str) and not installation_id):
            raise ValueError(f"Expected a non-empty value for `installation_id` but received {installation_id!r}")
        return self._get(
            path_template(
                "/v1/mcp/servers/{id}/installations/{installationId}", **{"id": id, "installationId": installation_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpInstallation,
        )

    def update(
        self,
        installation_id: str,
        *,
        id: str,
        name: str | Omit = omit,
        slug: Slug | Omit = omit,
        is_private: bool | Omit = omit,
        login_portal_uid: Optional[str] | Omit = omit,
        document_auth: Dict[str, object] | Omit = omit,
        mcp_version: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpInstallation:
        """
        Update an installation. Set `isPrivate` and add access groups to put it behind a login.

        Args:
            installation_id: Path parameter.
            id: Path parameter.
            name: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            login_portal_uid: Body parameter.
            document_auth: Body parameter.
            mcp_version: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpInstallation: Default Response

        Example:
            ```python
            installation = client.mcp.servers.installations.update(
                id="42",
                installation_id="84",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if installation_id is None or (isinstance(installation_id, str) and not installation_id):
            raise ValueError(f"Expected a non-empty value for `installation_id` but received {installation_id!r}")
        return self._patch(
            path_template(
                "/v1/mcp/servers/{id}/installations/{installationId}", **{"id": id, "installationId": installation_id}
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "is_private": is_private,
                    "login_portal_uid": login_portal_uid,
                    "document_auth": document_auth,
                    "mcp_version": mcp_version,
                },
                installation_update_params.InstallationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpInstallation,
        )

    def delete(
        self,
        installation_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallationDeleteResponse:
        """
        Delete an installation of an MCP server.

        Args:
            installation_id: Path parameter.
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InstallationDeleteResponse: Default Response

        Example:
            ```python
            installation = client.mcp.servers.installations.delete(
                id="42",
                installation_id="84",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if installation_id is None or (isinstance(installation_id, str) and not installation_id):
            raise ValueError(f"Expected a non-empty value for `installation_id` but received {installation_id!r}")
        return self._delete(
            path_template(
                "/v1/mcp/servers/{id}/installations/{installationId}", **{"id": id, "installationId": installation_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallationDeleteResponse,
        )

    def create_access_group(
        self,
        installation_id: str,
        *,
        id: str,
        access_group_uid: Nanoid,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallationCreateAccessGroupResponse:
        """
        Let an access group reach a private installation.

        Args:
            installation_id: Path parameter.
            id: Path parameter.
            access_group_uid: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InstallationCreateAccessGroupResponse: Default Response

        Example:
            ```python
            installation = client.mcp.servers.installations.create_access_group(
                id="42",
                installation_id="84",
                access_group_uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if installation_id is None or (isinstance(installation_id, str) and not installation_id):
            raise ValueError(f"Expected a non-empty value for `installation_id` but received {installation_id!r}")
        return self._post(
            path_template(
                "/v1/mcp/servers/{id}/installations/{installationId}/access-group",
                **{"id": id, "installationId": installation_id},
            ),
            body=maybe_transform(
                {"access_group_uid": access_group_uid},
                installation_create_access_group_params.InstallationCreateAccessGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallationCreateAccessGroupResponse,
        )

    def delete_access_group(
        self,
        installation_id: str,
        *,
        id: str,
        access_group_uid: Nanoid,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallationDeleteAccessGroupResponse:
        """
        Stop an access group reaching a private installation.

        Args:
            installation_id: Path parameter.
            id: Path parameter.
            access_group_uid: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InstallationDeleteAccessGroupResponse: Default Response

        Example:
            ```python
            installation = client.mcp.servers.installations.delete_access_group(
                id="42",
                installation_id="84",
                access_group_uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if installation_id is None or (isinstance(installation_id, str) and not installation_id):
            raise ValueError(f"Expected a non-empty value for `installation_id` but received {installation_id!r}")
        return self._delete(
            path_template(
                "/v1/mcp/servers/{id}/installations/{installationId}/access-group",
                **{"id": id, "installationId": installation_id},
            ),
            body=maybe_transform(
                {"access_group_uid": access_group_uid},
                installation_delete_access_group_params.InstallationDeleteAccessGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallationDeleteAccessGroupResponse,
        )


class AsyncInstallationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstallationsResourceWithRawResponse:
        return AsyncInstallationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstallationsResourceWithStreamingResponse:
        return AsyncInstallationsResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallationListResponse:
        """
        List the installations of an MCP server. An installation is what an MCP client connects to.

        Args:
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InstallationListResponse: Default Response

        Example:
            ```python
            installation = await client.mcp.servers.installations.list(
                id="42",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/mcp/servers/{id}/installations", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallationListResponse,
        )

    async def create(
        self,
        id: str,
        *,
        name: str,
        slug: Slug | Omit = omit,
        document_auth: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpInstallation:
        """
        Create an installation of an MCP server. `documentAuth` holds the credentials the server presents to the upstream API and is never returned.

        Args:
            id: Path parameter.
            name: Body parameter.
            slug: Body parameter.
            document_auth: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpInstallation: Default Response

        Example:
            ```python
            installation = await client.mcp.servers.installations.create(
                id="42",
                name="Acme MCP",
                document_auth={},
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/mcp/servers/{id}/installations", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "document_auth": document_auth,
                },
                installation_create_params.InstallationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpInstallation,
        )

    async def retrieve(
        self,
        installation_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpInstallation:
        """
        Get a single installation of an MCP server.

        Args:
            installation_id: Path parameter.
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpInstallation: Default Response

        Example:
            ```python
            installation = await client.mcp.servers.installations.retrieve(
                id="42",
                installation_id="84",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if installation_id is None or (isinstance(installation_id, str) and not installation_id):
            raise ValueError(f"Expected a non-empty value for `installation_id` but received {installation_id!r}")
        return await self._get(
            path_template(
                "/v1/mcp/servers/{id}/installations/{installationId}", **{"id": id, "installationId": installation_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpInstallation,
        )

    async def update(
        self,
        installation_id: str,
        *,
        id: str,
        name: str | Omit = omit,
        slug: Slug | Omit = omit,
        is_private: bool | Omit = omit,
        login_portal_uid: Optional[str] | Omit = omit,
        document_auth: Dict[str, object] | Omit = omit,
        mcp_version: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpInstallation:
        """
        Update an installation. Set `isPrivate` and add access groups to put it behind a login.

        Args:
            installation_id: Path parameter.
            id: Path parameter.
            name: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            login_portal_uid: Body parameter.
            document_auth: Body parameter.
            mcp_version: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            McpInstallation: Default Response

        Example:
            ```python
            installation = await client.mcp.servers.installations.update(
                id="42",
                installation_id="84",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if installation_id is None or (isinstance(installation_id, str) and not installation_id):
            raise ValueError(f"Expected a non-empty value for `installation_id` but received {installation_id!r}")
        return await self._patch(
            path_template(
                "/v1/mcp/servers/{id}/installations/{installationId}", **{"id": id, "installationId": installation_id}
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "is_private": is_private,
                    "login_portal_uid": login_portal_uid,
                    "document_auth": document_auth,
                    "mcp_version": mcp_version,
                },
                installation_update_params.InstallationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpInstallation,
        )

    async def delete(
        self,
        installation_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallationDeleteResponse:
        """
        Delete an installation of an MCP server.

        Args:
            installation_id: Path parameter.
            id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InstallationDeleteResponse: Default Response

        Example:
            ```python
            installation = await client.mcp.servers.installations.delete(
                id="42",
                installation_id="84",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if installation_id is None or (isinstance(installation_id, str) and not installation_id):
            raise ValueError(f"Expected a non-empty value for `installation_id` but received {installation_id!r}")
        return await self._delete(
            path_template(
                "/v1/mcp/servers/{id}/installations/{installationId}", **{"id": id, "installationId": installation_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallationDeleteResponse,
        )

    async def create_access_group(
        self,
        installation_id: str,
        *,
        id: str,
        access_group_uid: Nanoid,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallationCreateAccessGroupResponse:
        """
        Let an access group reach a private installation.

        Args:
            installation_id: Path parameter.
            id: Path parameter.
            access_group_uid: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InstallationCreateAccessGroupResponse: Default Response

        Example:
            ```python
            installation = await client.mcp.servers.installations.create_access_group(
                id="42",
                installation_id="84",
                access_group_uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if installation_id is None or (isinstance(installation_id, str) and not installation_id):
            raise ValueError(f"Expected a non-empty value for `installation_id` but received {installation_id!r}")
        return await self._post(
            path_template(
                "/v1/mcp/servers/{id}/installations/{installationId}/access-group",
                **{"id": id, "installationId": installation_id},
            ),
            body=await async_maybe_transform(
                {"access_group_uid": access_group_uid},
                installation_create_access_group_params.InstallationCreateAccessGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallationCreateAccessGroupResponse,
        )

    async def delete_access_group(
        self,
        installation_id: str,
        *,
        id: str,
        access_group_uid: Nanoid,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallationDeleteAccessGroupResponse:
        """
        Stop an access group reaching a private installation.

        Args:
            installation_id: Path parameter.
            id: Path parameter.
            access_group_uid: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            InstallationDeleteAccessGroupResponse: Default Response

        Example:
            ```python
            installation = await client.mcp.servers.installations.delete_access_group(
                id="42",
                installation_id="84",
                access_group_uid="UakgbKJ5m9gl0JDMbcJqL",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if installation_id is None or (isinstance(installation_id, str) and not installation_id):
            raise ValueError(f"Expected a non-empty value for `installation_id` but received {installation_id!r}")
        return await self._delete(
            path_template(
                "/v1/mcp/servers/{id}/installations/{installationId}/access-group",
                **{"id": id, "installationId": installation_id},
            ),
            body=await async_maybe_transform(
                {"access_group_uid": access_group_uid},
                installation_delete_access_group_params.InstallationDeleteAccessGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallationDeleteAccessGroupResponse,
        )


class InstallationsResourceWithRawResponse:
    def __init__(self, installations: InstallationsResource) -> None:
        self._installations = installations

        self.list = to_raw_response_wrapper(
            installations.list,
        )
        self.create = to_raw_response_wrapper(
            installations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            installations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            installations.update,
        )
        self.delete = to_raw_response_wrapper(
            installations.delete,
        )
        self.create_access_group = to_raw_response_wrapper(
            installations.create_access_group,
        )
        self.delete_access_group = to_raw_response_wrapper(
            installations.delete_access_group,
        )


class AsyncInstallationsResourceWithRawResponse:
    def __init__(self, installations: AsyncInstallationsResource) -> None:
        self._installations = installations

        self.list = async_to_raw_response_wrapper(
            installations.list,
        )
        self.create = async_to_raw_response_wrapper(
            installations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            installations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            installations.update,
        )
        self.delete = async_to_raw_response_wrapper(
            installations.delete,
        )
        self.create_access_group = async_to_raw_response_wrapper(
            installations.create_access_group,
        )
        self.delete_access_group = async_to_raw_response_wrapper(
            installations.delete_access_group,
        )


class InstallationsResourceWithStreamingResponse:
    def __init__(self, installations: InstallationsResource) -> None:
        self._installations = installations

        self.list = to_streamed_response_wrapper(
            installations.list,
        )
        self.create = to_streamed_response_wrapper(
            installations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            installations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            installations.update,
        )
        self.delete = to_streamed_response_wrapper(
            installations.delete,
        )
        self.create_access_group = to_streamed_response_wrapper(
            installations.create_access_group,
        )
        self.delete_access_group = to_streamed_response_wrapper(
            installations.delete_access_group,
        )


class AsyncInstallationsResourceWithStreamingResponse:
    def __init__(self, installations: AsyncInstallationsResource) -> None:
        self._installations = installations

        self.list = async_to_streamed_response_wrapper(
            installations.list,
        )
        self.create = async_to_streamed_response_wrapper(
            installations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            installations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            installations.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            installations.delete,
        )
        self.create_access_group = async_to_streamed_response_wrapper(
            installations.create_access_group,
        )
        self.delete_access_group = async_to_streamed_response_wrapper(
            installations.delete_access_group,
        )
