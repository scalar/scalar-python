# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid

__all__ = ["ScalarDocPublishProjectResponse"]


class ScalarDocPublishProjectResponse(BaseModel):
    publish_uid: Nanoid = FieldInfo(alias="publishUid")
