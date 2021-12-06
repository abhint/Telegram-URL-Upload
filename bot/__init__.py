import logging
from logging.handlers import RotatingFileHandler
from .env import get_env

API_ID = get_env('API_ID')
API_HASH = get_env('API_HASH')
BOT_TOKEN = get_env('BOT_TOKEN')
REGEX = "^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
LOGGER_FILE_NAME = "linktofile.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOGGER_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ])
logging.getLogger('pyrogram').setLevel(logging.WARNING)


def logger(log: str) -> logging.Logger:
    return logging.getLogger(log)


# Error handling
class ErrorLinkToFile(Exception):
    pass


# Download Location

DOWNLOAD_LOCATION = "./download/{}/{}/{}"
