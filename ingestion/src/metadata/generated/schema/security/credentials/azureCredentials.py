# generated by datamodel-codegen:
#   filename:  security/credentials/azureCredentials.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel, CustomSecretStr


class AzureCredentials(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    clientId: Annotated[
        Optional[str],
        Field(
            None,
            description='Your Service Principal App ID (Client ID)',
            title='Client ID',
        ),
    ]
    clientSecret: Annotated[
        Optional[CustomSecretStr],
        Field(
            None,
            description='Your Service Principal Password (Client Secret)',
            title='Client Secret',
        ),
    ]
    tenantId: Annotated[
        Optional[str],
        Field(
            None, description='Tenant ID of your Azure Subscription', title='Tenant ID'
        ),
    ]
    accountName: Annotated[
        Optional[str],
        Field(
            None,
            description='Account Name of your storage account',
            title='Storage Account Name',
        ),
    ]
    vaultName: Annotated[
        Optional[str], Field(None, description='Key Vault Name', title='Key Vault Name')
    ]
    scopes: Annotated[
        Optional[str],
        Field(
            None,
            description='Scopes to get access token, for e.g. api://6dfX33ab-XXXX-49df-XXXX-3459eX817d3e/.default',
            title='Scopes',
        ),
    ]
