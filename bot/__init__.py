import logging
from .env import get_env
from logging.handlers import RotatingFileHandler

API_ID = get_env('API_ID')
API_HASH = get_env('API_HASH')
BOT_TOKEN = get_env('BOT_TOKEN')
# REGEX = "^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
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

# Thumb
THUMB = ""

# Messages


ERROR = '\nContact **[Abhijith N T](tg://user?id=429320566)** or create a [new issue](' \
        'https://github.com/abhint/Telegram-URL-Upload/issues/new) with GitHub.'
URL_NOT_VALID = 'URL: {}\nThe link is not valid or something is wrong with the bot.'
START_MESSAGE = "Hello __[{0}](tg://user?id={1}) {2}__,\n__I can upload files remotely to Telegram__\n" \
                "**/help - help command for more info**"

# -_-

# BANNER = """\033[1;32m
# ########   #######  ########    ####  ######      #######  ##    ## ##       #### ######## 
# ##     ## ##     ##    ##        ##  ##    ##    ##     ## ###   ## ##        ##  ##       
# ##     ## ##     ##    ##        ##  ##          ##     ## ####  ## ##        ##  ##       
# ########  ##     ##    ##        ##   ######     ##     ## ## ## ## ##        ##  ######   
# ##     ## ##     ##    ##        ##        ##    ##     ## ##  #### ##        ##  ##       
# ##     ## ##     ##    ##        ##  ##    ##    ##     ## ##   ### ##        ##  ##       
# ########   #######     ##       ####  ######      #######  ##    ## ######## #### ######## 
# """
