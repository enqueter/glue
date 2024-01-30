"""
Module crawler.py
"""
import logging

import boto3
import botocore.client
import botocore.exceptions

import src.functions.secret
import src.functions.serial


class Crawler:
    """
    Class Crawler

    In progress ...
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_crawler.html#
        https://docs.aws.amazon.com/glue/latest/dg/example_glue_CreateCrawler_section.html
        https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples
    """

    def __init__(self, parameters: dict):
        """

        :param parameters: A collection ...
        """

        self.__parameters = parameters

        # Glue Client & Amazon Resource Name (ARN)
        self.__secret = src.functions.secret.Secret()
        self.__glue_client: botocore.client.BaseClient = boto3.client(service_name='glue')
        self.__glue_arn: str = f'arn:aws:iam::{self.__secret.exc(secret_id='AccountIdentifier')}:role/{self.__secret.exc(secret_id='GlueServiceRole')}'

    def create_crawler(self):
        """

        :return:
        """

        try:
            return self.__glue_client.create_crawler(
                Name=self.__parameters['crawler_name'],
                Role=self.__glue_arn,
                DatabaseName=self.__parameters['database_name'],
                Description=self.__parameters['crawler_description'],
                Targets={'S3Targets': [
                    {
                        'Path': f's3://{self.__parameters['s3_bucket_name']}'
                    },
                ]},
                TablePrefix=self.__parameters['table_prefix'],
                Schedule=self.__parameters['schedule']
            )
        except botocore.exceptions.ClientError as err:
            raise err

    def start_crawler(self):
        """

        :return:
        """

        try:
            self.__glue_client.start_crawler(Name=self.__parameters['crawler_name'])
            logging.log(level=logging.INFO, msg='The glue crawler is now running ...')
        except self.__glue_client.exceptions.CrawlerRunningException:
            logging.log(level=logging.INFO, msg='The glue crawler is already running ...')
        except botocore.exceptions.ClientError as err:
            raise err

    def delete_crawler(self, name: str):
        """

        :param name:
        :return:
        """

        try:
            self.__glue_client.delete_crawler(Name=name)
            return True
        except self.__glue_client.exceptions.EntityNotFoundException:
            logging.log(level=logging.INFO, msg=f'A glue crawler named {name} does not exist.')
            return True
        except self.__glue_client.exceptions.CrawlerRunningException:
            logging.log(level=logging.INFO, msg='The glue crawler is running ...')
            return False
        except botocore.exceptions.ClientError as err:
            raise err
