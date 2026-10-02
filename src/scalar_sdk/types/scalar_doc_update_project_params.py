# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, Literal, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

from .shared.nanoid import Nanoid

__all__ = ["ScalarDocUpdateProjectParams"]


class ScalarDocUpdateProjectParams(TypedDict, total=False):
    name: str

    is_private: Annotated[bool, PropertyInfo(alias="isPrivate")]

    access_groups: Annotated[SequenceNotStr[Nanoid], PropertyInfo(alias="accessGroups")]

    login_portal_uid: Annotated[Union[Nanoid, Literal[""]], PropertyInfo(alias="loginPortalUid")]

    active_theme_id: Annotated[Nanoid, PropertyInfo(alias="activeThemeId")]

    agent_enabled: Annotated[bool, PropertyInfo(alias="agentEnabled")]

    analytics_enabled: Annotated[bool, PropertyInfo(alias="analyticsEnabled")]
