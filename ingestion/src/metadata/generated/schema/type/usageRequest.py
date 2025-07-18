# generated by datamodel-codegen:
#   filename:  type/usageRequest.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class UsageRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    date: Annotated[str, Field(description='Date of execution of SQL query')]
    count: Annotated[int, Field(description='Usage count of table')]
