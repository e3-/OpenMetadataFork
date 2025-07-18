# generated by datamodel-codegen:
#   filename:  entity/applications/configuration/internal/helloPipelinesConfiguration.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class HelloPipelinesAppConfiguration(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    sleep: Annotated[int, Field(title='Sleep time (seconds)')]
    echo: Annotated[str, Field(title='Echo message')]
