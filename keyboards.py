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
        [KeyboardButton(text="Bounty")],
        [KeyboardButton(text="Back")]
    ],
    resize_keyboard=True
)



knockout_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Out in the Open", callback_data="Out in the Open")],
        [InlineKeyboardButton(text="Belle's Rock", callback_data="Belle's Rock")],
        [InlineKeyboardButton(text="Goldarm Gulch", callback_data="Goldarm Gulch")],
        [InlineKeyboardButton(text="Flowing Springs", callback_data="Flowing Springs")],
        [InlineKeyboardButton(text="New Horizons", callback_data="New Horizons")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)



brawl_ball_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Center Stage", callback_data="Center Stage")],
        [InlineKeyboardButton(text="Pinball Dreams", callback_data="Pinball Dreams")],
        [InlineKeyboardButton(text="Sneaky Fields", callback_data="Sneaky Fields")],
        [InlineKeyboardButton(text="Triple Dribble", callback_data="Triple Dribble")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)



heist_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Bridge Too Far", callback_data="Bridge Too Far")],
        [InlineKeyboardButton(text="Hot Potato", callback_data="Hot Potato")],
        [InlineKeyboardButton(text="Kaboom Canyon", callback_data="Kaboom Canyon")],
        [InlineKeyboardButton(text="Safe Zone", callback_data="Safe Zone")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)


gem_grab_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Gem Fort", callback_data="Gem Fort")],
        [InlineKeyboardButton(text="Hard Rock Mine", callback_data="Hard Rock Mine")],
        [InlineKeyboardButton(text="Undermine", callback_data="Undermine")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)


hot_zone_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Dueling Beetles", callback_data="Dueling Beetles")],
        [InlineKeyboardButton(text="Open Business", callback_data="Open Business")],
        [InlineKeyboardButton(text="Parallel Plays", callback_data="Parallel Plays")],
        [InlineKeyboardButton(text="Ring of Fire", callback_data="Ring of Fire")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)


bounty_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Layer Cake", callback_data="Layer Cake")],
        [InlineKeyboardButton(text="Dry Season", callback_data="Dry Season")],
        [InlineKeyboardButton(text="Hideout", callback_data="Hideout")],
        [InlineKeyboardButton(text="Canal Grande", callback_data="Canal Grande")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)