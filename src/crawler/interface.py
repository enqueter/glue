"""
Module interface.py
"""
import logging

import src.crawler.algorithm


class Interface:
    """
    The interface to the crawler actions
    """

    def __init__(self) -> None:
        """
        The constructor
        """

        self.__algorithm = src.crawler.algorithm.Algorithm()

    def exc(self, parameters: dict):
        """

        :param parameters: The dictionary of parameters
        """

        match parameters['objective']:
            case 'delete':
                self.__algorithm.delete_crawler()
            case 'create':
                self.__algorithm.create_crawler()
            case 'start':
                self.__algorithm.start_crawler()
            case _:
                logging.log(level= logging.INFO,
                            msg=f'{parameters['objective']} is not a database action option')
                return False
