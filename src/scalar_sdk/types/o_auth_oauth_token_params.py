# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OAuthOauthTokenParams"]


class OAuthOauthTokenParams(TypedDict, total=False):
    grant_type: Required[str]

    client_id: str

    client_secret: str

    code: str

    redirect_uri: str

    code_verifier: str

    refresh_token: str

    scope: str
