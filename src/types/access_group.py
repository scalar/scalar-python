# File generated from our OpenAPI spec by Scalar. See README.md for details.


from .._models import BaseModel
from .slug import Slug

__all__ = ["AccessGroup"]


class AccessGroup(BaseModel):

    accessGroupSlug: Slug
