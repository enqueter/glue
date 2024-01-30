"""
The module main.py
"""
import logging
import os
import sys


def main():
    """
    The entry point
    """

    # Parameters
    logger = logging.getLogger(__name__)
    logger.info(msg=parameters)

    # Service
    match parameters['service']:
        case 'crawler':
            src.crawler.interface.Interface(parameters=parameters).exc()
        case 'database':
            src.database.interface.Interface(parameters=parameters).exc()
        case _:
            raise f"{parameters['service']} is not a service option"

    # Delete __pycache__
    src.functions.cache.Cache().delete()


if __name__ == '__main__':
    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Classes
    import src.crawler.interface
    import src.database.interface
    import src.functions.cache
    import src.functions.serial

    # The parameters
    uri = os.path.join(root, 'parameters.yaml')
    dictionary = src.functions.serial.Serial().get_dictionary(uri=uri)
    parameters: dict = dictionary['parameters']

    main()
