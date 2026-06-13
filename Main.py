import os
import asyncio
import sys
import logging

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()


async def main():
    if not TOKEN:
        logging.error("BOT_TOKEN is not set. Set BOT_TOKEN in your environment or .env file.")
        sys.exit(1)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
