# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

from .oauth_scope import OauthScope

__all__ = ["OauthToken"]


class OauthToken(BaseModel):
    access_token: str

    token_type: Literal["Bearer"]

    expires_in: int

    refresh_token: str

    scope: OauthScope
