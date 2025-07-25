# generated by datamodel-codegen:
#   filename:  security/secrets/secretsManagerProvider.json
#   timestamp: 2025-07-11T17:47:24+00:00

from __future__ import annotations

from enum import Enum


class SecretsManagerProvider(Enum):
    db = 'db'
    managed_aws = 'managed-aws'
    aws = 'aws'
    managed_aws_ssm = 'managed-aws-ssm'
    aws_ssm = 'aws-ssm'
    managed_azure_kv = 'managed-azure-kv'
    azure_kv = 'azure-kv'
    in_memory = 'in-memory'
    gcp = 'gcp'
