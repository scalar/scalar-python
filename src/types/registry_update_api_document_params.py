# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict
from .._utils import PropertyInfo

__all__ = ["RegistryUpdateApiDocumentParams"]


class RegistryUpdateApiDocumentParams(TypedDict, total=False):

    title: str

    description: str

    is_private: Annotated[bool, PropertyInfo(alias="isPrivate")]

    ruleset: str
