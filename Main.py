import os
import asyncio
import sys
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.start import router as start_router
from handlers.pick import router as pick_router

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(pick_router)


async def main():
    if not TOKEN:
        logging.error("BOT_TOKEN is not set. Set BOT_TOKEN in your environment or .env file.")
        sys.exit(1)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

    print("Bot stopped")
    