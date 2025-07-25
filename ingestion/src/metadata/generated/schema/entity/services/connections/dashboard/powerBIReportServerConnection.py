# generated by datamodel-codegen:
#   filename:  entity/services/connections/dashboard/powerBIReportServerConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import AnyUrl, ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr

from .....type import filterPattern
from .. import connectionBasicType


class PowerBIReportServerType(Enum):
    PowerBIReportServer = 'PowerBIReportServer'


class PowerBIReportServerConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[PowerBIReportServerType],
        Field(
            PowerBIReportServerType.PowerBIReportServer,
            description='Service Type',
            title='Service Type',
        ),
    ]
    hostPort: Annotated[
        AnyUrl,
        Field(
            description='Dashboard URL for PowerBI Report Server.',
            title='Host and Port',
        ),
    ]
    username: Annotated[
        str,
        Field(
            description='Username to connect to PowerBI report server.',
            title='Username',
        ),
    ]
    password: Annotated[
        CustomSecretStr,
        Field(
            description='Password to connect to PowerBI report server.',
            title='Password',
        ),
    ]
    webPortalVirtualDirectory: Annotated[
        Optional[str],
        Field(
            'Reports',
            description='Web Portal Virtual Directory Name.',
            title='Web Portal Virtual Directory Name',
        ),
    ]
    supportsMetadataExtraction: Annotated[
        Optional[connectionBasicType.SupportsMetadataExtraction],
        Field(None, title='Supports Metadata Extraction'),
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
