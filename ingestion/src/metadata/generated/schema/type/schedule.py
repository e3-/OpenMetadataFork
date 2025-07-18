# generated by datamodel-codegen:
#   filename:  type/schedule.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from . import basic


class Schedule(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    startDate: Annotated[
        Optional[basic.DateTime],
        Field(None, description='Start date and time of the schedule.'),
    ]
    repeatFrequency: Annotated[
        Optional[basic.Duration],
        Field(
            None,
            description="Repeat frequency in ISO 8601 duration format. Example - 'P23DT23H'.",
        ),
    ]
