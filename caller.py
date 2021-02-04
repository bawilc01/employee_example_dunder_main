# caller file

import configparser
import logging
import sys


def main():
    config = configparser.ConfigParser()
    config.read(f'./config.ini')

    # logging setup

    caller_log_name = f'Class Practice Log'

    # logging setup
    logger = logging.getLogger()
    logger.name = caller_log_name
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # stream_handler = logging.StreamHandler()  # will logger.info all levels to the console stream
    # logger.addHandler(stream_handler)

    logger.info('------------------------------- process with caller started-------------------------------')

    try:
        import class_practice
        class_practice.main(logger)
    except Exception as e:
        logger.error(e)
        raise e

    try:
        import new_file
        new_file.main(logger)
    except Exception as e:
        logger.error(e)
        raise e



    logger.info('------------------------------- process with caller complete -------------------------------')


if __name__ == '__main__':
    main()
