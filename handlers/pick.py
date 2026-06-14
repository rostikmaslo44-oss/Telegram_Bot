from aiogram import Router
from aiogram.types import Message

from keyboards import modes_menu

router = Router()

@router.message(lambda msg: msg.text == "Peak selection")
async def choose_mode(message: Message):
    await message.answer(
        "Choose a mode: ",
        reply_markup=modes_menu
    )