# generated by datamodel-codegen:
#   filename:  auth/revokeToken.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from pydantic import ConfigDict

from metadata.ingestion.models.custom_pydantic import BaseModel

from ..type import basic


class GenerateJwtTokenRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: basic.Uuid
