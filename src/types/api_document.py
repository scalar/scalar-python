# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel
from .nanoid import Nanoid
from .version import Version
from .slug import Slug
from .namespace import Namespace
from .managed_doc_version import ManagedDocVersion

__all__ = ["ApiDocument"]


class ApiDocument(BaseModel):

    uid: Nanoid

    version: Version

    title: str

    slug: Slug

    description: str

    namespace: Namespace

    isPrivate: bool

    tags: str

    versions: List[ManagedDocVersion]
