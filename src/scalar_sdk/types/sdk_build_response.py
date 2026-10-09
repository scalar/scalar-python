# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SdkBuildResponse"]


class SdkBuildResponse(BaseModel):
    version: str


SdkBuildResponse: TypeAlias = Optional[SdkBuildResponse]
