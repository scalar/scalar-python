# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict
from .version import Version
from .._utils import PropertyInfo

__all__ = ["RegistryCreateApiDocumentVersionParams"]


class RegistryCreateApiDocumentVersionParams(TypedDict, total=False):

    version: Required[Version]

    document: Required[str]

    force: bool

    last_known_version_sha: Annotated[str, PropertyInfo(alias="lastKnownVersionSha")]
