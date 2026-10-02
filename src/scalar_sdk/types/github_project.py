# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .shared.timestamp import Timestamp
from .active_deployment import ActiveDeployment
from .slug import Slug
from .github_project_repository import GithubProjectRepository

__all__ = ["GithubProject"]


class GithubProject(BaseModel):
    uid: Nanoid

    created_at: Timestamp = FieldInfo(alias="createdAt")

    updated_at: Timestamp = FieldInfo(alias="updatedAt")

    name: str

    active_deployment: Optional[ActiveDeployment] = FieldInfo(alias="activeDeployment", default=None)

    last_published: Optional[Timestamp] = FieldInfo(alias="lastPublished", default=None)

    last_published_uid: Optional[str] = FieldInfo(alias="lastPublishedUid", default=None)

    login_portal_uid: str = FieldInfo(alias="loginPortalUid")

    user_info_hook_url: str = FieldInfo(alias="userInfoHookUrl")

    active_theme_id: str = FieldInfo(alias="activeThemeId")

    typesense_id: Optional[float] = FieldInfo(alias="typesenseId", default=None)

    is_private: bool = FieldInfo(alias="isPrivate")

    agent_enabled: bool = FieldInfo(alias="agentEnabled")

    analytics_enabled: bool = FieldInfo(alias="analyticsEnabled")

    access_groups: str = FieldInfo(alias="accessGroups")

    slug: Slug

    publish_status: str = FieldInfo(alias="publishStatus")

    publish_message: str = FieldInfo(alias="publishMessage")

    repository: Optional[GithubProjectRepository] = None
