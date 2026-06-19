# File generated from our OpenAPI spec by Scalar. See README.md for details.


from .._models import BaseModel
from .nanoid import Nanoid
from .slug import Slug
from .namespace import Namespace

__all__ = ["Rule"]


class Rule(BaseModel):

    uid: Nanoid

    title: str

    description: str

    slug: Slug

    namespace: Namespace

    isPrivate: bool
