# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias
from .github_project import GithubProject

__all__ = ["ScalarDocListGuidesResponse"]

ScalarDocListGuidesResponse: TypeAlias = List[GithubProject]
