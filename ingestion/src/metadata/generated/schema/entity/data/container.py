# generated by datamodel-codegen:
#   filename:  entity/data/container.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ...type import (
    assetCertification,
    basic,
    entityHistory,
    entityReference,
    entityReferenceList,
    lifeCycle,
    tagLabel,
    votes,
)
from ..services import storageService
from . import table


class FileFormat(Enum):
    zip = 'zip'
    gz = 'gz'
    zstd = 'zstd'
    csv = 'csv'
    tsv = 'tsv'
    json = 'json'
    parquet = 'parquet'
    avro = 'avro'


class ContainerDataModel(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    isPartitioned: Annotated[
        Optional[bool],
        Field(
            False,
            description='Whether the data under this container is partitioned by some property, eg. eventTime=yyyy-mm-dd',
        ),
    ]
    columns: Annotated[
        List[table.Column],
        Field(description="Columns belonging to this container's schema"),
    ]


class Container(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Annotated[
        basic.Uuid,
        Field(description='Unique identifier that identifies this container instance.'),
    ]
    name: Annotated[
        basic.EntityName, Field(description='Name that identifies the container.')
    ]
    fullyQualifiedName: Annotated[
        Optional[basic.FullyQualifiedEntityName],
        Field(
            None,
            description="Name that uniquely identifies a container in the format 'ServiceName.ContainerName'.",
        ),
    ]
    displayName: Annotated[
        Optional[str],
        Field(None, description='Display Name that identifies this container.'),
    ]
    description: Annotated[
        Optional[basic.Markdown],
        Field(None, description='Description of the container instance.'),
    ]
    version: Annotated[
        Optional[entityHistory.EntityVersion],
        Field(None, description='Metadata version of the entity.'),
    ]
    updatedAt: Annotated[
        Optional[basic.Timestamp],
        Field(
            None,
            description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
        ),
    ]
    updatedBy: Annotated[
        Optional[str], Field(None, description='User who made the update.')
    ]
    href: Annotated[
        Optional[basic.Href],
        Field(None, description='Link to the resource corresponding to this entity.'),
    ]
    owners: Annotated[
        Optional[entityReferenceList.EntityReferenceList],
        Field(None, description='Owners of this container.'),
    ]
    service: Annotated[
        entityReference.EntityReference,
        Field(
            description='Link to the storage service where this container is hosted in.'
        ),
    ]
    parent: Annotated[
        Optional[entityReference.EntityReference],
        Field(
            None,
            description='Link to the parent container under which this entity sits, if not top level.',
        ),
    ]
    children: Annotated[
        Optional[entityReferenceList.EntityReferenceList],
        Field(
            None,
            description='References to child containers residing under this entity.',
        ),
    ]
    dataModel: Annotated[
        Optional[ContainerDataModel],
        Field(
            None,
            description="References to the container's data model, if data is structured, or null otherwise",
        ),
    ]
    prefix: Annotated[
        Optional[str],
        Field(None, description='Optional prefix path defined for this container'),
    ]
    numberOfObjects: Annotated[
        Optional[float],
        Field(None, description='The number of objects/files this container has.'),
    ]
    size: Annotated[
        Optional[float],
        Field(None, description='The total size in KB this container has.'),
    ]
    fileFormats: Annotated[
        Optional[List[FileFormat]],
        Field(
            None,
            description='File & data formats identified for the container:  e.g. dataFormats=[csv, json]. These can be present both when the container has a dataModel or not',
        ),
    ]
    serviceType: Annotated[
        Optional[storageService.StorageServiceType],
        Field(None, description='Service type this table is hosted in.'),
    ]
    followers: Annotated[
        Optional[entityReferenceList.EntityReferenceList],
        Field(None, description='Followers of this container.'),
    ]
    tags: Annotated[
        Optional[List[tagLabel.TagLabel]],
        Field([], description='Tags for this container.'),
    ]
    changeDescription: Annotated[
        Optional[entityHistory.ChangeDescription],
        Field(None, description='Change that lead to this version of the entity.'),
    ]
    incrementalChangeDescription: Annotated[
        Optional[entityHistory.ChangeDescription],
        Field(None, description='Change that lead to this version of the entity.'),
    ]
    deleted: Annotated[
        Optional[bool],
        Field(
            False, description='When `true` indicates the entity has been soft deleted.'
        ),
    ]
    retentionPeriod: Annotated[
        Optional[basic.Duration],
        Field(
            None,
            description='Retention period of the data in the Container. Period is expressed as duration in ISO 8601 format in UTC. Example - `P23DT23H`.',
        ),
    ]
    extension: Annotated[
        Optional[basic.EntityExtension],
        Field(
            None,
            description='Entity extension data with custom attributes added to the entity.',
        ),
    ]
    sourceUrl: Annotated[
        Optional[basic.SourceUrl], Field(None, description='Source URL of container.')
    ]
    fullPath: Annotated[
        Optional[str], Field(None, description='Full path of the container/file.')
    ]
    domain: Annotated[
        Optional[entityReference.EntityReference],
        Field(
            None,
            description='Domain the Container belongs to. When not set, the Container inherits the domain from the storage service it belongs to.',
        ),
    ]
    dataProducts: Annotated[
        Optional[entityReferenceList.EntityReferenceList],
        Field(None, description='List of data products this entity is part of.'),
    ]
    votes: Annotated[
        Optional[votes.Votes], Field(None, description='Votes on the entity.')
    ]
    lifeCycle: Annotated[
        Optional[lifeCycle.LifeCycle],
        Field(None, description='Life Cycle properties of the entity'),
    ]
    certification: Optional[assetCertification.AssetCertification] = None
    sourceHash: Annotated[
        Optional[str],
        Field(
            None, description='Source hash of the entity', max_length=32, min_length=1
        ),
    ]
