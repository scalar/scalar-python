# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .slug import Slug

__all__ = ["ScalarDocListGuidesResponse", "GithubProject", "ActiveDeployment", "GithubProjectRepository"]

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

class ActiveDeployment(BaseModel):

    uid: str

    domain: str

    published_at: int = FieldInfo(alias="publishedAt")

class GithubProject(BaseModel):

    uid: str

    created_at: int = FieldInfo(alias="createdAt")

    updated_at: int = FieldInfo(alias="updatedAt")

    name: str

    active_deployment: Optional[ActiveDeployment] = FieldInfo(alias="activeDeployment", default=None)

    last_published: Optional[int] = FieldInfo(alias="lastPublished", default=None)

    last_published_uid: Optional[str] = FieldInfo(alias="lastPublishedUid", default=None)

    login_portal_uid: str = FieldInfo(alias="loginPortalUid")

    active_theme_id: str = FieldInfo(alias="activeThemeId")

    typesense_id: Optional[float] = FieldInfo(alias="typesenseId", default=None)

    is_private: bool = FieldInfo(alias="isPrivate")

    agent_enabled: bool = FieldInfo(alias="agentEnabled")

    access_groups: object = FieldInfo(alias="accessGroups")

    slug: Slug

    publish_status: str = FieldInfo(alias="publishStatus")

    publish_message: str = FieldInfo(alias="publishMessage")

    repository: Optional[GithubProjectRepository] = None



ScalarDocListGuidesResponse: TypeAlias = List[GithubProject]
