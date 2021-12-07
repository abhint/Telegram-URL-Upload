from pyrogram import filters
from pyrogram.types import Message
from bot.linktofile import TG
from bot import logger

LOGGER = logger(__name__)


# Start command

@TG.on_message(filters.command("start") & filters.private)
async def start_message(_, messages: Message):
    LOGGER.info(f'{messages.from_user.first_name} - {messages.from_user.id}')
    await messages.reply('Hello! '
                         f'[{messages.from_user.first_name}](tg://user?id={messages.from_user.id})')


# help command

@TG.on_message(filters.command(['help', 'h']))
async def help_message(_, message: Message):
    await message.reply(f"[Abhijith](tg://user?id=429320566)")
