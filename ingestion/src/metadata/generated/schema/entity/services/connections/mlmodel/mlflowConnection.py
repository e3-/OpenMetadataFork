# generated by datamodel-codegen:
#   filename:  entity/services/connections/mlmodel/mlflowConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from .....type import filterPattern
from .. import connectionBasicType


class MlflowType(Enum):
    Mlflow = 'Mlflow'


class MlflowConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[MlflowType],
        Field(MlflowType.Mlflow, description='Service Type', title='Service Type'),
    ]
    trackingUri: Annotated[
        str,
        Field(
            description='Mlflow Experiment tracking URI. E.g., http://localhost:5000',
            title='Tracking URI',
        ),
    ]
    registryUri: Annotated[
        str,
        Field(
            description='Mlflow Model registry backend. E.g., mysql+pymysql://mlflow:password@localhost:3307/experiments',
            title='Registry URI',
        ),
    ]
    mlModelFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to only fetch MlModels with names matching the pattern.',
            title='Default ML Model Filter Pattern',
        ),
    ]
    supportsMetadataExtraction: Annotated[
        Optional[connectionBasicType.SupportsMetadataExtraction],
        Field(None, title='Supports Metadata Extraction'),
    ]
