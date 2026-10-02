# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .sdk import Sdk

__all__ = ["SdkListResponse"]


class SdkListResponse(BaseModel):
    data: List[Sdk]

    has_more: bool = FieldInfo(alias="hasMore")
