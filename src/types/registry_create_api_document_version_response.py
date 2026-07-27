# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .version import Version

__all__ = ["RegistryCreateAPIDocumentVersionResponse", "Tool"]


class Tool(BaseModel):

    path: str

    method: Literal["delete", "get", "head", "options", "patch", "post", "put", "trace"]

    enabled_tools: List[Literal["execute-request", "get-mini-openapi-spec"]] = FieldInfo(alias="enabledTools")



class RegistryCreateAPIDocumentVersionResponse(BaseModel):

    uid: str

    created_at: float = FieldInfo(alias="createdAt")

    version: Version

    upgraded: bool

    embed_status: Optional[Literal["complete", "failed"]] = FieldInfo(alias="embedStatus", default=None)

    tags: List[str]

    tools: Optional[List[Tool]] = None

    yaml_sha: Optional[str] = FieldInfo(alias="yamlSha", default=None)

    json_sha: Optional[str] = FieldInfo(alias="jsonSha", default=None)

    version_sha: Optional[str] = FieldInfo(alias="versionSha", default=None)
