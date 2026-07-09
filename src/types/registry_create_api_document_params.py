# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict
from .version import Version
from .._utils import PropertyInfo

__all__ = ["RegistryCreateApiDocumentParams"]


class RegistryCreateApiDocumentParams(TypedDict, total=False):

    title: Required[str]

    description: str

    version: Required[Version]

    slug: Required[str]

    ruleset: str

    is_private: Annotated[bool, PropertyInfo(alias="isPrivate")]

    document: Required[str]
