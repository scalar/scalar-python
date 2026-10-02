# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["OauthError"]


class OauthError(BaseModel):
    error: str

    error_description: Optional[str] = None
