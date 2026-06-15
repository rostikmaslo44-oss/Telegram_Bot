from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Peak selection")],
        [KeyboardButton(text="Counter peak")],
        [KeyboardButton(text="Mode info")],
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

knockout_maps = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text="Goldarm Gulch", callback_data="goldarm_gulch")],
        [InlineKeyboardButton(text="Deep End", callback_data="deep_end")],
        [InlineKeyboardButton(text="Belle's Rock", callback_data="belles_rock")],
        [InlineKeyboardButton(text="More", callback_data="back_to_modes")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)