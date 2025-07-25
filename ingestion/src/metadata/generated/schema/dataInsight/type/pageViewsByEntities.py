# generated by datamodel-codegen:
#   filename:  dataInsight/type/pageViewsByEntities.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ...type import basic


class PageViewsByEntities(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    timestamp: Annotated[
        Optional[basic.Timestamp], Field(None, description='timestamp')
    ]
    pageViews: Annotated[
        Optional[float], Field(None, description='Number of page views')
    ]
    entityType: Annotated[
        Optional[str],
        Field(None, description='Type of entity. Derived from the page URL.'),
    ]
