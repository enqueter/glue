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

        self.__algorithm = src.database.algorithm.Algorithm()

    def exc(self) -> bool:
        """
        Executes database actions ...

        :return: bool
        """

        match self.__parameters['action']:
            case 'delete':
                return self.__algorithm.delete_database(name=parameters['database_name'])
            case _:
                raise f'{parameters['action']} is not a database action option'
