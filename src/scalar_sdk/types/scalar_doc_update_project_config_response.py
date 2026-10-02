# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ScalarDocUpdateProjectConfigResponse"]


class ScalarDocUpdateProjectConfigResponse(BaseModel):
    commit_sha: Optional[str] = FieldInfo(alias="commitSha", default=None)

    ref: str

    base_token: str = FieldInfo(alias="baseToken")
