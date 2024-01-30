"""
Module algorithm.py
"""

import logging

import boto3

import botocore.client
import botocore.exceptions


class Algorithm:
    """
    Class Algorithm

    In progress ...
        https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples
    """

    def __init__(self, parameters: dict):
        """
        The constructor

        :param parameters: A dictionary of parameters
        """

        self.__parameters = parameters

        # Glue Client
        self.__glue_client = boto3.client(service_name='glue')

    def delete_database(self) -> bool:
        """
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_database.html

        :return:
        """

        try:
            self.__glue_client.delete_database(Name=self.__parameters['database_name'])
            logging.log(level=logging.INFO, msg=f'Database {self.__parameters['database_name']} has been deleted.')
            return True
        except self.__glue_client.exceptions.EntityNotFoundException:
            logging.log(level=logging.INFO, msg=f'Database {self.__parameters['database_name']} does not exist.')
            return True
        except self.__glue_client.exceptions.OperationTimeoutException:
            logging.log(level=logging.INFO, msg='Time out.')
            return False
        except botocore.exceptions.ClientError as err:
            raise err
