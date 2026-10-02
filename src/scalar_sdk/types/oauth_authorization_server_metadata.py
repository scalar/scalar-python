# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["OauthAuthorizationServerMetadata"]


class OauthAuthorizationServerMetadata(BaseModel):
    issuer: str

    authorization_endpoint: str

    token_endpoint: str

    revocation_endpoint: str

    response_types_supported: List[str]

    grant_types_supported: List[str]

    code_challenge_methods_supported: List[str]

    token_endpoint_auth_methods_supported: List[str]

    revocation_endpoint_auth_methods_supported: List[str]

    scopes_supported: List[str]
