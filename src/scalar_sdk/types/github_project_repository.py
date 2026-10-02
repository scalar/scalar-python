# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["GithubProjectRepository"]


class GithubProjectRepository(BaseModel):
    linked_by: str = FieldInfo(alias="linkedBy")

    id: float

    name: str

    config_path: str = FieldInfo(alias="configPath")

    branch: str

    publish_on_merge: bool = FieldInfo(alias="publishOnMerge")

    publish_previews: bool = FieldInfo(alias="publishPreviews")

    pr_comments: bool = FieldInfo(alias="prComments")

    expired: bool
