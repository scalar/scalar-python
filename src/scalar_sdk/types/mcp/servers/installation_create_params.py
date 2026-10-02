# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, Required, TypedDict

from ...._utils import PropertyInfo

from ...slug import Slug

__all__ = ["InstallationCreateParams"]


class InstallationCreateParams(TypedDict, total=False):
    name: Required[str]

    slug: Slug

    document_auth: Required[Annotated[Dict[str, object], PropertyInfo(alias="documentAuth")]]
