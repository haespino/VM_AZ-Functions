import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Azure Configuration
AZURE_SUBSCRIPTION_ID = os.environ.get('AZURE_SUBSCRIPTION_ID')
AZURE_TENANT_ID = os.environ.get('AZURE_TENANT_ID')
AZURE_CLIENT_ID = os.environ.get('AZURE_CLIENT_ID')
AZURE_CLIENT_SECRET = os.environ.get('AZURE_CLIENT_SECRET')

# CosmosDB Configuration
COSMOSDB_CONNECTION_STRING = os.environ.get('COSMOSDB_CONNECTION_STRING')
COSMOSDB_DATABASE_NAME = 'vm_management'
COSMOSDB_CONTAINER_VMS = 'vms'
COSMOSDB_CONTAINER_SSH_KEYS = 'ssh_keys'
COSMOSDB_CONTAINER_VM_STATUS = 'vm_status'

# Key Vault Configuration
KEY_VAULT_URL = os.environ.get('KEY_VAULT_URL')

# API Configuration
API_KEY = os.environ.get('API_KEY')

# VM Configuration
VM_SIZES = {
    'small': 'Standard_B1s',
    'medium': 'Standard_B2s',
    'large': 'Standard_B4ms'
}

VM_IMAGE = {
    'publisher': 'Canonical',
    'offer': '0001-com-ubuntu-server-focal',
    'sku': '20_04-lts-gen2',
    'version': 'latest'
}

# Default VM Configuration
DEFAULT_VM_SIZE = 'medium'
DEFAULT_REGION = 'eastus'
DEFAULT_ADMIN_USERNAME = 'azureuser'

# Network Security Group Rules
NSG_RULES = [
    {
        'name': 'SSH',
        'priority': 1001,
        'direction': 'Inbound',
        'access': 'Allow',
        'protocol': 'Tcp',
        'source_port_range': '*',
        'destination_port_range': '22',
        'source_address_prefix': '*',
        'destination_address_prefix': '*'
    },
    {
        'name': 'HTTP',
        'priority': 1002,
        'direction': 'Inbound',
        'access': 'Allow',
        'protocol': 'Tcp',
        'source_port_range': '*',
        'destination_port_range': '80',
        'source_address_prefix': '*',
        'destination_address_prefix': '*'
    },
    {
        'name': 'HTTPS',
        'priority': 1003,
        'direction': 'Inbound',
        'access': 'Allow',
        'protocol': 'Tcp',
        'source_port_range': '*',
        'destination_port_range': '443',
        'source_address_prefix': '*',
        'destination_address_prefix': '*'
    }
]

# Initialize Key Vault client
def get_keyvault_client():
    """Initialize and return Key Vault client"""
    credential = DefaultAzureCredential()
    return SecretClient(vault_url=KEY_VAULT_URL, credential=credential)

# Validation functions
def validate_config():
    """Validate that all required configuration is present"""
    required_vars = [
        'AZURE_SUBSCRIPTION_ID',
        'AZURE_TENANT_ID', 
        'AZURE_CLIENT_ID',
        'AZURE_CLIENT_SECRET',
        'COSMOSDB_CONNECTION_STRING',
        'KEY_VAULT_URL',
        'API_KEY'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.environ.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    return True