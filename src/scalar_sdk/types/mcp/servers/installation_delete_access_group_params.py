# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ...._utils import PropertyInfo

from ...shared.nanoid import Nanoid

__all__ = ["InstallationDeleteAccessGroupParams"]


class InstallationDeleteAccessGroupParams(TypedDict, total=False):
    id: Required[str]

    access_group_uid: Required[Annotated[Nanoid, PropertyInfo(alias="accessGroupUid")]]
