# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OAuthOauthRevokeParams"]


class OAuthOauthRevokeParams(TypedDict, total=False):
    token: Required[str]

    token_type_hint: str

    client_id: str

    client_secret: str
