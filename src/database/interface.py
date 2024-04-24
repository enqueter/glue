"""
Module interface.py
"""

import src.database.algorithm

import src.elements.gp as gp


class Interface:
    """
     Database actions interface.
    """

    def __init__(self, parameters: gp.GP) -> None:
        """
        The constructor

        :param parameters: A dictionary of parameters
        """

        self.__parameters = parameters

        # Database actions instance
        self.__algorithm = src.database.algorithm.Algorithm(parameters=self.__parameters)

    def exc(self) -> None:
        """
        Executes database actions ...

        :return: bool
        """

        match self.__parameters.objective:
            case 'delete':
                self.__algorithm.delete()
            case _:
                raise f'{self.__parameters.objective} is not a database action objective'
