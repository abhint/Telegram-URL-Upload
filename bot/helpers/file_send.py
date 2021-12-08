import magic
from ..linktofile import TG
from pyrogram.types import Message
from pyrogram.errors import RPCError
import time
from .display import progress


async def file_send(filename: str, client: TG, updates: Message, message: Message):
    _now = time.time()
    file_mime = magic.Magic(mime=True).from_file(filename)
    try:
        if file_mime.startswith('video'):
            return await client.send_video(
                chat_id=updates.chat.id,
                video=filename,
                caption=f"MIME: {file_mime}\nvideo",
                reply_to_message_id=message.message_id,
                progress=progress,
                progress_args=(
                    updates,
                    _now
                )
            )
        elif file_mime.startswith('image'):
            return await client.send_photo(
                chat_id=updates.chat.id,
                photo=filename,
                caption=f"MIME: {file_mime}\nimage",
                reply_to_message_id=message.message_id,
                progress=progress,
                progress_args=(
                    updates,
                    _now
                )
            )

        elif file_mime.startswith('audio'):
            return await client.send_audio(
                chat_id=updates.chat.id,
                audio=filename,
                caption=f"MIME: {file_mime}\naudio",
                progress=progress,
                reply_to_message_id=message.message_id,
                progress_args=(
                    updates,
                    _now
                )
            )
        else:
            return await client.send_document(
                chat_id=updates.chat.id,
                document=filename,
                caption=f"MIME: {file_mime}\ndocument",
                progress=progress,
                reply_to_message_id=message.message_id,
                progress_args=(
                    updates,
                    _now
                ),
            )
    except RPCError as err:
        raise Exception(f'{err}')
    # await updates.delete()
