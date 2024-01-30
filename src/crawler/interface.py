"""
Module interface.py
"""

import src.crawler.algorithm


class Interface:
    """
    The interface to the crawler actions
    """

    def __init__(self, parameters: dict) -> None:
        """
        The constructor

        :param parameters: The dictionary of parameters
        """

        self.__parameters: dict = parameters

        self.__algorithm = src.crawler.algorithm.Algorithm(parameters=self.__parameters)

    def exc(self, ):
        """

        :return:
        """

        match self.__parameters['action']:
            case 'delete':
                self.__algorithm.delete()
            case 'create':
                self.__algorithm.create()
            case 'start':
                self.__algorithm.start()
            case _:
                raise f'{self.__parameters['action']} is not a crawler action option'
