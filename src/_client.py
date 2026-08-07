# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import os
import threading
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, is_mapping_t, get_async_library
from ._compat import cached_property
from ._exceptions import APIStatusError, ScalarError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._version import __version__

if TYPE_CHECKING:
    from .resources import (
        registry,
        schemas,
        login_portals,
        rules,
        themes,
        teams,
        scalar_docs,
        namespaces,
        authentication,
    )
    from .resources.registry import RegistryResource, AsyncRegistryResource
    from .resources.schemas import SchemasResource, AsyncSchemasResource
    from .resources.login_portals import LoginPortalsResource, AsyncLoginPortalsResource
    from .resources.rules import RulesResource, AsyncRulesResource
    from .resources.themes import ThemesResource, AsyncThemesResource
    from .resources.teams import TeamsResource, AsyncTeamsResource
    from .resources.scalar_docs import ScalarDocsResource, AsyncScalarDocsResource
    from .resources.namespaces import NamespacesResource, AsyncNamespacesResource
    from .resources.authentication import AuthenticationResource, AsyncAuthenticationResource

# Serializes lazy resource imports so concurrent cold access from multiple
# threads cannot deadlock on CPython import locks (see CPython 3.14).
_RESOURCE_IMPORT_LOCK = threading.RLock()

__all__ = ["Scalar", "AsyncScalar", "Client", "AsyncClient", "Timeout", "Transport", "ProxiesTypes", "RequestOptions"]


class Scalar(SyncAPIClient):
    # client options
    bearer_auth: str

    def __init__(
        self,
        *,
        bearer_auth: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Scalar client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_auth` from `BEARER_AUTH`
        """
        if bearer_auth is None:
            bearer_auth = os.environ.get("BEARER_AUTH")
        if bearer_auth is None:
            raise ScalarError(
                "The bearer_auth client option must be set either by passing bearer_auth to the client or by setting the BEARER_AUTH environment variable"
            )
        self.bearer_auth = bearer_auth
        if base_url is None:
            base_url = os.environ.get("SCALAR_BASE_URL")
        if base_url is None:
            base_url = "https://access.scalar.com"
        custom_headers_env = os.environ.get("SCALAR_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = Stream

    @cached_property
    def registry(self) -> "RegistryResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.registry import RegistryResource
        return RegistryResource(self)

    @cached_property
    def schemas(self) -> "SchemasResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.schemas import SchemasResource
        return SchemasResource(self)

    @cached_property
    def login_portals(self) -> "LoginPortalsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.login_portals import LoginPortalsResource
        return LoginPortalsResource(self)

    @cached_property
    def rules(self) -> "RulesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.rules import RulesResource
        return RulesResource(self)

    @cached_property
    def themes(self) -> "ThemesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.themes import ThemesResource
        return ThemesResource(self)

    @cached_property
    def teams(self) -> "TeamsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.teams import TeamsResource
        return TeamsResource(self)

    @cached_property
    def scalar_docs(self) -> "ScalarDocsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.scalar_docs import ScalarDocsResource
        return ScalarDocsResource(self)

    @cached_property
    def namespaces(self) -> "NamespacesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.namespaces import NamespacesResource
        return NamespacesResource(self)

    @cached_property
    def authentication(self) -> "AuthenticationResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AuthenticationResource
        return AuthenticationResource(self)

    @cached_property
    def with_raw_response(self) -> ScalarWithRawResponse:
        return ScalarWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScalarWithStreamedResponse:
        return ScalarWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._bearer_auth_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _bearer_auth_header_auth(self) -> dict[str, str]:
        value = self.bearer_auth
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError("Could not resolve authentication method. Expected Authorization to be set.")

    def copy(
        self,
        *,
        bearer_auth: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            bearer_auth=bearer_auth or self.bearer_auth,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncScalar(AsyncAPIClient):
    # client options
    bearer_auth: str

    def __init__(
        self,
        *,
        bearer_auth: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncScalar client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_auth` from `BEARER_AUTH`
        """
        if bearer_auth is None:
            bearer_auth = os.environ.get("BEARER_AUTH")
        if bearer_auth is None:
            raise ScalarError(
                "The bearer_auth client option must be set either by passing bearer_auth to the client or by setting the BEARER_AUTH environment variable"
            )
        self.bearer_auth = bearer_auth
        if base_url is None:
            base_url = os.environ.get("SCALAR_BASE_URL")
        if base_url is None:
            base_url = "https://access.scalar.com"
        custom_headers_env = os.environ.get("SCALAR_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = AsyncStream

    @cached_property
    def registry(self) -> "AsyncRegistryResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.registry import AsyncRegistryResource
        return AsyncRegistryResource(self)

    @cached_property
    def schemas(self) -> "AsyncSchemasResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.schemas import AsyncSchemasResource
        return AsyncSchemasResource(self)

    @cached_property
    def login_portals(self) -> "AsyncLoginPortalsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.login_portals import AsyncLoginPortalsResource
        return AsyncLoginPortalsResource(self)

    @cached_property
    def rules(self) -> "AsyncRulesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.rules import AsyncRulesResource
        return AsyncRulesResource(self)

    @cached_property
    def themes(self) -> "AsyncThemesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.themes import AsyncThemesResource
        return AsyncThemesResource(self)

    @cached_property
    def teams(self) -> "AsyncTeamsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.teams import AsyncTeamsResource
        return AsyncTeamsResource(self)

    @cached_property
    def scalar_docs(self) -> "AsyncScalarDocsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.scalar_docs import AsyncScalarDocsResource
        return AsyncScalarDocsResource(self)

    @cached_property
    def namespaces(self) -> "AsyncNamespacesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.namespaces import AsyncNamespacesResource
        return AsyncNamespacesResource(self)

    @cached_property
    def authentication(self) -> "AsyncAuthenticationResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AsyncAuthenticationResource
        return AsyncAuthenticationResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncScalarWithRawResponse:
        return AsyncScalarWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScalarWithStreamedResponse:
        return AsyncScalarWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._bearer_auth_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _bearer_auth_header_auth(self) -> dict[str, str]:
        value = self.bearer_auth
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError("Could not resolve authentication method. Expected Authorization to be set.")

    def copy(
        self,
        *,
        bearer_auth: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            bearer_auth=bearer_auth or self.bearer_auth,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ScalarWithRawResponse:
    _client: Scalar

    def __init__(self, client: Scalar) -> None:
        self._client = client

    @cached_property
    def registry(self) -> registry.RegistryResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.registry import RegistryResourceWithRawResponse
        return RegistryResourceWithRawResponse(self._client.registry)

    @cached_property
    def schemas(self) -> schemas.SchemasResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.schemas import SchemasResourceWithRawResponse
        return SchemasResourceWithRawResponse(self._client.schemas)

    @cached_property
    def login_portals(self) -> login_portals.LoginPortalsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.login_portals import LoginPortalsResourceWithRawResponse
        return LoginPortalsResourceWithRawResponse(self._client.login_portals)

    @cached_property
    def rules(self) -> rules.RulesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.rules import RulesResourceWithRawResponse
        return RulesResourceWithRawResponse(self._client.rules)

    @cached_property
    def themes(self) -> themes.ThemesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.themes import ThemesResourceWithRawResponse
        return ThemesResourceWithRawResponse(self._client.themes)

    @cached_property
    def teams(self) -> teams.TeamsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.teams import TeamsResourceWithRawResponse
        return TeamsResourceWithRawResponse(self._client.teams)

    @cached_property
    def scalar_docs(self) -> scalar_docs.ScalarDocsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.scalar_docs import ScalarDocsResourceWithRawResponse
        return ScalarDocsResourceWithRawResponse(self._client.scalar_docs)

    @cached_property
    def namespaces(self) -> namespaces.NamespacesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.namespaces import NamespacesResourceWithRawResponse
        return NamespacesResourceWithRawResponse(self._client.namespaces)

    @cached_property
    def authentication(self) -> authentication.AuthenticationResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AuthenticationResourceWithRawResponse
        return AuthenticationResourceWithRawResponse(self._client.authentication)


class AsyncScalarWithRawResponse:
    _client: AsyncScalar

    def __init__(self, client: AsyncScalar) -> None:
        self._client = client

    @cached_property
    def registry(self) -> registry.AsyncRegistryResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.registry import AsyncRegistryResourceWithRawResponse
        return AsyncRegistryResourceWithRawResponse(self._client.registry)

    @cached_property
    def schemas(self) -> schemas.AsyncSchemasResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.schemas import AsyncSchemasResourceWithRawResponse
        return AsyncSchemasResourceWithRawResponse(self._client.schemas)

    @cached_property
    def login_portals(self) -> login_portals.AsyncLoginPortalsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.login_portals import AsyncLoginPortalsResourceWithRawResponse
        return AsyncLoginPortalsResourceWithRawResponse(self._client.login_portals)

    @cached_property
    def rules(self) -> rules.AsyncRulesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.rules import AsyncRulesResourceWithRawResponse
        return AsyncRulesResourceWithRawResponse(self._client.rules)

    @cached_property
    def themes(self) -> themes.AsyncThemesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.themes import AsyncThemesResourceWithRawResponse
        return AsyncThemesResourceWithRawResponse(self._client.themes)

    @cached_property
    def teams(self) -> teams.AsyncTeamsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.teams import AsyncTeamsResourceWithRawResponse
        return AsyncTeamsResourceWithRawResponse(self._client.teams)

    @cached_property
    def scalar_docs(self) -> scalar_docs.AsyncScalarDocsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.scalar_docs import AsyncScalarDocsResourceWithRawResponse
        return AsyncScalarDocsResourceWithRawResponse(self._client.scalar_docs)

    @cached_property
    def namespaces(self) -> namespaces.AsyncNamespacesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.namespaces import AsyncNamespacesResourceWithRawResponse
        return AsyncNamespacesResourceWithRawResponse(self._client.namespaces)

    @cached_property
    def authentication(self) -> authentication.AsyncAuthenticationResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AsyncAuthenticationResourceWithRawResponse
        return AsyncAuthenticationResourceWithRawResponse(self._client.authentication)


class ScalarWithStreamedResponse:
    _client: Scalar

    def __init__(self, client: Scalar) -> None:
        self._client = client

    @cached_property
    def registry(self) -> registry.RegistryResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.registry import RegistryResourceWithStreamingResponse
        return RegistryResourceWithStreamingResponse(self._client.registry)

    @cached_property
    def schemas(self) -> schemas.SchemasResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.schemas import SchemasResourceWithStreamingResponse
        return SchemasResourceWithStreamingResponse(self._client.schemas)

    @cached_property
    def login_portals(self) -> login_portals.LoginPortalsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.login_portals import LoginPortalsResourceWithStreamingResponse
        return LoginPortalsResourceWithStreamingResponse(self._client.login_portals)

    @cached_property
    def rules(self) -> rules.RulesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.rules import RulesResourceWithStreamingResponse
        return RulesResourceWithStreamingResponse(self._client.rules)

    @cached_property
    def themes(self) -> themes.ThemesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.themes import ThemesResourceWithStreamingResponse
        return ThemesResourceWithStreamingResponse(self._client.themes)

    @cached_property
    def teams(self) -> teams.TeamsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.teams import TeamsResourceWithStreamingResponse
        return TeamsResourceWithStreamingResponse(self._client.teams)

    @cached_property
    def scalar_docs(self) -> scalar_docs.ScalarDocsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.scalar_docs import ScalarDocsResourceWithStreamingResponse
        return ScalarDocsResourceWithStreamingResponse(self._client.scalar_docs)

    @cached_property
    def namespaces(self) -> namespaces.NamespacesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.namespaces import NamespacesResourceWithStreamingResponse
        return NamespacesResourceWithStreamingResponse(self._client.namespaces)

    @cached_property
    def authentication(self) -> authentication.AuthenticationResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AuthenticationResourceWithStreamingResponse
        return AuthenticationResourceWithStreamingResponse(self._client.authentication)


class AsyncScalarWithStreamedResponse:
    _client: AsyncScalar

    def __init__(self, client: AsyncScalar) -> None:
        self._client = client

    @cached_property
    def registry(self) -> registry.AsyncRegistryResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.registry import AsyncRegistryResourceWithStreamingResponse
        return AsyncRegistryResourceWithStreamingResponse(self._client.registry)

    @cached_property
    def schemas(self) -> schemas.AsyncSchemasResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.schemas import AsyncSchemasResourceWithStreamingResponse
        return AsyncSchemasResourceWithStreamingResponse(self._client.schemas)

    @cached_property
    def login_portals(self) -> login_portals.AsyncLoginPortalsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.login_portals import AsyncLoginPortalsResourceWithStreamingResponse
        return AsyncLoginPortalsResourceWithStreamingResponse(self._client.login_portals)

    @cached_property
    def rules(self) -> rules.AsyncRulesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.rules import AsyncRulesResourceWithStreamingResponse
        return AsyncRulesResourceWithStreamingResponse(self._client.rules)

    @cached_property
    def themes(self) -> themes.AsyncThemesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.themes import AsyncThemesResourceWithStreamingResponse
        return AsyncThemesResourceWithStreamingResponse(self._client.themes)

    @cached_property
    def teams(self) -> teams.AsyncTeamsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.teams import AsyncTeamsResourceWithStreamingResponse
        return AsyncTeamsResourceWithStreamingResponse(self._client.teams)

    @cached_property
    def scalar_docs(self) -> scalar_docs.AsyncScalarDocsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.scalar_docs import AsyncScalarDocsResourceWithStreamingResponse
        return AsyncScalarDocsResourceWithStreamingResponse(self._client.scalar_docs)

    @cached_property
    def namespaces(self) -> namespaces.AsyncNamespacesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.namespaces import AsyncNamespacesResourceWithStreamingResponse
        return AsyncNamespacesResourceWithStreamingResponse(self._client.namespaces)

    @cached_property
    def authentication(self) -> authentication.AsyncAuthenticationResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AsyncAuthenticationResourceWithStreamingResponse
        return AsyncAuthenticationResourceWithStreamingResponse(self._client.authentication)


# Alias names for the documented `Client` / `AsyncClient` symbols.
Client = Scalar
AsyncClient = AsyncScalar
