# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import TypeAlias
from .._models import BaseModel

__all__ = ["RegistryCreateApiDocumentResponse", "RegistryCreateApiDocumentResponse"]

class RegistryCreateApiDocumentResponse(BaseModel):

    uid: str

    versionUid: str

    title: str

    jsonSha: str

    yamlSha: str

    versionSha: str



RegistryCreateApiDocumentResponse: TypeAlias = RegistryCreateApiDocumentResponse
