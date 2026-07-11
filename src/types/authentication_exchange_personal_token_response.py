# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthenticationExchangePersonalTokenResponse"]

class AuthenticationExchangePersonalTokenResponse(BaseModel):

    access_token: str = FieldInfo(alias="accessToken")



