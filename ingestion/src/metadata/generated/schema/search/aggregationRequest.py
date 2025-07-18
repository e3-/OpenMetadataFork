# generated by datamodel-codegen:
#   filename:  search/aggregationRequest.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class SortOrder(Enum):
    asc = 'asc'
    desc = 'desc'


class TopHits(BaseModel):
    size: Annotated[
        Optional[int],
        Field(1, description='Number of top documents to return per bucket.'),
    ]
    sortField: Annotated[
        Optional[str], Field('_doc', description='Field to sort the top hits on.')
    ]
    sortOrder: Annotated[
        Optional[SortOrder],
        Field(SortOrder.asc, description='Sort order for top hits - asc or desc.'),
    ]


class AggregationRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    query: Annotated[
        Optional[str],
        Field('', description='Query string to be sent to the search engine.'),
    ]
    index: Annotated[
        Optional[str],
        Field('table_search_index', description='Name of the index to aggregate on.'),
    ]
    fieldName: Annotated[
        str,
        Field(
            description='Field name to aggregate on (typically a keyword field like service.displayName.keyword).'
        ),
    ]
    fieldValue: Annotated[
        Optional[str],
        Field('', description='Filter value for the aggregation include clause.'),
    ]
    deleted: Annotated[
        Optional[bool],
        Field(False, description='Whether to include deleted documents.'),
    ]
    size: Annotated[
        Optional[int],
        Field(
            10, description='Size to limit the number of aggregation buckets returned.'
        ),
    ]
    sourceFields: Annotated[
        Optional[List[str]],
        Field(
            None,
            description='List of fields to include from _source in the response (outside of top_hits).',
        ),
    ]
    topHits: Annotated[
        Optional[TopHits],
        Field(
            {'size': 1, 'sortField': '_doc', 'sortOrder': 'asc'},
            description='Optional top_hits sub-aggregation to fetch selected source fields per bucket.',
        ),
    ]
