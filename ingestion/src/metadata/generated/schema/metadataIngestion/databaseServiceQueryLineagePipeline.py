# generated by datamodel-codegen:
#   filename:  metadataIngestion/databaseServiceQueryLineagePipeline.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from ..type import filterPattern


class DatabaseLineageConfigType(Enum):
    DatabaseLineage = 'DatabaseLineage'


class DatabaseServiceQueryLineagePipeline(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[DatabaseLineageConfigType],
        Field(DatabaseLineageConfigType.DatabaseLineage, description='Pipeline type'),
    ]
    queryLogDuration: Annotated[
        Optional[int],
        Field(
            1,
            description='Configuration to tune how far we want to look back in query logs to process lineage data.',
            title='Query Log Duration',
        ),
    ]
    queryLogFilePath: Annotated[
        Optional[str],
        Field(
            None,
            description='Configuration to set the file path for query logs',
            title='Query Log File Path',
        ),
    ]
    resultLimit: Annotated[
        Optional[int],
        Field(
            1000,
            description='Configuration to set the limit for query logs',
            title='Result Limit',
        ),
    ]
    parsingTimeoutLimit: Annotated[
        Optional[int],
        Field(
            300,
            description='Configuration to set the timeout for parsing the query in seconds.',
            title='Parsing Timeout Limit',
        ),
    ]
    filterCondition: Annotated[
        Optional[str],
        Field(
            None,
            description='Configuration the condition to filter the query history.',
            title='Filter Condition',
        ),
    ]
    schemaFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to only fetch tables or databases that matches the pattern.',
            title='Schema Filter Pattern',
        ),
    ]
    tableFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex exclude tables or databases that matches the pattern.',
            title='Table Filter Pattern',
        ),
    ]
    databaseFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to only fetch databases that matches the pattern.',
            title='Database Filter Pattern',
        ),
    ]
    storedProcedureFilterPattern: Annotated[
        Optional[filterPattern.FilterPattern],
        Field(
            None,
            description='Regex to only fetch stored procedures that matches the pattern.',
            title='Stored Procedure Filter Pattern',
        ),
    ]
    overrideViewLineage: Annotated[
        Optional[bool],
        Field(
            False,
            description="Set the 'Override View Lineage' toggle to control whether to override the existing view lineage.",
            title='Override View Lineage',
        ),
    ]
    processViewLineage: Annotated[
        Optional[bool],
        Field(
            True,
            description="Set the 'Process View Lineage' toggle to control whether to process view lineage.",
            title='Process View Lineage',
        ),
    ]
    processQueryLineage: Annotated[
        Optional[bool],
        Field(
            True,
            description="Set the 'Process Query Lineage' toggle to control whether to process query lineage.",
            title='Process Query Lineage',
        ),
    ]
    processStoredProcedureLineage: Annotated[
        Optional[bool],
        Field(
            True,
            description="Set the 'Process Stored ProcedureLog Lineage' toggle to control whether to process stored procedure lineage.",
            title='Process Stored Procedure Lineage',
        ),
    ]
    threads: Annotated[
        Optional[int],
        Field(
            1,
            description='Number of Threads to use in order to parallelize lineage ingestion.',
            ge=1,
            title='Number of Threads',
        ),
    ]
    processCrossDatabaseLineage: Annotated[
        Optional[bool],
        Field(
            False,
            description="Set the 'Process Cross Database Lineage' toggle to control whether to process table lineage across different databases.",
            title='Process Cross Database Lineage',
        ),
    ]
    crossDatabaseServiceNames: Annotated[
        Optional[List[str]],
        Field(
            None,
            description="Set 'Cross Database Service Names' to process lineage with the database.",
            title='Cross Database Service Names',
        ),
    ]
    enableTempTableLineage: Annotated[
        Optional[bool],
        Field(
            False,
            description='Handle Lineage for Snowflake Temporary and Transient Tables. ',
            title='Enable Temp Table Lineage',
        ),
    ]
    incrementalLineageProcessing: Annotated[
        Optional[bool],
        Field(
            True,
            description="Set the 'Incremental Lineage Processing' toggle to control whether to process lineage incrementally.",
            title='Incremental Lineage Processing',
        ),
    ]
