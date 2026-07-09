# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypeAlias
from .._models import BaseModel
from .slug import Slug

__all__ = ["ScalarDocListGuidesResponse", "GithubProject", "ActiveDeployment", "GithubProjectRepository"]

class GithubProjectRepository(BaseModel):

    linkedBy: str

    id: float

    name: str

    configPath: str

    branch: str

    publishOnMerge: bool

    publishPreviews: bool

    prComments: bool

    expired: bool

class ActiveDeployment(BaseModel):

    uid: str

    domain: str

    publishedAt: int

class GithubProject(BaseModel):

    uid: str

    createdAt: int

    updatedAt: int

    name: str

    activeDeployment: Optional[ActiveDeployment] = None

    lastPublished: Optional[int] = None

    lastPublishedUid: Optional[str] = None

    loginPortalUid: str

    activeThemeId: str

    typesenseId: Optional[float] = None

    isPrivate: bool

    agentEnabled: bool

    accessGroups: object

    slug: Slug

    publishStatus: str

    publishMessage: str

    repository: Optional[GithubProjectRepository] = None



ScalarDocListGuidesResponse: TypeAlias = List[GithubProject]
