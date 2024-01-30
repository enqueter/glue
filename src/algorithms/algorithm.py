"""
Module database.py
"""

import logging

import boto3

import botocore.client
import botocore.exceptions


class Database:
    """
    Class Database

    In progress ...
        https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples
    """

    def __init__(self):
        """
        The constructor
        """

        # Glue Client
        self.__glue_client = boto3.client(service_name='glue')

    def delete_database(self, name: str) -> bool:
        """
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_database.html

        :param name:
        :return:
        """

        try:
            self.__glue_client.delete_database(Name=name)
            logging.log(level=logging.INFO, msg=f'Database {name} has been deleted.')
            return True
        except self.__glue_client.exceptions.EntityNotFoundException:
            logging.log(level=logging.INFO, msg=f'Database {name} does not exist.')
            return True
        except self.__glue_client.exceptions.OperationTimeoutException:
            logging.log(level=logging.INFO, msg='Time out.')
            return False
        except botocore.exceptions.ClientError as err:
            raise err
