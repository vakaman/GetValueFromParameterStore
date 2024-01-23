from abc import ABC, abstractmethod


class ProviderInterface(ABC):
    @abstractmethod
    def get_parameter(self, name):
        pass
