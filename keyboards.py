from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Mode info")],
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
        [KeyboardButton(text="Bounty")],
        [KeyboardButton(text="Back")]
    ],
    resize_keyboard=True
)

knockout_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Out in the Open", callback_data="map_out_in_the_open")],
        [InlineKeyboardButton(text="Belle's Rock", callback_data="map_Belle's Rock")],
        [InlineKeyboardButton(text="Goldarm Gulch", callback_data="map_Goldarm Gulch")],
        [InlineKeyboardButton(text="Flowing Springs", callback_data="map_Flowing Springs")],
        [InlineKeyboardButton(text="New Horizons", callback_data="map_New Horizons")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

brawl_ball_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Center Stage", callback_data="map_Center Stage")],
        [InlineKeyboardButton(text="Pinball Dreams", callback_data="map_Pinball Dreams")],
        [InlineKeyboardButton(text="Sneaky Fields", callback_data="map_Sneaky Fields")],
        [InlineKeyboardButton(text="Triple Dribble", callback_data="map_Triple Dribble")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

heist_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Bridge Too Far", callback_data="map_Bridge Too Far")],
        [InlineKeyboardButton(text="Hot Potato", callback_data="map_Hot Potato")],
        [InlineKeyboardButton(text="Kaboom Canyon", callback_data="map_Kaboom Canyon")],
        [InlineKeyboardButton(text="Safe Zone", callback_data="map_Safe Zone")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

gem_grab_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Gem Fort", callback_data="map_Gem Fort")],
        [InlineKeyboardButton(text="Hard Rock Mine", callback_data="map_Hard Rock Mine")],
        [InlineKeyboardButton(text="Undermine", callback_data="map_Undermine")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

hot_zone_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Dueling Beetles", callback_data="map_Dueling Beetles")],
        [InlineKeyboardButton(text="Open Business", callback_data="map_Open Business")],
        [InlineKeyboardButton(text="Parallel Plays", callback_data="map_Parallel Plays")],
        [InlineKeyboardButton(text="Ring of Fire", callback_data="map_Ring of Fire")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

bounty_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Layer Cake", callback_data="map_Layer Cake")],
        [InlineKeyboardButton(text="Dry Season", callback_data="map_Dry Season")],
        [InlineKeyboardButton(text="Hideout", callback_data="map_Hideout")],
        [InlineKeyboardButton(text="Canal Grande", callback_data="map_Canal Grande")],
        [InlineKeyboardButton(text="Shooting Star", callback_data="map_Shooting Star")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

back_to_menu_characters = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="back_to_main_options")]
    ]
)
