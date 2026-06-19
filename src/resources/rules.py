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
from ..types.rule_list_rulesets_response import RuleListRulesetsResponse
from ..types.rule_create_ruleset_response import RuleCreateRulesetResponse
from ..types import rule_create_ruleset_params
from ..types.rule_update_ruleset_response import RuleUpdateRulesetResponse
from ..types import rule_update_ruleset_params
from ..types.rule_delete_ruleset_response import RuleDeleteRulesetResponse
from ..types.rule_retrieve_ruleset_document_response import RuleRetrieveRulesetDocumentResponse
from ..types.rule_create_ruleset_access_group_response import RuleCreateRulesetAccessGroupResponse
from ..types import rule_create_ruleset_access_group_params
from ..types.rule_delete_ruleset_access_group_response import RuleDeleteRulesetAccessGroupResponse
from ..types import rule_delete_ruleset_access_group_params

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
        """List all rulesets in a namespace."""
        if not namespace:
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
        idempotency_key: str | None = None,
    ) -> RuleCreateRulesetResponse:
        """Create a rule in a namespace."""
        if not namespace:
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
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RuleCreateRulesetResponse,
        )

    def update_ruleset(
        self,
        slug: str,
        *,
        namespace: str,
        title: str | Omit = omit,
        description: str | Omit = omit,
        is_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RuleUpdateRulesetResponse:
        """Update rule metadata by slug."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._patch(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {
            "title": title,
            "description": description,
            "is_private": is_private,
        },
            rule_update_ruleset_params.RuleUpdateRulesetParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
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
        idempotency_key: str | None = None,
    ) -> RuleDeleteRulesetResponse:
        """Delete a rule by slug."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
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
    ) -> RuleRetrieveRulesetDocumentResponse:
        """Get a rule document by slug."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleRetrieveRulesetDocumentResponse,
        )

    def create_ruleset_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RuleCreateRulesetAccessGroupResponse:
        """Grant an access group to a rule."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._post(
            path_template("/v1/rulesets/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            rule_create_ruleset_access_group_params.RuleCreateRulesetAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RuleCreateRulesetAccessGroupResponse,
        )

    def delete_ruleset_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RuleDeleteRulesetAccessGroupResponse:
        """Remove an access group from a rule."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            path_template("/v1/rulesets/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=maybe_transform(
            {"access_group_slug": access_group_slug},
            rule_delete_ruleset_access_group_params.RuleDeleteRulesetAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
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
        """List all rulesets in a namespace."""
        if not namespace:
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
        idempotency_key: str | None = None,
    ) -> RuleCreateRulesetResponse:
        """Create a rule in a namespace."""
        if not namespace:
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
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RuleCreateRulesetResponse,
        )

    async def update_ruleset(
        self,
        slug: str,
        *,
        namespace: str,
        title: str | Omit = omit,
        description: str | Omit = omit,
        is_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RuleUpdateRulesetResponse:
        """Update rule metadata by slug."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._patch(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {
            "title": title,
            "description": description,
            "is_private": is_private,
        },
            rule_update_ruleset_params.RuleUpdateRulesetParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
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
        idempotency_key: str | None = None,
    ) -> RuleDeleteRulesetResponse:
        """Delete a rule by slug."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
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
    ) -> RuleRetrieveRulesetDocumentResponse:
        """Get a rule document by slug."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/v1/rulesets/{namespace}/{slug}", **{"namespace": namespace, "slug": slug}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleRetrieveRulesetDocumentResponse,
        )

    async def create_ruleset_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RuleCreateRulesetAccessGroupResponse:
        """Grant an access group to a rule."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._post(
            path_template("/v1/rulesets/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            rule_create_ruleset_access_group_params.RuleCreateRulesetAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=RuleCreateRulesetAccessGroupResponse,
        )

    async def delete_ruleset_access_group(
        self,
        slug: str,
        *,
        namespace: str,
        access_group_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> RuleDeleteRulesetAccessGroupResponse:
        """Remove an access group from a rule."""
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            path_template("/v1/rulesets/{namespace}/{slug}/access-group", **{"namespace": namespace, "slug": slug}),
            body=await async_maybe_transform(
            {"access_group_slug": access_group_slug},
            rule_delete_ruleset_access_group_params.RuleDeleteRulesetAccessGroupParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
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
