# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ScalarDocPublishGuideResponse"]


class ScalarDocPublishGuideResponse(BaseModel):
    publish_uid: str = FieldInfo(alias="publishUid")
