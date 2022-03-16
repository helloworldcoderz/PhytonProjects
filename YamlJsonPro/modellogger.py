import logging
import sys


def init_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )


def log_debug(message):
    logging.debug(message)


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)


def log_exception(message):
    logging.exception(message)