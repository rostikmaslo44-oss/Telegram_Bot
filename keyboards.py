from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Головне меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Mode info")],
        [KeyboardButton(text="Counter peak")],
        [KeyboardButton(text="Character info")]
    ],
    resize_keyboard=True
)

# Меню вибору режимів
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

# --- KNOCKOUT MAPS ---
knockout_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Out in the Open", callback_data="map:knockout:out_in_the_open")],
        [InlineKeyboardButton(text="Belle's Rock", callback_data="map:knockout:Belle's Rock")],
        [InlineKeyboardButton(text="Goldarm Gulch", callback_data="map:knockout:Goldarm Gulch")],
        [InlineKeyboardButton(text="Flowing Springs", callback_data="map:knockout:Flowing Springs")],
        [InlineKeyboardButton(text="New Horizons", callback_data="map:knockout:New Horizons")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

# --- BRAWL BALL MAPS ---
brawl_ball_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Center Stage", callback_data="map:brawl_ball:Center Stage")],
        [InlineKeyboardButton(text="Pinball Dreams", callback_data="map:brawl_ball:Pinball Dreams")],
        [InlineKeyboardButton(text="Sneaky Fields", callback_data="map:brawl_ball:Sneaky Fields")],
        [InlineKeyboardButton(text="Triple Dribble", callback_data="map:brawl_ball:Triple Dribble")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

# --- HEIST MAPS ---
heist_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Bridge Too Far", callback_data="map:heist:Bridge Too Far")],
        [InlineKeyboardButton(text="Hot Potato", callback_data="map:heist:Hot Potato")],
        [InlineKeyboardButton(text="Kaboom Canyon", callback_data="map:heist:Kaboom Canyon")],
        [InlineKeyboardButton(text="Safe Zone", callback_data="map:heist:Safe Zone")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

# --- GEM GRAB MAPS ---
gem_grab_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Gem Fort", callback_data="map:gem_grab:Gem Fort")],
        [InlineKeyboardButton(text="Hard Rock Mine", callback_data="map:gem_grab:Hard Rock Mine")],
        [InlineKeyboardButton(text="Undermine", callback_data="map:gem_grab:Undermine")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

# --- HOT ZONE MAPS ---
hot_zone_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Dueling Beetles", callback_data="map:hot_zone:Dueling Beetles")],
        [InlineKeyboardButton(text="Open Business", callback_data="map:hot_zone:Open Business")],
        [InlineKeyboardButton(text="Parallel Plays", callback_data="map:hot_zone:Parallel Plays")],
        [InlineKeyboardButton(text="Ring of Fire", callback_data="map:hot_zone:Ring of Fire")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

# --- BOUNTY MAPS ---
bounty_maps = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Layer Cake", callback_data="map:bounty:Layer Cake")],
        [InlineKeyboardButton(text="Dry Season", callback_data="map:bounty:Dry Season")],
        [InlineKeyboardButton(text="Hideout", callback_data="map:bounty:Hideout")],
        [InlineKeyboardButton(text="Canal Grande", callback_data="map:bounty:Canal Grande")],
        [InlineKeyboardButton(text="Shooting Star", callback_data="map:bounty:Shooting Star")],
        [InlineKeyboardButton(text="Back", callback_data="back_to_modes")]
    ]
)

back_to_menu_characters = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="back_to_main_options")]
    ]
)