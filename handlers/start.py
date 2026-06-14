from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import main_menu

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Hello ! Enter your choise:",
        reply_markup=main_menu
    )