# generated by datamodel-codegen:
#   filename:  api/tests/createCustomMetric.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ...type import basic, entityReferenceList


class CreateCustomMetricRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    description: Annotated[
        Optional[basic.Markdown],
        Field(None, description='Description of the custom metric.'),
    ]
    name: Annotated[
        basic.EntityName, Field(description='Name that identifies this Custom Metric.')
    ]
    columnName: Annotated[
        Optional[str], Field(None, description='Name of the column in a table.')
    ]
    expression: Annotated[
        str,
        Field(
            description='SQL expression to compute the Metric. It should return a single numerical value.'
        ),
    ]
    owners: Annotated[
        Optional[entityReferenceList.EntityReferenceList],
        Field(None, description='Owners of this Pipeline.'),
    ]
    updatedAt: Annotated[
        Optional[basic.Timestamp],
        Field(
            None,
            description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
        ),
    ]
    updatedBy: Annotated[
        Optional[str], Field(None, description='User who made the update.')
    ]
