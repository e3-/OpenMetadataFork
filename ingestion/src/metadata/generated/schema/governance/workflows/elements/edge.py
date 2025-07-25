# generated by datamodel-codegen:
#   filename:  governance/workflows/elements/edge.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class EdgeDefinition(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    from_: Annotated[
        str, Field(alias='from', description='Element from which the edge will start.')
    ]
    to: Annotated[str, Field(description='Element on which the edge will end.')]
    condition: Annotated[
        Optional[str],
        Field(
            None,
            description='Defines if the edge will follow a path depending on the source node result.',
        ),
    ]
