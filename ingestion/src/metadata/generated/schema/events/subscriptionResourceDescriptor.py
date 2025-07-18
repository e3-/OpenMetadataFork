# generated by datamodel-codegen:
#   filename:  events/subscriptionResourceDescriptor.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class Operation(Enum):
    filterBySource = 'filterBySource'
    filterByEntityId = 'filterByEntityId'
    filterByOwnerName = 'filterByOwnerName'
    filterByFqn = 'filterByFqn'
    filterByEventType = 'filterByEventType'
    filterByUpdaterName = 'filterByUpdaterName'
    filterByFieldChange = 'filterByFieldChange'
    filterByDomain = 'filterByDomain'
    filterByMentionedName = 'filterByMentionedName'
    filterByGeneralMetadataEvents = 'filterByGeneralMetadataEvents'
    filterByUpdaterIsBot = 'filterByUpdaterIsBot'


class SubscriptionResourceDescriptor(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: Annotated[
        Optional[str],
        Field(
            None,
            description='Name of the resource. For entity related resources, resource name is same as the entity name. Some resources such as lineage are not entities but are resources.',
        ),
    ]
    supportedFilters: Annotated[
        Optional[List[Operation]],
        Field(
            None, description='List of operations supported filters by the resource.'
        ),
    ]
