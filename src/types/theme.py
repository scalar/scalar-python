# File generated from our OpenAPI spec by Scalar. See README.md for details.


from .._models import BaseModel
from .nanoid import Nanoid
from .slug import Slug

__all__ = ["Theme"]


class Theme(BaseModel):

    uid: Nanoid

    name: str

    description: str

    slug: Slug
