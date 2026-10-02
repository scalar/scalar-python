# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .slug import Slug
from .shared.namespace import Namespace
from .version import Version
from .sdk_target_summary import SdkTargetSummary
from .sdk_version import SdkVersion

__all__ = ["Sdk"]


class Sdk(BaseModel):
    uid: Nanoid

    title: str

    slug: Slug

    namespace: Namespace

    description: str

    is_private: bool = FieldInfo(alias="isPrivate")

    api_uid: Optional[Nanoid] = FieldInfo(alias="apiUid", default=None)

    api_version: Optional[Version] = FieldInfo(alias="apiVersion", default=None)

    current_version: Version = FieldInfo(alias="currentVersion")

    targets: List[SdkTargetSummary]

    versions: List[SdkVersion]
