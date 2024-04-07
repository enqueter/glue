"""
Module select.py
"""
import src.crawler.interface
import src.database.interface

import src.elements.glue_paramaters as gpr


class Select:
    """
    Select and execute a service
    """

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def exc(parameters: gpr.GlueParameters):
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
