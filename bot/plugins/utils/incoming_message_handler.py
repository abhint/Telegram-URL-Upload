import time

from pyrogram import filters
from pyrogram.types import Message
from bot import DOWNLOAD_LOCATION, ERROR, URL_NOT_VALID, logger
from bot.helpers import link_check, download_file, file_send, remove_file
from bot.linktofile import TG

LOGGER = logger(__name__)


@TG.on_message(filters.regex(pattern='.*http.*'))
async def incoming_urls(client: TG, message: Message) -> None:
    LOGGER.info(f'{message.from_user.id} - {message.text}')
    url = message.text
    if '|' in url:
        url, file_name = url.replace(' ', '').split('|')
        download_location = DOWNLOAD_LOCATION.format(message.from_user.id, int(time.time()), file_name)
    else:
        download_location = DOWNLOAD_LOCATION.format(message.from_user.id, int(time.time()), '%(title)s.%(ext)s')

    url_check = await link_check(url)
    if url_check is False:
        await message.reply(f'{URL_NOT_VALID}\n{ERROR}'.format(url),
                            disable_web_page_preview=True
                            )
        return
    _reply = await client.send_message(
        message.chat.id,
        f'**URL:** {url} is valid',
        reply_to_message_id=message.message_id,
        disable_web_page_preview=True
    )
    file_download_path = await download_file(url, download_location, _reply)

    if file_download_path is False:
        await message.reply(f'Sorry file path is not found\n{ERROR}')
        return
    try:
        await file_send(file_download_path, client, _reply, message)
    except Exception as err:
        print(f"'File uploading error: {err}")
        await client.send_message(
            message.chat.id,
            f'File uploading error\n{ERROR}',
            reply_to_message_id=message.message_id
        )

    await _reply.delete()
    try:
        remove_file(file_download_path)
    except Exception as e:
        print(e)
