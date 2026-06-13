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

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start(message: Message) -> None:
    full_name = message.from_user.full_name if message.from_user else "there"
    await message.answer(f"Hello <b>{full_name}</b>")

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.copy_to(chat_id=message.chat.id)
    except Exception:
        await message.answer("Could not copy message")


async def main():
    if not TOKEN:
        logging.error("BOT_TOKEN is not set. Set BOT_TOKEN in your environment or .env file.")
        sys.exit(1)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
