# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .oauth_token import OauthToken
from .oauth_error import OauthError

__all__ = ["OAuthOauthTokenResponse"]

OAuthOauthTokenResponse: TypeAlias = Union[OauthToken, OauthError]
