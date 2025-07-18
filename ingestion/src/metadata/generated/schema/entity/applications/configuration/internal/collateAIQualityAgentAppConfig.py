# generated by datamodel-codegen:
#   filename:  entity/applications/configuration/internal/collateAIQualityAgentAppConfig.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class CollateAIQualityAgentAppType(Enum):
    CollateAIQualityAgent = 'CollateAIQualityAgent'


class CollateaiqualityagentappconfigJson(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[CollateAIQualityAgentAppType],
        Field(
            CollateAIQualityAgentAppType.CollateAIQualityAgent,
            description='Application Type',
            title='Application Type',
        ),
    ]
    filter: Annotated[
        str,
        Field(
            description='Query filter to be passed to ES. E.g., `{"query":{"bool":{"must":[{"bool":{"should":[{"term":{"domain.displayName.keyword":"DG Anim"}}]}}]}}}`. This is the same payload as in the Explore page.',
            title='Filter',
        ),
    ]
    active: Annotated[
        Optional[bool],
        Field(
            False,
            description='Whether the suggested tests should be active or not upon suggestion',
            title='Active',
        ),
    ]
