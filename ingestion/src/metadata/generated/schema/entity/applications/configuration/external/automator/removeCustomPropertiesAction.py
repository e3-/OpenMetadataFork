# generated by datamodel-codegen:
#   filename:  entity/applications/configuration/external/automator/removeCustomPropertiesAction.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class RemoveCustomPropertiesActionType(Enum):
    RemoveCustomPropertiesAction = 'RemoveCustomPropertiesAction'


class RemoveCustomPropertiesAction(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        RemoveCustomPropertiesActionType,
        Field(description='Application Type', title='Application Type'),
    ]
    customProperties: Annotated[
        List[str], Field(description='Custom Properties keys to remove')
    ]
