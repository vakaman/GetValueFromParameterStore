from .ParameterStoreProvider import ParameterStoreProvider
from .VaultProvider import VaultProvider


class ProviderFactory:

    @staticmethod
    def create(name):
        if name == "parameter-store":
            return ParameterStoreProvider()
        if name == "vault":
            return VaultProvider()

        raise ValueError("Invalid provider type")
