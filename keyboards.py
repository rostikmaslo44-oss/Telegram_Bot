from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Peak selection")],
        [KeyboardButton(text="Counter peak")],
        [KeyboardButton(text="Character info")]
    ],
    resize_keyboard=True
)

modes_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Knockout")],
        [KeyboardButton(text="Brawl Ball")],
        [KeyboardButton(text="Hot Zone")],
        [KeyboardButton(text="Gem Grab")],
        [KeyboardButton(text="Heist")],
        [KeyboardButton(text="Back")]
    ],
    resize_keyboard=True
)