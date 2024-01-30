"""
Module interface.py
"""

import src.database.algorithm


class Interface:
    """
    The interface to database actions
    """

    def __init__(self) -> None:
        """
        The constructor
        """

        self.__algorithm = src.database.algorithm.Algorithm()

    def exc(self, parameters: dict) -> bool:
        """
        Executes database actions ...

        
        :param parameters: A dictionary of parameters

        :return: bool
        """

        match parameters['action']:
            case 'delete':
                return self.__algorithm.delete_database(name=parameters['database_name'])
            case _:
                raise f'{parameters['action']} is not a database action option'
