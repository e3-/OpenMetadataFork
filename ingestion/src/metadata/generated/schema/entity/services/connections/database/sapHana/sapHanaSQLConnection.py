# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/sapHana/sapHanaSQLConnection.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr


class SapHanaSQLConnection(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    hostPort: Annotated[
        str,
        Field(description='Host and port of the Hana service.', title='Host and Port'),
    ]
    username: Annotated[
        str,
        Field(
            description='Username to connect to Hana. This user should have privileges to read all the metadata.',
            title='Username',
        ),
    ]
    password: Annotated[
        CustomSecretStr,
        Field(description='Password to connect to Hana.', title='Password'),
    ]
    databaseSchema: Annotated[
        Optional[str],
        Field(
            None,
            description='Database Schema of the data source. This is an optional parameter, if you would like to restrict the metadata reading to a single schema. When left blank, OpenMetadata Ingestion attempts to scan all the schemas.',
            title='Database Schema',
        ),
    ]
    database: Annotated[
        Optional[str],
        Field(None, description='Database of the data source.', title='Database'),
    ]
