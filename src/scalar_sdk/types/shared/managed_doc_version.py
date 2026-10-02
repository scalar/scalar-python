# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .nanoid import Nanoid
from ..version import Version
from ..method import Method

__all__ = ["ManagedDocVersion", "Tool"]


class Tool(BaseModel):
    path: str

    method: Method

    enabled_tools: List[Literal["execute-request", "get-mini-openapi-spec"]] = FieldInfo(alias="enabledTools")


class ManagedDocVersion(BaseModel):
    uid: Nanoid

    created_at: float = FieldInfo(alias="createdAt")

    version: Version

    upgraded: bool

    endpoint_count: Optional[int] = FieldInfo(alias="endpointCount", default=None)

    embed_status: Optional[Literal["complete", "failed"]] = FieldInfo(alias="embedStatus", default=None)

    tags: List[str]

    tools: Optional[List[Tool]] = None

    yaml_sha: Optional[str] = FieldInfo(alias="yamlSha", default=None)

    json_sha: Optional[str] = FieldInfo(alias="jsonSha", default=None)
