# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .slug import Slug
from .shared.timestamp import Timestamp

__all__ = ["DocsProject"]


class DocsProject(BaseModel):
    uid: Nanoid

    name: str

    slug: Slug

    is_private: bool = FieldInfo(alias="isPrivate")

    access_groups: str = FieldInfo(alias="accessGroups")

    login_portal_uid: str = FieldInfo(alias="loginPortalUid")

    active_theme_id: str = FieldInfo(alias="activeThemeId")

    agent_enabled: bool = FieldInfo(alias="agentEnabled")

    analytics_enabled: bool = FieldInfo(alias="analyticsEnabled")

    last_published: Optional[Timestamp] = FieldInfo(alias="lastPublished", default=None)

    publish_status: str = FieldInfo(alias="publishStatus")
