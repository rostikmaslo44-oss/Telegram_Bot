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


@router.message(lambda msg: msg.text == "Нокаут")
async def show_nokaut(message: Message):
    # Приклад карт і інформації про режим "Нокаут"
    info = (
        "Режим: Нокаут\n"
        "Опис: Інтенсивний режим з одиночними поєдинками до вибуття.\n\n"
        "Карти:\n"
        "1) Арена Штормів — відкритий простір з численними укриттями.\n"
        "2) Фортеця Нокута — вузькі коридори, підходить для тактичних штурмів.\n"
        "3) Панорама — високі точки для снайперів і відкриті ділянки.\n\n"
        "Правила:\n"
        "- Гравець вибуває після поразки.\n"
        "- Переможець отримує бонуси та рейтинг.\n\n"
        "Поради:\n"
        "- Використовуйте укриття і контролюйте високі точки.\n"
        "- Працюйте в парі для утримання позицій."
    )

    await message.answer(info)
