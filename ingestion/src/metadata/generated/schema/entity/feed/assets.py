# generated by datamodel-codegen:
#   filename:  entity/feed/assets.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict

from metadata.ingestion.models.custom_pydantic import BaseModel

from ...type import entityReferenceList


class AssetsFeedInfo(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    updatedAssets: Optional[entityReferenceList.EntityReferenceList] = None
