# generated by datamodel-codegen:
#   filename:  auth/createPersonalToken.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from . import jwtAuth


class CreatePersonalToken(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    tokenName: Annotated[str, Field(description='Name of the Personal Access Token')]
    JWTTokenExpiry: jwtAuth.JWTTokenExpiry
