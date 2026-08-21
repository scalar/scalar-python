# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .version import Version
from .slug import Slug
from .shared.namespace import Namespace
from .shared.managed_doc_version import ManagedDocVersion

__all__ = ["RegistryListAPIDocumentsResponse", "RegistryListAPIDocumentsResponseItem"]


class RegistryListAPIDocumentsResponseItem(BaseModel):
    uid: Nanoid

    version: Version

    title: str

    slug: Slug

    description: str

    namespace: Namespace

    is_private: bool = FieldInfo(alias="isPrivate")

    tags: object

    versions: List[ManagedDocVersion]


RegistryListAPIDocumentsResponse: TypeAlias = List[RegistryListAPIDocumentsResponseItem]
