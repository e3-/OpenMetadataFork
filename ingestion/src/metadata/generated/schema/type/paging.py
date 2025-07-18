# generated by datamodel-codegen:
#   filename:  type/paging.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class Paging(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    before: Annotated[
        Optional[str],
        Field(
            None,
            description='Before cursor used for getting the previous page (see API pagination for details).',
        ),
    ]
    after: Annotated[
        Optional[str],
        Field(
            None,
            description='After cursor used for getting the next page (see API pagination for details).',
        ),
    ]
    offset: Annotated[
        Optional[int],
        Field(None, description='Offset used in case of offset based pagination.'),
    ]
    limit: Annotated[
        Optional[int],
        Field(None, description='Limit used in case of offset based pagination.'),
    ]
    total: Annotated[
        int, Field(description='Total number of entries available to page through.')
    ]
