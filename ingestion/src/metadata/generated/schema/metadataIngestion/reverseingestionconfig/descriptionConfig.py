# generated by datamodel-codegen:
#   filename:  metadataIngestion/reverseingestionconfig/descriptionConfig.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class ReverseIngestionDescriptionConfig(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    previousDescription: Annotated[
        Optional[str], Field(None, description='Previous description of the service')
    ]
    newDescription: Annotated[
        Optional[str], Field(None, description='New description of the service')
    ]
