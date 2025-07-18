# generated by datamodel-codegen:
#   filename:  api/openMetadataServerVersion.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ..type import basic


class OpenMetadataServerVersion(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    version: Annotated[
        Optional[str],
        Field(None, description='Software version of the OpenMetadata Server'),
    ]
    revision: Annotated[
        Optional[str],
        Field(None, description='Software revision of the OpenMetadata Server'),
    ]
    timestamp: Annotated[
        Optional[basic.Timestamp], Field(None, description='Build timestamp')
    ]
