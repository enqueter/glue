"""
Module algorithm.py
"""
import logging

import boto3
import botocore.client
import botocore.exceptions

import src.elements.glue_paramaters as gpr
import src.functions.secret


class Algorithm:
    """
    Class Algorithm

    In progress ...
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_crawler.html#
        https://docs.aws.amazon.com/glue/latest/dg/example_glue_CreateCrawler_section.html
        https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples
    """

    def __init__(self, parameters: gpr.GlueParameters):
        """

        :param parameters: A collection …
        """

        self.__parameters = parameters

        # Glue Client & Amazon Resource Name (ARN)
        self.__secret = src.functions.secret.Secret()
        session = boto3.session.Session()
        self.__glue_client: botocore.client.BaseClient = session.client(service_name='glue')

        account_id: str = self.__secret.exc(secret_id='AccountIdentifier')
        glue_service_role: str = self.__secret.exc(secret_id='GlueServiceRole')
        self.__glue_arn: str = f'arn:aws:iam::{account_id}:role/{glue_service_role}'

    def create(self):
        """

        :return:
        """

        try:
            self.__glue_client.create_crawler(
                Name=self.__parameters.crawler_name,
                Role=self.__glue_arn,
                DatabaseName=self.__parameters.database_name,
                Description=self.__parameters.crawler_description,
                Targets={'S3Targets': [
                    {
                        'Path': f's3://{self.__parameters.s3_bucket_name}'
                    },
                ]},
                TablePrefix=self.__parameters.table_prefix,
                Schedule=self.__parameters.schedule
            )
            logging.log(level=logging.INFO, msg='Creating crawler ...')
        except botocore.exceptions.ClientError as err:
            raise err

    def start(self):
        """

        :return:
        """

        try:
            self.__glue_client.start_crawler(Name=self.__parameters.crawler_name)
            logging.log(level=logging.INFO, msg='The glue crawler is now running ...')
        except self.__glue_client.exceptions.CrawlerRunningException:
            logging.log(level=logging.INFO, msg='The glue crawler is already running ...')
        except botocore.exceptions.ClientError as err:
            raise err

    def delete(self):
        """

        :return:
        """

        try:
            self.__glue_client.delete_crawler(Name=self.__parameters.crawler_name)
            logging.log(level=logging.INFO, msg='Deleting crawler ...')

        except self.__glue_client.exceptions.EntityNotFoundException:
            logging.log(level=logging.INFO, msg=f'A glue crawler named {self.__parameters.crawler_name} does not exist.')

        except self.__glue_client.exceptions.CrawlerRunningException:
            logging.log(level=logging.WARNING, msg='The glue crawler is running, no action taken ...')

        except botocore.exceptions.ClientError as err:
            raise err
