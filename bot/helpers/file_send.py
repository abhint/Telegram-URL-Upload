import magic
import os
from ..linktofile import TG
from pyrogram.types import Message
from pyrogram.errors import RPCError
import time
from .time import time_data
from bot import THUMB
from .tools import video_details


async def file_send(file_path: str, client: TG, updates: Message, message: Message):
    _now = time.time()
    file_mime = magic.Magic(mime=True).from_file(file_path)
    file_name = os.path.basename(file_path)
    document_thumb = THUMB if THUMB else None
    # file_name = file_path.split('/')[-1].split('.')[0]
    try:
        if file_mime.startswith('video'):
            width, height, duration, thumb = video_details(file_path)
            await updates.edit_text('Uploading...')
            await client.send_video(
                chat_id=updates.chat.id,
                video=file_path,
                caption=f"{file_name}",
                reply_to_message_id=message.message_id,
                duration=duration,
                thumb=thumb,
                width=width,
                height=height,
                # progress=progress,
                # progress_args=(updates,)
            )
            await updates.edit_text(f'Uploaded...100% in {time_data(time.time() - _now)}')
        elif file_mime.startswith('image'):
            await updates.edit_text('Uploading...')
            await client.send_photo(
                chat_id=updates.chat.id,
                photo=file_path,
                caption=f"{file_name}",
                reply_to_message_id=message.message_id,
                # progress=progress,
                # progress_args=(updates,)

            )
            await updates.edit_text(f'Uploaded...100% in {time_data(time.time() - _now)}')
        elif file_mime.startswith('audio'):
            await updates.edit_text('Uploading...')
            await client.send_audio(
                chat_id=updates.chat.id,
                audio=file_path,
                caption=f"{file_name}",
                reply_to_message_id=message.message_id,
                # progress=progress,
                # progress_args=(updates,)
            )
            await updates.edit_text(f'Uploaded...100% in {time_data(time.time() - _now)}')
        else:
            await updates.edit_text('Uploading...')
            await client.send_document(
                chat_id=updates.chat.id,
                document=file_path,
                caption=f"{file_name}",
                reply_to_message_id=message.message_id,
                thumb=document_thumb
                # progress=progress,
                # progress_args=(updates,),
            )
            await updates.edit_text(f'Uploaded...100% in {time_data(time.time() - _now)}')
    except RPCError as err:
        raise Exception(f'File Upload RPCError: {err}')
    # await updates.delete()
