# generated by datamodel-codegen:
#   filename:  entity/services/connections/dashboard/supersetConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from .....type import filterPattern
from ....utils import supersetApiConnection
from .. import connectionBasicType
from ..database import mysqlConnection, postgresConnection


class SupersetType(Enum):
    Superset = 'Superset'


class SupersetConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[SupersetType],
        Field(SupersetType.Superset, description='Service Type', title='Service Type'),
    ]
    hostPort: Annotated[
        AnyUrl,
        Field(description='URL for the superset instance.', title='Host and Port'),
    ]
    connection: Annotated[
        Union[
            supersetApiConnection.SupersetApiConnection,
            postgresConnection.PostgresConnection,
            mysqlConnection.MysqlConnection,
        ],
        Field(
            description='Choose between API or database connection fetch metadata from superset.',
            title='Superset Connection',
        ),
    ]
    dashboardFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to exclude or include dashboards that matches the pattern.',
            title='Default Dashboard Filter Pattern',
        ),
    ]
    chartFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex exclude or include charts that matches the pattern.',
            title='Default Chart Filter Pattern',
        ),
    ]
    dataModelFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex exclude or include data models that matches the pattern.',
            title='Default Data Model Filter Pattern',
        ),
    ]
    projectFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to exclude or include projects that matches the pattern.',
            title='Default Project Filter Pattern',
        ),
    ]
    supportsMetadataExtraction: Annotated[
        Optional[connectionBasicType.SupportsMetadataExtraction],
        Field(None, title='Supports Metadata Extraction'),
    ]
