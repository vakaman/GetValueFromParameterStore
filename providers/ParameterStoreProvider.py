import os
import boto3
from .ProviderInterface import ProviderInterface


class ParameterStoreProvider(ProviderInterface):

    def __init__(self):
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        aws_region = os.getenv('AWS_REGION', 'us-east-1')

        self.client = boto3.client(
            'ssm',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region
        )

    def get_parameter(self, name):

        response = self.client.get_parameter(Name=name, WithDecryption=True)

        if 'Parameter' in response and 'Value' in response['Parameter']:
            return response['Parameter']['Value']

        return None
