# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScalarDocPublishProjectParams"]


class ScalarDocPublishProjectParams(TypedDict, total=False):
    commit_sha: Annotated[str, PropertyInfo(alias="commitSha")]

    preview: bool

    config_path: Annotated[str, PropertyInfo(alias="configPath")]
