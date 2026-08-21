# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .shared.timestamp import Timestamp
from .slug import Slug

__all__ = [
    "ScalarDocListGuidesResponse",
    "ScalarDocListGuidesResponseItem",
    "ScalarDocListGuidesResponseItemActiveDeployment",
    "ScalarDocListGuidesResponseItemRepository",
]


class ScalarDocListGuidesResponseItemRepository(BaseModel):
    linked_by: str = FieldInfo(alias="linkedBy")

    id: float

    name: str

    config_path: str = FieldInfo(alias="configPath")

    branch: str

    publish_on_merge: bool = FieldInfo(alias="publishOnMerge")

    publish_previews: bool = FieldInfo(alias="publishPreviews")

    pr_comments: bool = FieldInfo(alias="prComments")

    expired: bool


class ScalarDocListGuidesResponseItemActiveDeployment(BaseModel):
    uid: str

    domain: str

    published_at: Timestamp = FieldInfo(alias="publishedAt")


class ScalarDocListGuidesResponseItem(BaseModel):
    uid: Nanoid

    created_at: Timestamp = FieldInfo(alias="createdAt")

    updated_at: Timestamp = FieldInfo(alias="updatedAt")

    name: str

    active_deployment: Optional[ScalarDocListGuidesResponseItemActiveDeployment] = FieldInfo(
        alias="activeDeployment", default=None
    )

    last_published: Optional[Timestamp] = FieldInfo(alias="lastPublished", default=None)

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

    repository: Optional[ScalarDocListGuidesResponseItemRepository] = None


ScalarDocListGuidesResponse: TypeAlias = List[ScalarDocListGuidesResponseItem]
