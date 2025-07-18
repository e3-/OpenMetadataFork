# generated by datamodel-codegen:
#   filename:  entity/services/ingestionPipelines/status.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import ConfigDict, Field, RootModel
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class IngestionStatusModel(RootModel[Any]):
    root: Annotated[
        Any,
        Field(description='Ingestion detailed status', title='IngestionStatusModel'),
    ]


class StackTraceError(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: Annotated[str, Field(description='Name of the asset with the error')]
    error: Annotated[str, Field(description='Error being handled')]
    stackTrace: Annotated[
        Optional[str], Field(None, description='Exception stack trace')
    ]


class StepSummary(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: Annotated[str, Field(description='Step name')]
    records: Annotated[
        Optional[int], Field(0, description='Number of successfully processed records.')
    ]
    updated_records: Annotated[
        Optional[int], Field(0, description='Number of successfully updated records.')
    ]
    warnings: Annotated[
        Optional[int], Field(0, description='Number of records raising warnings.')
    ]
    errors: Annotated[
        Optional[int], Field(0, description='Number of records with errors.')
    ]
    filtered: Annotated[
        Optional[int], Field(0, description='Number of filtered records.')
    ]
    failures: Annotated[
        Optional[List[StackTraceError]],
        Field(None, description='Sample of errors encountered in the step'),
    ]


class IngestionStatus(RootModel[List[StepSummary]]):
    root: Annotated[
        List[StepSummary],
        Field(
            description='Summary for each step of the ingestion pipeline',
            title='IngestionStatus',
        ),
    ]
