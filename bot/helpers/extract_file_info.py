from youtube_dl import YoutubeDL
from youtube_dl.utils import YoutubeDLError


async def link_check(url: str) -> bool:
    """
    param url: the URL you want to validate
    :return: True if download content is available or False
    """

    ydl_opts = {
        'no_warnings': True
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=False)
            return True
    except YoutubeDLError as err:
        return False
