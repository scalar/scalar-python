# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import TypeAlias
from .._models import BaseModel

__all__ = ["RegistryUpdateApiDocumentVersionResponse", "RegistryUpdateApiDocumentVersionResponse"]

class RegistryUpdateApiDocumentVersionResponse(BaseModel):

    jsonSha: str

    yamlSha: str

    versionSha: str



RegistryUpdateApiDocumentVersionResponse: TypeAlias = RegistryUpdateApiDocumentVersionResponse
