# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .slug import Slug

__all__ = ["AccessGroup"]


class AccessGroup(BaseModel):

    access_group_slug: Slug = FieldInfo(alias="accessGroupSlug")
