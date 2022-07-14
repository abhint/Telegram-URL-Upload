from pyrogram import Client
from bot import (API_ID, API_HASH, BOT_TOKEN, logger)


class TG(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        self.LOGGER = logger(__name__)
        super().__init__(
            name,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="bot/plugins"),
            sleep_threshold=60,
            parse_mode="markdown"
        )

    async def start(self):
        await super().start()
        self.LOGGER.info(f'Bot is Online!')
        # print(BANNER)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info(f'Bot is Offline!')
