"""
Module select.py
"""
import src.crawler.interface
import src.database.interface

import src.elements.gp as gp


class Select:
    """
    Select and execute a service
    """

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def exc(parameters: gp.GP):
        """

        :param parameters:
        :return:
        """

        # Service

        match parameters.service:
            case 'crawler':
                src.crawler.interface.Interface(parameters=parameters).exc()
            case 'database':
                src.database.interface.Interface(parameters=parameters).exc()
            case _:
                raise f"{parameters.service} is not a service option"
