# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Union
from typing_extensions import Literal
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
from ..types.scalar_doc_list_guides_response import ScalarDocListGuidesResponse
from ..types.scalar_doc_create_guide_response import ScalarDocCreateGuideResponse
from ..types.slug import Slug
from ..types import (
    scalar_doc_create_guide_params,
    scalar_doc_list_projects_params,
    scalar_doc_create_project_params,
    scalar_doc_update_project_params,
    scalar_doc_publish_project_params,
    scalar_doc_list_project_config_params,
    scalar_doc_update_project_config_params,
)
from ..types.scalar_doc_publish_guide_response import ScalarDocPublishGuideResponse
from ..types.scalar_doc_list_projects_response import ScalarDocListProjectsResponse
from ..types.docs_project import DocsProject
from ..types.scalar_doc_update_project_response import ScalarDocUpdateProjectResponse
from ..types.shared.nanoid import Nanoid
from ..types.scalar_doc_delete_project_response import ScalarDocDeleteProjectResponse
from ..types.scalar_doc_publish_project_response import ScalarDocPublishProjectResponse
from ..types.scalar_doc_list_project_config_response import ScalarDocListProjectConfigResponse
from ..types.scalar_doc_update_project_config_response import ScalarDocUpdateProjectConfigResponse
from ..types.scalar_doc_list_project_domain_response import ScalarDocListProjectDomainResponse
from ..types.scalar_doc_list_project_domain_status_response import ScalarDocListProjectDomainStatusResponse

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
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocPublishGuideResponse,
        )

    def list_projects(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocListProjectsResponse:
        """
        List every docs project on the team.

        Args:
            limit: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocListProjectsResponse: Default Response

        Example:
            ```python
            scalar_doc = client.scalar_docs.list_projects()
            ```
        """
        return self._get(
            "/v1/docs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, scalar_doc_list_projects_params.ScalarDocListProjectsParams),
            ),
            cast_to=ScalarDocListProjectsResponse,
        )

    def create_project(
        self,
        *,
        name: str,
        slug: Slug | Omit = omit,
        is_private: bool | Omit = omit,
        blank: bool | Omit = omit,
        provider: Literal["forgejo", "github", "bitbucket"],
        github_repository: scalar_doc_create_project_params.GithubRepository | Omit = omit,
        bitbucket_repository: scalar_doc_create_project_params.BitbucketRepository | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocsProject:
        """
        Create a docs project. Omit `provider` to have Scalar host the repository.

        Args:
            name: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            blank: Body parameter.
            provider: Body parameter.
            github_repository: Body parameter.
            bitbucket_repository: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DocsProject: Default Response

        Example:
            ```python
            scalar_doc = client.scalar_docs.create_project(
                name="",
                provider="forgejo",
            )
            ```
        """
        return self._post(
            "/v1/docs",
            body=maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "is_private": is_private,
                    "blank": blank,
                    "provider": provider,
                    "github_repository": github_repository,
                    "bitbucket_repository": bitbucket_repository,
                },
                scalar_doc_create_project_params.ScalarDocCreateProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocsProject,
        )

    def retrieve_project(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocsProject:
        """
        Get a single docs project by its slug.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DocsProject: Default Response

        Example:
            ```python
            scalar_doc = client.scalar_docs.retrieve_project(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/v1/docs/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocsProject,
        )

    def update_project(
        self,
        slug: str,
        *,
        name: str | Omit = omit,
        is_private: bool | Omit = omit,
        access_groups: SequenceNotStr[Nanoid] | Omit = omit,
        login_portal_uid: Union[Nanoid, Literal[""]] | Omit = omit,
        active_theme_id: Nanoid | Omit = omit,
        agent_enabled: bool | Omit = omit,
        analytics_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocUpdateProjectResponse:
        """
        Update project settings. Set `isPrivate` with `accessGroups` to put the site behind a login.

        Args:
            slug: Path parameter.
            name: Body parameter.
            is_private: Body parameter.
            access_groups: Body parameter.
            login_portal_uid: Body parameter.
            active_theme_id: Body parameter.
            agent_enabled: Body parameter.
            analytics_enabled: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocUpdateProjectResponse: Default Response

        Example:
            ```python
            scalar_doc = client.scalar_docs.update_project(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._patch(
            path_template("/v1/docs/{slug}", **{"slug": slug}),
            body=maybe_transform(
                {
                    "name": name,
                    "is_private": is_private,
                    "access_groups": access_groups,
                    "login_portal_uid": login_portal_uid,
                    "active_theme_id": active_theme_id,
                    "agent_enabled": agent_enabled,
                    "analytics_enabled": analytics_enabled,
                },
                scalar_doc_update_project_params.ScalarDocUpdateProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocUpdateProjectResponse,
        )

    def delete_project(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocDeleteProjectResponse:
        """
        Delete a docs project, its deploys, its publish records and its cached builds.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocDeleteProjectResponse: Default Response

        Example:
            ```python
            scalar_doc = client.scalar_docs.delete_project(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/docs/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocDeleteProjectResponse,
        )

    def publish_project(
        self,
        slug: str,
        *,
        commit_sha: str | Omit = omit,
        preview: bool | Omit = omit,
        config_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocPublishProjectResponse:
        """
        Start a build and deploy. The returned `publishUid` identifies the publish record.

        Args:
            slug: Path parameter.
            commit_sha: Body parameter.
            preview: Body parameter.
            config_path: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocPublishProjectResponse: Default Response

        Example:
            ```python
            scalar_doc = client.scalar_docs.publish_project(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/v1/docs/{slug}/publish", **{"slug": slug}),
            body=maybe_transform(
                {
                    "commit_sha": commit_sha,
                    "preview": preview,
                    "config_path": config_path,
                },
                scalar_doc_publish_project_params.ScalarDocPublishProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocPublishProjectResponse,
        )

    def list_project_config(
        self,
        slug: str,
        *,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocListProjectConfigResponse:
        """
        Read `scalar.config.json` straight from the project repository, without cloning it. `baseToken` is the compare-and-swap handle for a later write.

        Args:
            slug: Path parameter.
            ref: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocListProjectConfigResponse: Default Response

        Example:
            ```python
            scalar_doc = client.scalar_docs.list_project_config(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/v1/docs/{slug}/config", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"ref": ref}, scalar_doc_list_project_config_params.ScalarDocListProjectConfigParams
                ),
            ),
            cast_to=ScalarDocListProjectConfigResponse,
        )

    def update_project_config(
        self,
        slug: str,
        *,
        content: str,
        ref: str | Omit = omit,
        base_token: str | Omit = omit,
        message: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocUpdateProjectConfigResponse:
        """
        Commit `scalar.config.json` straight to the project repository. Pass the `baseToken` from the read this edit was based on; a conflict means the file moved underneath it.

        Args:
            slug: Path parameter.
            content: Body parameter.
            ref: Body parameter.
            base_token: Body parameter.
            message: Body parameter.
            path: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocUpdateProjectConfigResponse: Default Response

        Example:
            ```python
            scalar_doc = client.scalar_docs.update_project_config(
                slug="slug",
                content="",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._put(
            path_template("/v1/docs/{slug}/config", **{"slug": slug}),
            body=maybe_transform(
                {
                    "content": content,
                    "ref": ref,
                    "base_token": base_token,
                    "message": message,
                    "path": path,
                },
                scalar_doc_update_project_config_params.ScalarDocUpdateProjectConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocUpdateProjectConfigResponse,
        )

    def list_project_domain(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocListProjectDomainResponse:
        """
        The domains the project serves on — the Scalar-hosted one and the custom one, when set.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocListProjectDomainResponse: Default Response

        Example:
            ```python
            scalar_doc = client.scalar_docs.list_project_domain(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/v1/docs/{slug}/domain", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocListProjectDomainResponse,
        )

    def list_project_domain_status(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocListProjectDomainStatusResponse:
        """
        Whether the project custom domain points at Scalar yet. `expected` is the CNAME record to create; `found` is what resolves today. A project with no custom domain reports `verified` with no expected record, because Scalar serves its own subdomain directly.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocListProjectDomainStatusResponse: Default Response

        Example:
            ```python
            scalar_doc = client.scalar_docs.list_project_domain_status(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/v1/docs/{slug}/domain/status", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocListProjectDomainStatusResponse,
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
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocPublishGuideResponse,
        )

    async def list_projects(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocListProjectsResponse:
        """
        List every docs project on the team.

        Args:
            limit: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocListProjectsResponse: Default Response

        Example:
            ```python
            scalar_doc = await client.scalar_docs.list_projects()
            ```
        """
        return await self._get(
            "/v1/docs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, scalar_doc_list_projects_params.ScalarDocListProjectsParams
                ),
            ),
            cast_to=ScalarDocListProjectsResponse,
        )

    async def create_project(
        self,
        *,
        name: str,
        slug: Slug | Omit = omit,
        is_private: bool | Omit = omit,
        blank: bool | Omit = omit,
        provider: Literal["forgejo", "github", "bitbucket"],
        github_repository: scalar_doc_create_project_params.GithubRepository | Omit = omit,
        bitbucket_repository: scalar_doc_create_project_params.BitbucketRepository | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocsProject:
        """
        Create a docs project. Omit `provider` to have Scalar host the repository.

        Args:
            name: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            blank: Body parameter.
            provider: Body parameter.
            github_repository: Body parameter.
            bitbucket_repository: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DocsProject: Default Response

        Example:
            ```python
            scalar_doc = await client.scalar_docs.create_project(
                name="",
                provider="forgejo",
            )
            ```
        """
        return await self._post(
            "/v1/docs",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "slug": slug,
                    "is_private": is_private,
                    "blank": blank,
                    "provider": provider,
                    "github_repository": github_repository,
                    "bitbucket_repository": bitbucket_repository,
                },
                scalar_doc_create_project_params.ScalarDocCreateProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocsProject,
        )

    async def retrieve_project(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocsProject:
        """
        Get a single docs project by its slug.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DocsProject: Default Response

        Example:
            ```python
            scalar_doc = await client.scalar_docs.retrieve_project(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/v1/docs/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocsProject,
        )

    async def update_project(
        self,
        slug: str,
        *,
        name: str | Omit = omit,
        is_private: bool | Omit = omit,
        access_groups: SequenceNotStr[Nanoid] | Omit = omit,
        login_portal_uid: Union[Nanoid, Literal[""]] | Omit = omit,
        active_theme_id: Nanoid | Omit = omit,
        agent_enabled: bool | Omit = omit,
        analytics_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocUpdateProjectResponse:
        """
        Update project settings. Set `isPrivate` with `accessGroups` to put the site behind a login.

        Args:
            slug: Path parameter.
            name: Body parameter.
            is_private: Body parameter.
            access_groups: Body parameter.
            login_portal_uid: Body parameter.
            active_theme_id: Body parameter.
            agent_enabled: Body parameter.
            analytics_enabled: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocUpdateProjectResponse: Default Response

        Example:
            ```python
            scalar_doc = await client.scalar_docs.update_project(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._patch(
            path_template("/v1/docs/{slug}", **{"slug": slug}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "is_private": is_private,
                    "access_groups": access_groups,
                    "login_portal_uid": login_portal_uid,
                    "active_theme_id": active_theme_id,
                    "agent_enabled": agent_enabled,
                    "analytics_enabled": analytics_enabled,
                },
                scalar_doc_update_project_params.ScalarDocUpdateProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocUpdateProjectResponse,
        )

    async def delete_project(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocDeleteProjectResponse:
        """
        Delete a docs project, its deploys, its publish records and its cached builds.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocDeleteProjectResponse: Default Response

        Example:
            ```python
            scalar_doc = await client.scalar_docs.delete_project(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/docs/{slug}", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocDeleteProjectResponse,
        )

    async def publish_project(
        self,
        slug: str,
        *,
        commit_sha: str | Omit = omit,
        preview: bool | Omit = omit,
        config_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocPublishProjectResponse:
        """
        Start a build and deploy. The returned `publishUid` identifies the publish record.

        Args:
            slug: Path parameter.
            commit_sha: Body parameter.
            preview: Body parameter.
            config_path: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocPublishProjectResponse: Default Response

        Example:
            ```python
            scalar_doc = await client.scalar_docs.publish_project(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/v1/docs/{slug}/publish", **{"slug": slug}),
            body=await async_maybe_transform(
                {
                    "commit_sha": commit_sha,
                    "preview": preview,
                    "config_path": config_path,
                },
                scalar_doc_publish_project_params.ScalarDocPublishProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocPublishProjectResponse,
        )

    async def list_project_config(
        self,
        slug: str,
        *,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocListProjectConfigResponse:
        """
        Read `scalar.config.json` straight from the project repository, without cloning it. `baseToken` is the compare-and-swap handle for a later write.

        Args:
            slug: Path parameter.
            ref: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocListProjectConfigResponse: Default Response

        Example:
            ```python
            scalar_doc = await client.scalar_docs.list_project_config(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/v1/docs/{slug}/config", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"ref": ref}, scalar_doc_list_project_config_params.ScalarDocListProjectConfigParams
                ),
            ),
            cast_to=ScalarDocListProjectConfigResponse,
        )

    async def update_project_config(
        self,
        slug: str,
        *,
        content: str,
        ref: str | Omit = omit,
        base_token: str | Omit = omit,
        message: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocUpdateProjectConfigResponse:
        """
        Commit `scalar.config.json` straight to the project repository. Pass the `baseToken` from the read this edit was based on; a conflict means the file moved underneath it.

        Args:
            slug: Path parameter.
            content: Body parameter.
            ref: Body parameter.
            base_token: Body parameter.
            message: Body parameter.
            path: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocUpdateProjectConfigResponse: Default Response

        Example:
            ```python
            scalar_doc = await client.scalar_docs.update_project_config(
                slug="slug",
                content="",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._put(
            path_template("/v1/docs/{slug}/config", **{"slug": slug}),
            body=await async_maybe_transform(
                {
                    "content": content,
                    "ref": ref,
                    "base_token": base_token,
                    "message": message,
                    "path": path,
                },
                scalar_doc_update_project_config_params.ScalarDocUpdateProjectConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocUpdateProjectConfigResponse,
        )

    async def list_project_domain(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocListProjectDomainResponse:
        """
        The domains the project serves on — the Scalar-hosted one and the custom one, when set.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocListProjectDomainResponse: Default Response

        Example:
            ```python
            scalar_doc = await client.scalar_docs.list_project_domain(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/v1/docs/{slug}/domain", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocListProjectDomainResponse,
        )

    async def list_project_domain_status(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScalarDocListProjectDomainStatusResponse:
        """
        Whether the project custom domain points at Scalar yet. `expected` is the CNAME record to create; `found` is what resolves today. A project with no custom domain reports `verified` with no expected record, because Scalar serves its own subdomain directly.

        Args:
            slug: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ScalarDocListProjectDomainStatusResponse: Default Response

        Example:
            ```python
            scalar_doc = await client.scalar_docs.list_project_domain_status(
                slug="slug",
            )
            ```
        """
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/v1/docs/{slug}/domain/status", **{"slug": slug}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScalarDocListProjectDomainStatusResponse,
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
        self.list_projects = to_raw_response_wrapper(
            scalar_docs.list_projects,
        )
        self.create_project = to_raw_response_wrapper(
            scalar_docs.create_project,
        )
        self.retrieve_project = to_raw_response_wrapper(
            scalar_docs.retrieve_project,
        )
        self.update_project = to_raw_response_wrapper(
            scalar_docs.update_project,
        )
        self.delete_project = to_raw_response_wrapper(
            scalar_docs.delete_project,
        )
        self.publish_project = to_raw_response_wrapper(
            scalar_docs.publish_project,
        )
        self.list_project_config = to_raw_response_wrapper(
            scalar_docs.list_project_config,
        )
        self.update_project_config = to_raw_response_wrapper(
            scalar_docs.update_project_config,
        )
        self.list_project_domain = to_raw_response_wrapper(
            scalar_docs.list_project_domain,
        )
        self.list_project_domain_status = to_raw_response_wrapper(
            scalar_docs.list_project_domain_status,
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
        self.list_projects = async_to_raw_response_wrapper(
            scalar_docs.list_projects,
        )
        self.create_project = async_to_raw_response_wrapper(
            scalar_docs.create_project,
        )
        self.retrieve_project = async_to_raw_response_wrapper(
            scalar_docs.retrieve_project,
        )
        self.update_project = async_to_raw_response_wrapper(
            scalar_docs.update_project,
        )
        self.delete_project = async_to_raw_response_wrapper(
            scalar_docs.delete_project,
        )
        self.publish_project = async_to_raw_response_wrapper(
            scalar_docs.publish_project,
        )
        self.list_project_config = async_to_raw_response_wrapper(
            scalar_docs.list_project_config,
        )
        self.update_project_config = async_to_raw_response_wrapper(
            scalar_docs.update_project_config,
        )
        self.list_project_domain = async_to_raw_response_wrapper(
            scalar_docs.list_project_domain,
        )
        self.list_project_domain_status = async_to_raw_response_wrapper(
            scalar_docs.list_project_domain_status,
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
        self.list_projects = to_streamed_response_wrapper(
            scalar_docs.list_projects,
        )
        self.create_project = to_streamed_response_wrapper(
            scalar_docs.create_project,
        )
        self.retrieve_project = to_streamed_response_wrapper(
            scalar_docs.retrieve_project,
        )
        self.update_project = to_streamed_response_wrapper(
            scalar_docs.update_project,
        )
        self.delete_project = to_streamed_response_wrapper(
            scalar_docs.delete_project,
        )
        self.publish_project = to_streamed_response_wrapper(
            scalar_docs.publish_project,
        )
        self.list_project_config = to_streamed_response_wrapper(
            scalar_docs.list_project_config,
        )
        self.update_project_config = to_streamed_response_wrapper(
            scalar_docs.update_project_config,
        )
        self.list_project_domain = to_streamed_response_wrapper(
            scalar_docs.list_project_domain,
        )
        self.list_project_domain_status = to_streamed_response_wrapper(
            scalar_docs.list_project_domain_status,
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
        self.list_projects = async_to_streamed_response_wrapper(
            scalar_docs.list_projects,
        )
        self.create_project = async_to_streamed_response_wrapper(
            scalar_docs.create_project,
        )
        self.retrieve_project = async_to_streamed_response_wrapper(
            scalar_docs.retrieve_project,
        )
        self.update_project = async_to_streamed_response_wrapper(
            scalar_docs.update_project,
        )
        self.delete_project = async_to_streamed_response_wrapper(
            scalar_docs.delete_project,
        )
        self.publish_project = async_to_streamed_response_wrapper(
            scalar_docs.publish_project,
        )
        self.list_project_config = async_to_streamed_response_wrapper(
            scalar_docs.list_project_config,
        )
        self.update_project_config = async_to_streamed_response_wrapper(
            scalar_docs.update_project_config,
        )
        self.list_project_domain = async_to_streamed_response_wrapper(
            scalar_docs.list_project_domain,
        )
        self.list_project_domain_status = async_to_streamed_response_wrapper(
            scalar_docs.list_project_domain_status,
        )
