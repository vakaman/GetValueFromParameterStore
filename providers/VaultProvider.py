import os
from .ProviderInterface import ProviderInterface
from hvac import Client as VaultClient


class VaultProvider(ProviderInterface):
    def __init__(self):
        self.client = VaultClient(
            url=os.environ.get('VAULT_URL'),
            token=os.environ.get('VAULT_TOKEN')
        )

    def get_parameter(self, name):
        response = self.client.read(name)
        if response and 'data' in response:
            return response['data']
        return None
