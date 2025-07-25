# generated by datamodel-codegen:
#   filename:  events/eventSubscriptionOffset.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ..type import basic


class EventSubscriptionOffset(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    startingOffset: Annotated[
        int, Field(description='The offset from where event processing starts.')
    ]
    currentOffset: Annotated[
        int, Field(description='The current position in the events.')
    ]
    timestamp: Annotated[
        Optional[basic.Timestamp],
        Field(None, description='Update time of the job status.'),
    ]
