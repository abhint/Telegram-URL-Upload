from pyrogram import emoji
from pyrogram import filters
from pyrogram.types import Message
from bot.linktofile import TG
from bot import logger, START_MESSAGE
from bot.helpers import system_status

LOGGER = logger(__name__)


# Start command

@TG.on_message(filters.command("start") & filters.private)
async def start_message(_, messages: Message):
    LOGGER.info(f'{messages.from_user.first_name} - {messages.from_user.id}')
    await messages.reply(
        START_MESSAGE.format(messages.from_user.first_name, messages.from_user.id, emoji.GRINNING_FACE))
    # await messages.reply('Hello! '
    #                      f'[{messages.from_user.first_name}](tg://user?id={messages.from_user.id})')


# help command

@TG.on_message(filters.command(['help', 'h']))
async def help_message(_, messages: Message):
    LOGGER.info(f'{messages.from_user.first_name} - {messages.from_user.id}')
    await messages.reply(f"[Abhijith](tg://user?id=429320566)")


# Status
@TG.on_message(filters.command(["status", 's']))
async def status_message(_, messages: Message):
    LOGGER.info(f'{messages.from_user.first_name} - {messages.from_user.id}')
    usage = system_status()
    await messages.reply(usage)
