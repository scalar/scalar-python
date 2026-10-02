# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ScalarDocListProjectConfigResponse"]


class ScalarDocListProjectConfigResponse(BaseModel):
    path: str

    content: str

    ref: str

    base_token: str = FieldInfo(alias="baseToken")
