# generated by datamodel-codegen:
#   filename:  governance/workflows/elements/triggers/periodicBatchEntityTrigger.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from .....entity.applications import app


class Config(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    schedule: Annotated[
        app.AppSchedule,
        Field(description='Defines the schedule of the Periodic Trigger.'),
    ]
    entityType: Annotated[
        str,
        Field(
            description='Entity Type for which it should be triggered.',
            title='Entity Type',
        ),
    ]
    filters: Annotated[
        str,
        Field(
            description='Select the Search Filters to filter down the entities fetched.',
            title='Filters',
        ),
    ]
    batchSize: Annotated[
        Optional[int],
        Field(
            500,
            description='Number of Entities to process at once.',
            title='Batch Size',
        ),
    ]


class PeriodicBatchEntityTriggerDefinition(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Optional[str] = 'periodicBatchEntity'
    config: Optional[Config] = None
    output: Annotated[
        Optional[List[str]], Field(['relatedEntity'], max_length=1, min_length=1)
    ]
