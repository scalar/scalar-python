# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .docs_project import DocsProject

__all__ = ["ScalarDocListProjectsResponse"]


class ScalarDocListProjectsResponse(BaseModel):
    data: List[DocsProject]

    has_more: bool = FieldInfo(alias="hasMore")
