# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Annotated
from typing_extensions import Required, TypedDict
from .._utils import PropertyInfo

__all__ = ["RegistryCreateApiDocumentVersionParams"]


class RegistryCreateApiDocumentVersionParams(TypedDict, total=False):

    version: Required[str]

    document: Required[str]

    force: bool

    last_known_version_sha: Annotated[str, PropertyInfo(alias="lastKnownVersionSha")]
