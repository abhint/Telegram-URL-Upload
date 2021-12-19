#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


from .time import time_data
import time
from pyrogram.types import Message
from hurry.filesize import size, alternative
from pyrogram.errors import FloodWait, BadRequest, MessageNotModified

error = (FloodWait, MessageNotModified, BadRequest)


async def progress(current, total, message: Message, start_time):
    time_now = time.time()
    time_diff = time_now - start_time
    percent = round(current * 100 // total)
    progress_ = "{0} {1}%".format(
        progress_bar(percent),
        f"{current * 100 / total:.1f}"
    )
    time_ = "Time: {0}".format(
        time_data(start_time)
    )

    speed_ = "Speed: {0}/s".format(
        human_readable_size(current / time_diff)
    )
    download_ = "{0} of {1}".format(
        human_readable_size(current),
        human_readable_size(total)
    )
    try:
        await message.edit(
            text=f"{progress_}\n\n{download_}\n\n{speed_}\t{time_}"
        )

    except error as e:
        print(f'DISPLAY ERROR: {e}')
        pass


def progress_bar(percent):
    done_block = '█'
    empty_block = '░'
    return f"{done_block * int(percent / 5)}{empty_block * int(20 - int(percent / 5))}"


def human_readable_size(_size):
    return size(_size, system=alternative)
    # for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
    #     if size < 1000.0:
    #         break
    #     size /= 1000.0
    # return f"{size:.{decimal_places}f} {unit}"
