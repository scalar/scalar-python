# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .shared.nanoid import Nanoid
from .shared.timestamp import Timestamp
from .version import Version

__all__ = ["ManagedSchemaVersion"]


class ManagedSchemaVersion(BaseModel):
    uid: Nanoid

    created_at: Timestamp = FieldInfo(alias="createdAt")

    updated_at: Timestamp = FieldInfo(alias="updatedAt")

    version: Version

    yaml_sha: Optional[str] = FieldInfo(alias="yamlSha", default=None)

    json_sha: Optional[str] = FieldInfo(alias="jsonSha", default=None)
