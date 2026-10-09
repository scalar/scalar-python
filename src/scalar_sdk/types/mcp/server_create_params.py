# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

from ..slug import Slug

__all__ = ["ServerCreateParams"]


class ServerCreateParams(TypedDict, total=False):
    name: Required[str]

    slug: Slug

    version_uids: Annotated[SequenceNotStr[str], PropertyInfo(alias="versionUids")]

    project_uids: Annotated[SequenceNotStr[str], PropertyInfo(alias="projectUids")]
