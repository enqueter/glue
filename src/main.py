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
    logger.info(parameters)

    # Service
    match parameters['service']:
        case 'crawler':
            src.crawler.interface.Interface().exc(parameters=parameters)
        case 'database':
            src.database.interface.Interface().exc(parameters=parameters)
        case _:
            logger.info('%s is not a service option', parameters['service'])


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
    import src.functions.cache
    import src.functions.serial
    import src.crawler.interface
    import src.database.interface

    # The parameters
    uri = os.path.join(root, 'parameters.yaml')
    dictionary = src.functions.serial.Serial().get_dictionary(uri=uri)
    parameters: dict = dictionary['parameters']

    main()
