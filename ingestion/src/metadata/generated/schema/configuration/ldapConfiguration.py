# generated by datamodel-codegen:
#   filename:  configuration/ldapConfiguration.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel

from .ldapTrustStoreConfig import truststoreConfig


class TruststoreConfigType(Enum):
    TrustAll = 'TrustAll'
    JVMDefault = 'JVMDefault'
    HostName = 'HostName'
    CustomTrustStore = 'CustomTrustStore'


class LdapConfiguration(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    host: Annotated[
        str,
        Field(description='LDAP server address without scheme(Example :- localhost)'),
    ]
    port: Annotated[int, Field(description='Port of the server')]
    maxPoolSize: Annotated[
        Optional[int], Field(3, description='No of connection to create the pool with')
    ]
    isFullDn: Annotated[
        Optional[bool],
        Field(False, description='If enable need to give full dn to login'),
    ]
    dnAdminPrincipal: Annotated[
        str, Field(description='Distinguished Admin name with search capabilities')
    ]
    dnAdminPassword: Annotated[str, Field(description='Password for LDAP Admin')]
    sslEnabled: Annotated[
        Optional[bool], Field(False, description='LDAPS (secure LDAP) or LDAP')
    ]
    userBaseDN: Annotated[str, Field(description='User base distinguished name')]
    groupBaseDN: Annotated[
        Optional[str], Field(None, description='Group base distinguished name')
    ]
    roleAdminName: Annotated[Optional[str], Field(None, description='Admin role name')]
    allAttributeName: Annotated[
        Optional[str], Field(None, description='All attribute name')
    ]
    mailAttributeName: Annotated[str, Field(description='Email attribute name')]
    usernameAttributeName: Annotated[
        Optional[str], Field(None, description='User Name attribute name')
    ]
    groupAttributeName: Annotated[
        Optional[str], Field(None, description='Group Name attribute name')
    ]
    groupAttributeValue: Annotated[
        Optional[str], Field(None, description='Group attribute value')
    ]
    groupMemberAttributeName: Annotated[
        Optional[str], Field(None, description='Group Member Name attribute name')
    ]
    authRolesMapping: Annotated[
        Optional[str],
        Field(
            None,
            description='Json string of roles mapping between LDAP roles and Ranger roles',
        ),
    ]
    authReassignRoles: Annotated[
        Optional[List[str]],
        Field(None, description='Roles should be reassign every time user login'),
    ]
    truststoreFormat: Annotated[
        Optional[str], Field(None, description='Truststore format e.g. PKCS12, JKS.')
    ]
    truststoreConfigType: Annotated[
        Optional[TruststoreConfigType],
        Field(
            None,
            description='Truststore Type e.g. TrustAll, HostName, JVMDefault, CustomTrustStore.',
        ),
    ]
    trustStoreConfig: Annotated[
        Optional[truststoreConfig.TruststoreConfig],
        Field(None, description='Truststore Configuration'),
    ]
