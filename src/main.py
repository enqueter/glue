"""
The module main.py
"""
import logging
import argparse
import os
import sys


def main():
    """
    The entry point
    """

    logger = logging.getLogger(__name__)

    # Setting up
    dictionary = src.functions.serial.Serial().read(uri=args.elements)
    node: dict = dictionary['parameters']
    logger.info(node)

    parameters = src.elements.glue_paramaters.GlueParameters(**node)
    src.select.Select().exc(parameters=parameters)

    # Delete __pycache__
    src.functions.cache.Cache().delete()


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # logging
    logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Modules
    import src.functions.cache
    import src.functions.serial
    import src.functions.arguments
    import src.elements.glue_paramaters
    import src.select

    # The parameters
    arguments = src.functions.arguments.Arguments()
    parser = argparse.ArgumentParser()
    parser.add_argument('elements',
                        type=arguments.text,
                        help='The name of the YAML of parameters is required.')
    args = parser.parse_args()

    main()
