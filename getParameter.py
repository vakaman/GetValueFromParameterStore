import sys
from providers.ProviderFactory import ProviderFactory


def get_parameter(provider_name, parameter):

    provider = ProviderFactory.create(provider_name)

    return provider.get_parameter(parameter)

if __name__ == "__main__":
    provider = sys.argv[1]
    parameter = sys.argv[2]

    print(get_parameter(provider, parameter))
