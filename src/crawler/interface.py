"""
Module interface.py
"""

import src.crawler.algorithm

import src.elements.glue_paramaters as gpr


class Interface:
    """
    Crawler actions interface.
    """

    def __init__(self, parameters: gpr.GlueParameters) -> None:
        """
        The constructor

        :param parameters: The dictionary of parameters
        """

        self.__parameters = parameters

        # Crawler actions instance
        self.__algorithm = src.crawler.algorithm.Algorithm(parameters=self.__parameters)

    def exc(self):
        """

        :return:
        """

        match self.__parameters.objective:
            case 'delete':
                self.__algorithm.delete()
            case 'create':
                self.__algorithm.create()
            case 'start':
                self.__algorithm.start()
            case _:
                raise f'{self.__parameters.objective} is not a crawler action objective'
