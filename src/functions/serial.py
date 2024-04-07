"""
Module serial.py
"""
import yaml


class Serial:
    """
    Class Serial

    Description
    -----------
    Presently, this class reads-in local YAML data files; YAML is a data serialisation language.
    """

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def read(uri: str) -> dict:
        """

        :param uri: The file string of a local YAML file; path + file name + extension.
        :return:
        """

        with open(file=uri, mode='r', encoding='utf-8') as stream:
            try:
                return yaml.load(stream=stream, Loader=yaml.CLoader)
            except yaml.YAMLError as err:
                raise err from err
