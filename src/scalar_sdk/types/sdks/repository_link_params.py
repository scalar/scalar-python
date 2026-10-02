# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RepositoryLinkParams"]


class RepositoryLinkParams(TypedDict, total=False):
    language: Required[
        Literal[
            "typescript",
            "python",
            "cli",
            "csharp",
            "java",
            "ruby",
            "php",
            "go",
            "rust",
            "kotlin",
            "swift",
            "cpp",
            "dart",
        ]
    ]

    repository_id: Required[Annotated[int, PropertyInfo(alias="repositoryId")]]

    base_branch: Required[Annotated[str, PropertyInfo(alias="baseBranch")]]

    prerelease_type: Annotated[str, PropertyInfo(alias="prereleaseType")]
