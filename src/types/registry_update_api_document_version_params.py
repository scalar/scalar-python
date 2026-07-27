# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["RegistryUpdateAPIDocumentVersionParams"]


class RegistryUpdateAPIDocumentVersionParams(TypedDict, total=False):

    namespace: Required[str]

    slug: Required[str]

    document: Required[str]

    last_known_version_sha: Annotated[str, PropertyInfo(alias="lastKnownVersionSha")]
