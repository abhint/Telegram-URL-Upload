import magic
from ..linktofile import TG
from pyrogram.types import Message
from pyrogram.errors import RPCError


async def file_send(filename: str, client: TG, updates: Message):
    file_mime = magic.Magic(mime=True).from_file(filename)
    try:
        if file_mime.startswith('video'):
            return await client.send_video(
                chat_id=updates.chat.id,
                reply_to_message_id=updates.message_id,
                video=filename,
                caption="Hello"
            )
        elif file_mime.startswith('image'):
            return await client.send_photo(
                chat_id=updates.chat.id,
                reply_to_message_id=updates.message_id,
                photo=filename,
                caption="Hello"
            )
        elif file_mime.startswith('audio'):
            return await client.send_audio(
                chat_id=updates.chat.id,
                reply_to_message_id=updates.message_id,
                audio=filename,
                caption="Hello"
            )
        else:
            return await client.send_document(
                chat_id=updates.chat.id,
                reply_to_message_id=updates.message_id,
                document=filename,
                caption="Hello"
            )
    except RPCError as err:
        raise Exception(f'{err}')
