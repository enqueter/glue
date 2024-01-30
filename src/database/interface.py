"""
Module interface.py
"""
import logging

import src.database.algorithm


class Interface:
    """_summary_
    """

    def __init__(self) -> None:
        """
        The constructor
        """

        self.__algorithm = src.database.algorithm.Algorithm()

    def exc(self, parameters: dict) -> bool:
        """
        Executes database actions ...

        Args:
        :param parameters: A dictionary of parameters

        Returns:
            _type_: bool
        """

        match parameters['objective']:
            case 'delete':
                return self.__algorithm.delete_database(name=parameters['database_name'])
            case _:
                logging.log(level= logging.INFO,
                            msg=f'{parameters['objective']} is not a database action option')
                return False
