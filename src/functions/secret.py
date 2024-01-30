""" 
The secret ...
"""
import boto3
import botocore.exceptions

import json


class Secret:
    """
    Description
    -----------
    This class retrieves the ...


    References
    ----------

    * https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html

    """

    def __init__(self) -> None:
        """
        The constructor
        """

        self.__session = boto3.session.Session()
        self.__secrets_manager = self.__session.client(
            service_name='secretsmanager')

    def __get__value(self, secret_id: str) -> str:
        """
        The reader of a secret key's value.


        :param secret_id: The identification code of the secret

        Returns:
            _type_: str
        """

        try:
            secret_value: dict = self.__secrets_manager.get_secret_value(
                SecretId=secret_id)
        except botocore.exceptions.ClientError as err:
            raise err

        return secret_value['SecretString']

    def exc(self, secret_id: str) -> str:
        """
        Gets the value of a secret key.

        :param secret_id: The identification code of the secret

        Returns:
            _type_: str
        """

        expression = self.__get__value(secret_id=secret_id)
        dictionary: dict = json.loads(expression)

        return dictionary[secret_id]
