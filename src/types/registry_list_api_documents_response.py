# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypeAlias
from .._models import BaseModel
from .version import Version
from .slug import Slug

__all__ = ["RegistryListApiDocumentsResponse", "ApiDocument", "ManagedDocVersion", "Tool"]

class Tool(BaseModel):

    path: str

    method: Literal["delete", "get", "head", "options", "patch", "post", "put", "trace"]

    enabledTools: List[Literal["execute-request", "get-mini-openapi-spec"]]

class ManagedDocVersion(BaseModel):

    uid: str

    createdAt: float

    version: Version

    upgraded: bool

    embedStatus: Optional[Literal["complete", "failed"]] = None

    tags: List[str]

    tools: Optional[List[Tool]] = None

    yamlSha: Optional[str] = None

    jsonSha: Optional[str] = None

    versionSha: Optional[str] = None

class ApiDocument(BaseModel):

    uid: str

    version: Version

    title: str

    slug: Slug

    description: str

    namespace: str

    isPrivate: bool

    tags: object

    versions: List[ManagedDocVersion]



RegistryListApiDocumentsResponse: TypeAlias = List[ApiDocument]
