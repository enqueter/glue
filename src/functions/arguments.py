"""
Module arguments.py
"""
import os


class Arguments:

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def text(filename: str) -> str:
        """
        
        :param filename: The name, including extension, of the YAML file of parameters
        :return: 
        """

        uri = os.path.join(os.getcwd(), filename)

        try:
            os.path.isfile(path=uri)
            return uri
        except FileNotFoundError as err:
            raise err from err
        except OSError as err:
            raise err from err
