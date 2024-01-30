""" 
The secret ...
"""
import boto3
import botocore.exceptions


class Secret:
    """

    Description
    -----------
    This class retrieves the ...

    References
    ----------

    * https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    * https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html#API_GetSecretValue_ResponseSyntax

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


        :param secret_id: The identification code of the secret
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

        return self.__get__value(secret_id=secret_id)
