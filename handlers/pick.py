import json
from pathlib import Path

from rapidfuzz import process, fuzz
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards import (
    main_menu,
    modes_menu,
    knockout_maps,
    brawl_ball_maps,
    heist_maps,
    gem_grab_maps,
    hot_zone_maps,
    bounty_maps,
    back_to_menu_characters
)

router = Router()

BASE_DIR = Path(__file__).resolve().parent.parent
MAPS_FILE = BASE_DIR / "data" / "maps.json"
CHARACTERS_FILE = BASE_DIR / "data" / "characters.json"

with open(MAPS_FILE, "r", encoding="utf-8") as f:
    maps_data = json.load(f)

with open(CHARACTERS_FILE, "r", encoding="utf-8") as f:
    characters_data = json.load(f)


class CharacterStates(StatesGroup):
    waiting_for_name = State()


@router.message(F.text == "Character info")
async def start_character_search(message: Message, state: FSMContext):
    await message.answer(
        "Enter brawler's name:",
        reply_markup=back_to_menu_characters 
    )
    await state.set_state(CharacterStates.waiting_for_name) 


@router.message(F.text == "Mode info")
async def mode_info(message: Message):
    await message.answer(
        "Choose a mode:",
        reply_markup=modes_menu
    )


@router.message(F.text == "Back")
async def back_main(message: Message, state: FSMContext):
    await state.clear() 
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


@router.callback_query(F.data == "back_to_main_options")
async def back_main_callback(callback: CallbackQuery, state: FSMContext):
    await state.clear() 
    await callback.message.answer(
        "Main menu:",
        reply_markup=main_menu
    )
    await callback.answer()


@router.message(F.text == "Knockout")
async def knockout(message: Message):
    info = (
        "<b>Mode: Knockout ⚔️</b>\n\n"
        "<i>Description</i>: A 3v3 team mode where you have to eliminate your opponents in order to win a round. 🏆\n\n"
        "<b>Rules</b>:\n\n"
        "- Once you die, you cannot respawn till <i>next round</i>. ⏩\n"
        "- Mode has <i>2 to 3 rounds</i>. 🥇\n"
        "- Each round has a <i>time limit</i>, and maps gradually shrinks because of poison gas. ☠️\n"
        "- Tie is possible if <i>both team members die at the same time. 👾</i>\n\n"
        "<b>Choose a map to see the layout and strategies: </b>"
    )
    video = FSInputFile(BASE_DIR / "media" / "Knockout_map.mp4")
    await message.answer_video(video=video, caption=info, parse_mode="HTML", reply_markup=knockout_maps)


@router.message(F.text == "Brawl Ball")
async def brawl_ball(message: Message):
    info = (
        "<b>Mode: Brawl Ball ⚽</b>\n\n"
        "<i>Description</i>: A 3v3 team mode where teams compete to score goals and defeat their opponents. The first team to score 2 goals wins the match. 🏆\n\n"
        "<b>Rules</b>:\n\n"
        "- Players can <i>carry, pass, and shoot</i> the ball to score goals. ⚽\n"
        "- Defeating an enemy causes them to <i>drop the ball</i> immediately. 💥\n"
        "- The match ends when a team scores <i>2 goals</i> or when the timer runs out. ⏱️\n"
        "- If the score is tied at the end of regulation time, <i>Overtime</i> begins. 🔥\n\n"
        "<b>Choose a map to see the layout and strategies: </b>"
    )
    video = FSInputFile(BASE_DIR / "media" / "BrawlBall_map.mp4")
    await message.answer_video(video=video, caption=info, parse_mode="HTML", reply_markup=brawl_ball_maps)


@router.message(F.text == "Heist")
async def heist(message: Message):
    info = (
        "<b>Mode: Heist 💰</b>\n\n"
        "<i>Description</i>: A 3v3 team mode where each team must destroy the enemy safe while protecting their own. 🔓\n\n"
        "<b>Rules</b>:\n\n"
        "- The first team to <i>destroy the enemy safe</i> wins instantly. 💥\n"
        "- If time runs out, the team that dealt <i>more damage to the enemy safe</i> wins. ⏱️\n"
        "- Players <i>respawn after a short delay</i> when defeated. 🔄\n"
        "- Focus on <i>both attacking and defending</i> to secure victory. 🛡️⚔️\n\n"
        "<b>Choose a map to see the layout and strategies:</b>"
    )
    video = FSInputFile(BASE_DIR / "media" / "Heist_map.mp4")
    await message.answer_video(video=video, caption=info, parse_mode="HTML", reply_markup=heist_maps)


@router.message(F.text == "Gem Grab")
async def gem_grab(message: Message):
    info = (
        "<b>Mode: Gem Grab 💎</b>\n\n"
        "<i>Description</i>: A 3v3 team mode where teams collect gems that spawn in the center of the map. 💜\n\n"
        "<b>Rules</b>:\n\n"
        "- Collect <i>10 gems</i> to start the countdown. ⏳\n"
        "- Hold the gems for <i>15 seconds</i> without losing them to win. 🏆\n"
        "- Defeated players <i>drop all their gems</i> on the ground. 💎\n"
        "- Players <i>respawn after a short delay</i>. 🔄\n\n"
        "<b>Choose a map to see the layout and strategies:</b>"
    )
    video = FSInputFile(BASE_DIR / "media" / "GemGrab_map.mp4")
    await message.answer_video(video=video, caption=info, parse_mode="HTML", reply_markup=gem_grab_maps)


@router.message(F.text == "Hot Zone")
async def hot_zone(message: Message):
    info = (
        "<b>Mode: Hot Zone 🔥</b>\n\n"
        "<i>Description</i>: A 3v3 team mode where teams capture and control special zones on the map. 🎯\n\n"
        "<b>Rules</b>:\n\n"
        "- Stand inside a <i>Hot Zone</i> to capture it. 📍\n"
        "- The first team to reach <i>100% capture progress</i> wins. 🏆\n"
        "- Players <i>respawn after a short delay</i> when defeated. 🔄\n"
        "- Stay in control of the zones while <i>keeping enemies out</i>. 🚫\n\n"
        "<b>Choose a map to see the layout and strategies:</b>"
    )
    video = FSInputFile(BASE_DIR / "media" / "HotZone_map.mp4")
    await message.answer_video(video=video, caption=info, parse_mode="HTML", reply_markup=hot_zone_maps)


@router.message(F.text == "Bounty")
async def bounty(message: Message):
    info = (
        "<b>Mode: Bounty ⭐</b>\n\n"
        "<i>Description</i>: A 3v3 team mode where you earn stars by defeating opponents. 🌟\n\n"
        "<b>Rules</b>:\n\n"
        "- Every elimination gives your team <i>stars</i>. ⭐\n"
        "- Defeated players <i>lose their bounty stars</i> to the enemy team. 💀\n"
        "- Players <i>respawn after a short delay</i>. 🔄\n"
        "- When time runs out, the team with <i>the most stars</i> wins. 🏆\n"
        "\n"
        "<b>Choose a map to see the layout and strategies:</b>"
    )
    video = FSInputFile(BASE_DIR / "media" / "Bounty_map.mp4")
    await message.answer_video(video=video, caption=info, parse_mode="HTML", reply_markup=bounty_maps)


@router.callback_query(F.data.startswith("map:"))
async def show_map(callback: CallbackQuery):
    _, mode_key, map_key = callback.data.split(":")
    mode_data = maps_data.get(mode_key, {})
    data = mode_data.get(map_key)

    if not data:
        await callback.answer("Map not found", show_alert=True)
        return

    pretty_map_name = data.get("title", map_key)
    map_description = data.get("description", "Unknown map description")
    
    text = (
        f"📍 <b>{pretty_map_name}</b>\n\n"
        f"📝 <b>Description:</b>\n{map_description}"
    )

    clean_path = data["image"].lstrip("/")
    photo_path = (BASE_DIR / clean_path).resolve()

    if not photo_path.exists():
        await callback.answer(f"Image not found: {clean_path}", show_alert=True)
        return

    map_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔥 Picks", callback_data=f"show_picks:{mode_key}:{map_key}")],
            [InlineKeyboardButton(text="⬅️ Back to Modes", callback_data="back_to_modes")]
        ]
    )

    await callback.message.delete()
    await callback.message.answer_photo(
        photo=FSInputFile(photo_path),
        caption=text,
        parse_mode="HTML",
        reply_markup=map_keyboard
    )
    await callback.answer()


@router.callback_query(F.data.startswith("show_picks:"))
async def show_map_brawlers_picks(callback: CallbackQuery):
    data_parts = callback.data.split(":")
    mode_key = data_parts[1]
    map_key = data_parts[2]

    current_index = int(data_parts[3]) if len(data_parts) > 3 else 0

    mode_data = maps_data.get(mode_key, {})
    map_data = mode_data.get(map_key, {})

    if not map_data:
        await callback.answer("Data error", show_alert=True)
        return

    picks_list = map_data.get("picks", [])
    if not picks_list:
        await callback.answer("No picks configured for this map.", show_alert=True)
        return

    if current_index >= len(picks_list) or current_index < 0:
        current_index = 0

    pick = picks_list[current_index]
    brawlers_text = ", ".join(pick.get("brawlers", []))

    pick_text = (
        f"📍 Map: <b>{map_data.get('title', map_key)}</b>\n"
        f"🌟 <b>{pick.get('name', f'Setup #{current_index + 1}')}</b> "
        f"({current_index + 1}/{len(picks_list)})\n\n"
        f"⚔️ <b>Team:</b> {brawlers_text}\n\n"
        f"📝 <b>Strategy:</b> {pick.get('description', 'Unknown strategy')}"
    )

    navigation_buttons = []

    if current_index > 0:
        navigation_buttons.append(
            InlineKeyboardButton(
                text="◀️ Prev",
                callback_data=f"show_picks:{mode_key}:{map_key}:{current_index - 1}"
            )
        )

    if current_index < len(picks_list) - 1:
        navigation_buttons.append(
            InlineKeyboardButton(
                text="Next ▶️",
                callback_data=f"show_picks:{mode_key}:{map_key}:{current_index + 1}"
            )
        )

    inline_keyboard = []

    if navigation_buttons:
        inline_keyboard.append(navigation_buttons)

    inline_keyboard.append(
        [
            InlineKeyboardButton(
                text="⬅️ Back to Map Layout",
                callback_data=f"map:{mode_key}:{map_key}"
            )
        ]
    )

    reply_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

    clean_pick_path = pick.get("photo", "").lstrip("/")
    pick_photo_path = (BASE_DIR / clean_pick_path).resolve()

    await callback.answer()

    if pick_photo_path.exists():
        media = InputMediaPhoto(
            media=FSInputFile(pick_photo_path),
            caption=pick_text,
            parse_mode="HTML"
        )

        try:
            await callback.message.edit_media(
                media=media,
                reply_markup=reply_markup
            )
        except Exception:
            await callback.message.delete()
            await callback.message.answer_photo(
                photo=FSInputFile(pick_photo_path),
                caption=pick_text,
                parse_mode="HTML",
                reply_markup=reply_markup
            )
    else:
        await callback.message.delete()
        await callback.message.answer(
            text=pick_text,
            parse_mode="HTML",
            reply_markup=reply_markup
        )

@router.message(CharacterStates.waiting_for_name, F.text)
async def show_character_info(message: Message, state: FSMContext):
    user_name = message.text.strip()
    character_name = None

    for name in characters_data:
        if name.lower() == user_name.lower():
            character_name = name
            break

    if character_name is None:
        for name, data in characters_data.items():
            aliases = data.get("alises", [])  
            if any(alias.lower() == user_name.lower() for alias in aliases):
                character_name = name
                break

    if character_name is None:
        lower_name = {name.lower(): name for name in characters_data.keys()}
        result = process.extractOne(user_name.lower(), lower_name.keys(), score_cutoff=70)
        if result:
            character_name = lower_name[result[0]]

    if character_name is None:
        await message.answer(
            "<b>❌Character not found❌</b> \n"
            "Please check the name spelling and try again.",
            parse_mode="HTML",
            reply_markup=back_to_menu_characters
        )
        return

    data = characters_data[character_name]
    clean_path = data['image'].lstrip("/")
    photo_path = (BASE_DIR / clean_path).resolve()

    if not photo_path.exists():
        await message.answer(f"❌ Image for {character_name} not found on server.")
        return

    text = (
        f"<b>{character_name}</b>\n\n"
        f" <i>🎭Class:</i> {data['class']}\n"
        f" <i>💎Rarity:</i> {data['rarity']}\n"
        f" <i>⚔️MAX Damage:</i> {data['damage']}\n"
        f" <i>🛡️MAX Health:</i> {data['health']}\n"
        f" <i>⏳MAX reload speed:</i> {data['reload']}\n"
        f" <i>🏹MAX range:</i> {data['range']}\n"
        f" <i>🔥Super:</i> {data['super']}\n\n"
        "<b>🕹️Gadgets</b>:\n\n"
        f" · {data['gadgets'][0]}\n\n"
        f" · {data['gadgets'][1]}\n\n"
        "<b>💫Star Powers</b>:\n\n"
        f" · {data['passives'][0]}\n\n"
        f" · {data['passives'][1]}\n\n"
    )

    await message.answer_photo(
        photo=FSInputFile(photo_path),
        caption=text,
        reply_markup=back_to_menu_characters,
        parse_mode="HTML"
    )

    brawler_picks = data.get("brawler_picks", [])
    for index, pick in enumerate(brawler_picks):
        brawlers_text = ", ".join(pick.get("brawlers", []))
        
        pick_text = (
            f"🔥 <b>{pick.get('name', f'Setup #{index + 1}')}</b>\n\n"
            f"⚔️ <b>Team Composition:</b> {brawlers_text}\n\n"
            f"📝 <b>Strategy:</b> {pick.get('description', 'Unknown strategy')}"
        )

        clean_pick_path = pick.get("photo", "").lstrip("/")
        pick_photo_path = (BASE_DIR / clean_pick_path).resolve()

        if pick_photo_path and pick_photo_path.exists():
            await message.answer_photo(
                photo=FSInputFile(pick_photo_path),
                caption=pick_text,
                parse_mode="HTML"
            )
        else:
            await message.answer(
                text=pick_text,
                parse_mode="HTML"
            )