from youtube_dl import YoutubeDL
from youtube_dl.utils import YoutubeDLError


async def link_check(url: str) -> bool:
    """
    param url: the URL you want to validate
    :return: True if download content is available or False
    """

    try:
        with YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
            return True
    except YoutubeDLError as err:
        return False

# print(loop.run_until_complete(link_check(url, Message)))
