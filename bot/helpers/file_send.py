import magic
from ..linktofile import TG
from pyrogram.types import Message
from pyrogram.errors import RPCError
import time
from .display import progress
from .tools import video_details


async def file_send(file_path: str, client: TG, updates: Message, message: Message):
    _now = time.time()
    file_mime = magic.Magic(mime=True).from_file(file_path)
    file_name = file_path.split('/')[-1].split('.')[0]
    try:
        if file_mime.startswith('video'):
            width, height, duration, thumb = video_details(file_path)
            return await client.send_video(
                chat_id=updates.chat.id,
                video=file_path,
                caption=f"{file_name}",
                reply_to_message_id=message.message_id,
                progress=progress,
                duration=duration,
                thumb=thumb,
                width=width,
                height=height,
                progress_args=(updates,)
            )
        elif file_mime.startswith('image'):
            return await client.send_photo(
                chat_id=updates.chat.id,
                photo=file_path,
                caption=f"{file_name}",
                reply_to_message_id=message.message_id,
                progress=progress,
                progress_args=(updates,)

            )

        elif file_mime.startswith('audio'):
            return await client.send_audio(
                chat_id=updates.chat.id,
                audio=file_path,
                caption=f"{file_name}",
                progress=progress,
                reply_to_message_id=message.message_id,
                progress_args=(updates,)
            )
        else:
            return await client.send_document(
                chat_id=updates.chat.id,
                document=file_path,
                caption=f"{file_name}",
                progress=progress,
                reply_to_message_id=message.message_id,
                progress_args=(updates,),
            )
    except RPCError as err:
        raise Exception(f'{err}')
    # await updates.delete()
