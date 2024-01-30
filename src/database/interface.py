"""
Module interface.py
"""

import src.database.algorithm


class Interface:
    """
    The interface to database actions
    """

    def __init__(self, parameters: dict) -> None:
        """
        The constructor

        :param parameters: A dictionary of parameters
        """

        self.__parameters = parameters

        # Database actions instance
        self.__algorithm = src.database.algorithm.Algorithm(parameters=self.__parameters)

    def exc(self) -> bool:
        """
        Executes database actions ...

        :return: bool
        """

        match self.__parameters['action']:
            case 'delete':
                self.__algorithm.delete()
            case _:
                raise f'{self.__parameters['action']} is not a database action option'
