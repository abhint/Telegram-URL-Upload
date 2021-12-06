from pyrogram.types import Message
from youtube_dl import YoutubeDL
from youtube_dl.utils import YoutubeDLError


async def link_check(url: str, message: Message) -> bool:

    try:
        with YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
            return True
    except YoutubeDLError as err:
        return False

# print(loop.run_until_complete(link_check(url, Message)))
