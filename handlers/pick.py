import json
from pathlib import Path

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove

from keyboards import (
    main_menu,
    modes_menu,
    knockout_maps,
    brawl_ball_maps,
    heist_maps,
    gem_grab_maps,
    hot_zone_maps,
    bounty_maps
)

router = Router()

BASE_DIR = Path(__file__).resolve().parent.parent
MAPS_FILE = BASE_DIR / "data" / "maps.json"

CHARACTERS_FILE = BASE_DIR / "data" / "characters.json"

with open(MAPS_FILE, "r", encoding="utf-8") as f:
    maps_data = json.load(f)

with open(CHARACTERS_FILE, "r", encoding="utf-8") as f:
    characters_data = json.load(f)


@router.message(F.text == "Mode info")
async def mode_info(message: Message):
    await message.answer(
        "Choose a mode:",
        reply_markup=modes_menu
    )

@router.message(F.text == "Back")
async def back_main(message: Message):
    await message.answer(
        "Main menu:",
        reply_markup=main_menu
    )


@router.callback_query(F.data == "back_to_modes")
async def back_modes(callback: CallbackQuery):
    await callback.message.answer(
        "Choose a mode:",
        reply_markup=modes_menu
    )
    await callback.answer()

@router.message(F.text == "Knockout")
async def knockout(message: Message):

    info = (
        "<b>Mode: Knockout ⚔️</b>\n\n"
        "<i>Description</i>: A 3v3 team mode where you have to eliminate your opponents in order to win a round. 🏆\n\n"
        "<b>Rules</b>:\n\n"
        "- Once you die, you cannot respawn till <i>next round</i>. ⏩️\n\n"
        "- Mode has <i>2 to 3 rounds</i>(first team to win 2 rounds wins). 🥇\n\n"
        "- Each round has a <i>time limit</i>, and maps gradually shrinks because of poison gas. ☠️\n\n"
        "- Tie is possible if <i>both team members die at the same time. 👾</i>\n\n"
        "<b>Choose a map to see the layout and strategies: </b>"
    )

    video = FSInputFile(Path("media") / "Knockout_map.mp4")

    await message.answer_video(
        video=video,
        caption=info,
        parse_mode="HTML",
        reply_markup=knockout_maps
    )


@router.message(F.text == "Brawl Ball")
async def brawl_ball(message: Message):

    info = (
        "<b>Mode: Brawl Ball ⚽</b>\n\n"
        "<i>Description</i>: A 3v3 team mode where teams compete to score goals and defeat their opponents. The first team to score 2 goals wins the match. 🏆\n\n"
        "<b>Rules</b>:\n\n"
        "- Players can <i>carry, pass, and shoot</i> the ball to score goals. ⚽\n\n"
        "- Defeating an enemy causes them to <i>drop the ball</i> immediately. 💥\n\n"
        "- The match ends when a team scores <i>2 goals</i> or when the timer runs out. ⏱️\n\n"
        "- If the score is tied at the end of regulation time, <i>Overtime</i> begins. 🔥\n\n"
        "<b>Choose a map to see the layout and strategies: </b>"
    )

    video = FSInputFile(Path("media") / "BrawlBall_map.mp4")

    await message.answer_video(
        video=video,
        caption=info,
        parse_mode="HTML",
        reply_markup=brawl_ball_maps
    )


@router.message(F.text == "Heist")
async def heist(message: Message):

    info = (
        "<b>Mode: Heist 💰</b>\n\n"
        "<i>Description</i>: A 3v3 team mode where teams must protect their own Safe while trying to destroy the enemy Safe. 🏆\n\n"
        "<b>Rules</b>:\n\n"
        "- Each team has a Safe that must be defended 🔒\n\n"
        "- First Safe destroyed loses 💥\n\n"
        "<b>Choose a map to see the layout and strategies: </b>"
    )

    video = FSInputFile(Path("media") / "Heist_map.mp4")

    await message.answer_video(
        video=video,
        caption=info,
        parse_mode="HTML",
        reply_markup=heist_maps
    )


@router.message(F.text == "Gem Grab")
async def gem_grab(message: Message):

    info = (
        "<b>Mode: Gem Grab 💎</b>\n\n"
        "<i>Description</i>: A 3v3 team mode where teams battle to collect Gems from the center Gem Mine. 🏆\n\n"
        "<b>Rules</b>:\n\n"
        "- Collect Gems from center 💎\n\n"
        "- Hold 10 Gems to start countdown ⏳\n\n"
        "<b>Choose a map to see the layout and strategies: </b>"
    )

    video = FSInputFile(Path("media") / "GemGrab_map.mp4")

    await message.answer_video(
        video=video,
        caption=info,
        parse_mode="HTML",
        reply_markup=gem_grab_maps
    )


@router.message(F.text == "Hot Zone")
async def hot_zone(message: Message):

    info = (
        "<b>Mode: Hot Zone 🔥</b>\n\n"
        "<i>Description</i>: Control zones to earn percentage and win. 🏆\n\n"
        "<b>Rules</b>:\n\n"
        "- Stand in zone to capture 🔥\n\n"
        "- First to 100% wins 🥇\n\n"
        "<b>Choose a map to see the layout and strategies: </b>"
    )

    video = FSInputFile(Path("media") / "HotZone_map.mp4")

    await message.answer_video(
        video=video,
        caption=info,
        parse_mode="HTML",
        reply_markup=hot_zone_maps
    )


@router.message(F.text == "Bounty")
async def bounty(message: Message):

    info = (
        "<b>Mode: Bounty ⭐</b>\n\n"
        "<i>Description</i>: Earn stars by eliminating enemies. 🏆\n\n"
        "<b>Rules</b>:\n\n"
        "- More kills = more stars ⭐\n\n"
        "<b>Choose a map to see the layout and strategies: </b>"
    )

    video = FSInputFile(Path("media") / "Bounty_map.mp4")

    await message.answer_video(
        video=video,
        caption=info,
        parse_mode="HTML",
        reply_markup=bounty_maps
    )


@router.callback_query(F.data)
async def show_map(callback: CallbackQuery):

    map_name = callback.data

    for mode in maps_data.values():
        if map_name in mode:
            data = mode[map_name]

            text = (
                f"📍 <b>{map_name}</b>\n\n"
                f"🔥 Best Picks: {', '.join(data['best_picks'])}\n"
                f"⭐ Alternative Picks: {', '.join(data['alternative_picks'])}\n"
                f"🛡 Counter Picks: {', '.join(data['counter_picks'])}"
            )

            await callback.message.edit_caption(
                caption=text,
                parse_mode="HTML"
            )

            await callback.answer()
            return

    await callback.answer("Map not found", show_alert=True)


@router.message(F.text == "Character info")
async def character_info(message: Message):
    await message.answer(
        "Please enter the correct character name to get information about it(Ex. Shelly, Colt, etc):",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text)
async def show_character_info(message: Message):
    user_name = message.text.strip()

    character_name = None

    for name in characters_data:
        if name.lower() == user_name.lower():
            character_name = name
            break

    if character_name is None:
         await message.answer(
        "Character not found. Please check the name spelling and try again.",
        parse_mode="HTML"
         )
         return
    
    data = characters_data[character_name]


    text = (
            f" <b>{character_name}</b>\n\n"
            f" Class: {data['class']}\n"
            f" Rarity: {data['rarity']}\n"
            f" MAX Damage: {data['damage']}\n"
            f" MAX Health: {data['health']}\n"
            f" MAX reload speed: {data['reload']}\n"
            f" MAX range: {data['range']}\n\n"
            f" Super: {data['super']}\n"
            f" Gadget: {', '.join(data['gadgets'])}\n"
            f" Passives: {', '.join(data['passives'])}\n"

        )
        
    await message.answer(
            text=text,
            parse_mode="HTML"
        )
    return
    
   