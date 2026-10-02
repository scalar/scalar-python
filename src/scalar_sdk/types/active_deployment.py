# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.timestamp import Timestamp

__all__ = ["ActiveDeployment"]


class ActiveDeployment(BaseModel):
    uid: str

    domain: str

    published_at: Timestamp = FieldInfo(alias="publishedAt")
