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
from ..types.rule_list_rulesets_response import RuleListRulesetsResponse, Rule
from ..types.rule_create_ruleset_response import RuleCreateRulesetResponse
from ..types import rule_create_ruleset_params, rule_update_ruleset_params, rule_create_ruleset_access_group_params, rule_delete_ruleset_access_group_params
from ..types.rule_update_ruleset_response import RuleUpdateRulesetResponse
from ..types.rule_delete_ruleset_response import RuleDeleteRulesetResponse
from ..types.rule_create_ruleset_access_group_response import RuleCreateRulesetAccessGroupResponse
from ..types.slug import Slug
from ..types.rule_delete_ruleset_access_group_response import RuleDeleteRulesetAccessGroupResponse

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self)

    def list_rulesets(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleListRulesetsResponse:
        """
        List all rulesets in a namespace.
        
        Args:
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleListRulesetsResponse: Default Response
        
        Example:
            ```python
            rule = client.rules.list_rulesets(
                namespace="namespace",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._get(
            path_template("/v1/rulesets/{namespace}", **{"namespace": namespace}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleListRulesetsResponse,
        )

    def create_ruleset(
        self,
        namespace: str,
        *,
        title: str,
        description: str | Omit = omit,
        slug: str,
        is_private: bool | Omit = omit,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateRulesetResponse:
        """
        Create a rule in a namespace.
        
        Args:
            namespace: Path parameter.
            title: Body parameter.
            description: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleCreateRulesetResponse: Default Response
        
        Example:
            ```python
            rule = client.rules.create_ruleset(
                namespace="namespace",
                title="",
                slug="",
                document="",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._post(
            path_template("/v1/rulesets/{namespace}", **{"namespace": namespace}),
            body=maybe_transform(
            {
            "title": title,
            "description": description,
            "slug": slug,
            "is_private": is_private,
            "document": document,
        },
            rule_create_ruleset_params.RuleCreateRulesetParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleCreateRulesetResponse,
        )

    def update_ruleset(
        self,
        path_slug: str,
        *,
        path_namespace: str,
        body_namespace: str | Omit = omit,
        body_slug: str | Omit = omit,
        title: str | Omit = omit,
        description: str | Omit = omit,
        is_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleUpdateRulesetResponse:
        """
        Update rule metadata by slug.
        
        Args:
            path_slug: Path parameter.
            path_namespace: Path parameter.
            body_namespace: Body parameter.
            body_slug: Body parameter.
            title: Body parameter.
            description: Body parameter.
            is_private: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleUpdateRulesetResponse: Default Response
        
        Example:
            ```python
            rule = client.rules.update_ruleset(
                path_namespace="namespace",
                path_slug="slug",
            )
            ```
        """
        if path_namespace is None or (isinstance(path_namespace, str) and not path_namespace):
            raise ValueError(f"Expected a non-empty value for `path_namespace` but received {path_namespace!r}")
        if path_slug is None or (isinstance(path_slug, str) and not path_slug):
            raise ValueError(f"Expected a non-empty value for `path_slug` but received {path_slug!r}")
        return self._patch(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": path_namespace, "slug": path_slug}),
            body=maybe_transform(
            {
            "body_namespace": body_namespace,
            "body_slug": body_slug,
            "title": title,
            "description": description,
            "is_private": is_private,
        },
            rule_update_ruleset_params.RuleUpdateRulesetParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleUpdateRulesetResponse,
        )

    def delete_ruleset(
        self,
        slug: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleDeleteRulesetResponse:
        """
        Delete a rule by slug.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleDeleteRulesetResponse: Default Response
        
        Example:
            ```python
            rule = client.rules.delete_ruleset(
                namespace="namespace",
                slug="slug",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleDeleteRulesetResponse,
        )

    def retrieve_ruleset_document(
        self,
        slug: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Get a rule document by slug.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            str: Default Response
        
        Example:
            ```python
            rule = client.rules.retrieve_ruleset_document(
                namespace="namespace",
                slug="slug",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )

    def create_ruleset_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: Slug,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateRulesetAccessGroupResponse:
        """
        Grant an access group to a rule.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleCreateRulesetAccessGroupResponse: Default Response
        
        Example:
            ```python
            rule = client.rules.create_ruleset_access_group(
                namespace="namespace",
                slug="slug",
                access_group_slug="xxx",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/v1/rulesets/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            rule_create_ruleset_access_group_params.RuleCreateRulesetAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleCreateRulesetAccessGroupResponse,
        )

    def delete_ruleset_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: Slug,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleDeleteRulesetAccessGroupResponse:
        """
        Remove an access group from a rule.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleDeleteRulesetAccessGroupResponse: Default Response
        
        Example:
            ```python
            rule = client.rules.delete_ruleset_access_group(
                namespace="namespace",
                slug="slug",
                access_group_slug="xxx",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/rulesets/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            rule_delete_ruleset_access_group_params.RuleDeleteRulesetAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleDeleteRulesetAccessGroupResponse,
        )


class AsyncRulesResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self)

    async def list_rulesets(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleListRulesetsResponse:
        """
        List all rulesets in a namespace.
        
        Args:
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleListRulesetsResponse: Default Response
        
        Example:
            ```python
            rule = await client.rules.list_rulesets(
                namespace="namespace",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._get(
            path_template("/v1/rulesets/{namespace}", **{"namespace": namespace}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleListRulesetsResponse,
        )

    async def create_ruleset(
        self,
        namespace: str,
        *,
        title: str,
        description: str | Omit = omit,
        slug: str,
        is_private: bool | Omit = omit,
        document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateRulesetResponse:
        """
        Create a rule in a namespace.
        
        Args:
            namespace: Path parameter.
            title: Body parameter.
            description: Body parameter.
            slug: Body parameter.
            is_private: Body parameter.
            document: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleCreateRulesetResponse: Default Response
        
        Example:
            ```python
            rule = await client.rules.create_ruleset(
                namespace="namespace",
                title="",
                slug="",
                document="",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._post(
            path_template("/v1/rulesets/{namespace}", **{"namespace": namespace}),
            body=await async_maybe_transform(
            {
            "title": title,
            "description": description,
            "slug": slug,
            "is_private": is_private,
            "document": document,
        },
            rule_create_ruleset_params.RuleCreateRulesetParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleCreateRulesetResponse,
        )

    async def update_ruleset(
        self,
        path_slug: str,
        *,
        path_namespace: str,
        body_namespace: str | Omit = omit,
        body_slug: str | Omit = omit,
        title: str | Omit = omit,
        description: str | Omit = omit,
        is_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleUpdateRulesetResponse:
        """
        Update rule metadata by slug.
        
        Args:
            path_slug: Path parameter.
            path_namespace: Path parameter.
            body_namespace: Body parameter.
            body_slug: Body parameter.
            title: Body parameter.
            description: Body parameter.
            is_private: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleUpdateRulesetResponse: Default Response
        
        Example:
            ```python
            rule = await client.rules.update_ruleset(
                path_namespace="namespace",
                path_slug="slug",
            )
            ```
        """
        if path_namespace is None or (isinstance(path_namespace, str) and not path_namespace):
            raise ValueError(f"Expected a non-empty value for `path_namespace` but received {path_namespace!r}")
        if path_slug is None or (isinstance(path_slug, str) and not path_slug):
            raise ValueError(f"Expected a non-empty value for `path_slug` but received {path_slug!r}")
        return await self._patch(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": path_namespace, "slug": path_slug}),
            body=await async_maybe_transform(
            {
            "body_namespace": body_namespace,
            "body_slug": body_slug,
            "title": title,
            "description": description,
            "is_private": is_private,
        },
            rule_update_ruleset_params.RuleUpdateRulesetParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleUpdateRulesetResponse,
        )

    async def delete_ruleset(
        self,
        slug: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleDeleteRulesetResponse:
        """
        Delete a rule by slug.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleDeleteRulesetResponse: Default Response
        
        Example:
            ```python
            rule = await client.rules.delete_ruleset(
                namespace="namespace",
                slug="slug",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleDeleteRulesetResponse,
        )

    async def retrieve_ruleset_document(
        self,
        slug: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Get a rule document by slug.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            str: Default Response
        
        Example:
            ```python
            rule = await client.rules.retrieve_ruleset_document(
                namespace="namespace",
                slug="slug",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )

    async def create_ruleset_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: Slug,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateRulesetAccessGroupResponse:
        """
        Grant an access group to a rule.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleCreateRulesetAccessGroupResponse: Default Response
        
        Example:
            ```python
            rule = await client.rules.create_ruleset_access_group(
                namespace="namespace",
                slug="slug",
                access_group_slug="xxx",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/v1/rulesets/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            rule_create_ruleset_access_group_params.RuleCreateRulesetAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleCreateRulesetAccessGroupResponse,
        )

    async def delete_ruleset_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: Slug,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleDeleteRulesetAccessGroupResponse:
        """
        Remove an access group from a rule.
        
        Args:
            slug: Path parameter.
            namespace: Path parameter.
            access_group_slug: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            RuleDeleteRulesetAccessGroupResponse: Default Response
        
        Example:
            ```python
            rule = await client.rules.delete_ruleset_access_group(
                namespace="namespace",
                slug="slug",
                access_group_slug="xxx",
            )
            ```
        """
        if namespace is None or (isinstance(namespace, str) and not namespace):
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if slug is None or (isinstance(slug, str) and not slug):
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/rulesets/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            rule_delete_ruleset_access_group_params.RuleDeleteRulesetAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleDeleteRulesetAccessGroupResponse,
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.list_rulesets = to_raw_response_wrapper(
            rules.list_rulesets,
        )
        self.create_ruleset = to_raw_response_wrapper(
            rules.create_ruleset,
        )
        self.update_ruleset = to_raw_response_wrapper(
            rules.update_ruleset,
        )
        self.delete_ruleset = to_raw_response_wrapper(
            rules.delete_ruleset,
        )
        self.retrieve_ruleset_document = to_raw_response_wrapper(
            rules.retrieve_ruleset_document,
        )
        self.create_ruleset_access_group = to_raw_response_wrapper(
            rules.create_ruleset_access_group,
        )
        self.delete_ruleset_access_group = to_raw_response_wrapper(
            rules.delete_ruleset_access_group,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.list_rulesets = async_to_raw_response_wrapper(
            rules.list_rulesets,
        )
        self.create_ruleset = async_to_raw_response_wrapper(
            rules.create_ruleset,
        )
        self.update_ruleset = async_to_raw_response_wrapper(
            rules.update_ruleset,
        )
        self.delete_ruleset = async_to_raw_response_wrapper(
            rules.delete_ruleset,
        )
        self.retrieve_ruleset_document = async_to_raw_response_wrapper(
            rules.retrieve_ruleset_document,
        )
        self.create_ruleset_access_group = async_to_raw_response_wrapper(
            rules.create_ruleset_access_group,
        )
        self.delete_ruleset_access_group = async_to_raw_response_wrapper(
            rules.delete_ruleset_access_group,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.list_rulesets = to_streamed_response_wrapper(
            rules.list_rulesets,
        )
        self.create_ruleset = to_streamed_response_wrapper(
            rules.create_ruleset,
        )
        self.update_ruleset = to_streamed_response_wrapper(
            rules.update_ruleset,
        )
        self.delete_ruleset = to_streamed_response_wrapper(
            rules.delete_ruleset,
        )
        self.retrieve_ruleset_document = to_streamed_response_wrapper(
            rules.retrieve_ruleset_document,
        )
        self.create_ruleset_access_group = to_streamed_response_wrapper(
            rules.create_ruleset_access_group,
        )
        self.delete_ruleset_access_group = to_streamed_response_wrapper(
            rules.delete_ruleset_access_group,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.list_rulesets = async_to_streamed_response_wrapper(
            rules.list_rulesets,
        )
        self.create_ruleset = async_to_streamed_response_wrapper(
            rules.create_ruleset,
        )
        self.update_ruleset = async_to_streamed_response_wrapper(
            rules.update_ruleset,
        )
        self.delete_ruleset = async_to_streamed_response_wrapper(
            rules.delete_ruleset,
        )
        self.retrieve_ruleset_document = async_to_streamed_response_wrapper(
            rules.retrieve_ruleset_document,
        )
        self.create_ruleset_access_group = async_to_streamed_response_wrapper(
            rules.create_ruleset_access_group,
        )
        self.delete_ruleset_access_group = async_to_streamed_response_wrapper(
            rules.delete_ruleset_access_group,
        )
