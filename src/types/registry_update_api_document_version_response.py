# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RegistryUpdateAPIDocumentVersionResponse"]


class RegistryUpdateAPIDocumentVersionResponse(BaseModel):
    json_sha: str = FieldInfo(alias="jsonSha")

    yaml_sha: str = FieldInfo(alias="yamlSha")

    version_sha: str = FieldInfo(alias="versionSha")
