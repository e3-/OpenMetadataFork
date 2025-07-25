# generated by datamodel-codegen:
#   filename:  type/queryParserData.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class ParsedData(BaseModel):
    tables: Annotated[List[str], Field(description='List of tables used in query')]
    databaseName: Annotated[
        Optional[str],
        Field(None, description='Database associated with the table in the query'),
    ]
    joins: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            description='Maps each parsed table name of a query to the join information',
        ),
    ]
    sql: Annotated[str, Field(description='SQL query')]
    dialect: Annotated[Optional[str], Field(None, description='SQL dialect')]
    query_type: Annotated[Optional[str], Field(None, description='SQL query type')]
    exclude_usage: Annotated[
        Optional[bool],
        Field(
            None,
            description='Flag to check if query is to be excluded while processing usage',
        ),
    ]
    serviceName: Annotated[
        str, Field(description='Name that identifies this database service.')
    ]
    userName: Annotated[
        Optional[str],
        Field(None, description='Name of the user that executed the SQL query'),
    ]
    date: Annotated[
        Optional[str], Field(None, description='Date of execution of SQL query')
    ]
    databaseSchema: Annotated[
        Optional[str],
        Field(None, description='Database schema of the associated with query'),
    ]
    duration: Annotated[
        Optional[float],
        Field(None, description='How long did the query took to run in milliseconds.'),
    ]
    cost: Annotated[
        Optional[float], Field(None, description='Cost of the query execution')
    ]


class QueryParserData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    parsedData: Optional[List[ParsedData]] = None
