# generated by datamodel-codegen:
#   filename:  entity/datacontract/qualityValidation.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class QualityValidation(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    passed: Annotated[
        Optional[int], Field(None, description='Number of quality checks passed.')
    ]
    failed: Annotated[
        Optional[int], Field(None, description='Number of quality checks failed.')
    ]
    total: Annotated[
        Optional[int], Field(None, description='Total number of quality checks.')
    ]
    qualityScore: Annotated[
        Optional[float],
        Field(None, description='Overall quality score (0-100).', ge=0.0, le=100.0),
    ]
