import os

from aiogram import Router , F
from aiogram.types import Message , CallbackQuery

from keyboards import modes_menu , main_menu

from keyboards import knockout_maps 
from pathlib import Path
from aiogram.types import FSInputFile

router = Router()

@router.message(lambda msg: msg.text == "Mode info")
async def choose_mode(message: Message):
    await message.answer(
        "Choose a mode: ",
        reply_markup=modes_menu 
    )


@router.message(lambda msg: msg.text == "Knockout")
async def show_knockout(message: Message):
    # Приклад карт і інформації про режим "Нокаут"
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
    
    video_path = Path("media") / "Knockout_map.mp4"
    video = FSInputFile(video_path)
    await message.answer_video(
        caption = info,
        video = video,
        parse_mode = "HTML",
        reply_markup = knockout_maps)


@router.message(lambda msg: msg.text == "Brawl Ball")
async def show_brawl_ball(message: Message):
    info = (
    "<b>Mode: Brawl Ball ⚽</b>\n\n"
    "<i>Description</i>: A 3v3 team mode where teams compete to score goals and defeat their opponents. The first team to score 2 goals wins the match. 🏆\n\n"
    "<b>Rules</b>:\n\n"
    "- Players can <i>carry, pass, and shoot</i> the ball to score goals. ⚽\n\n"
    "- Defeating an enemy causes them to <i>drop the ball</i> immediately. 💥\n\n"
    "- The match ends when a team scores <i>2 goals</i> or when the timer runs out. ⏱️\n\n"
    "- If the score is tied at the end of regulation time, <i>Overtime</i> begins. During Overtime, obstacles are destroyed to make scoring easier. 🔥\n\n"
    "- The team with the most goals at the end of the match wins. 🥇\n\n"
    "<b>Choose a map to see the layout and strategies: </b>")

    video_path = Path("media") / "BrawlBall_map.mp4"
    video = FSInputFile(video_path)
    await message.answer_video(
        caption = info,
        video = video,
        parse_mode = "HTML",)
        

@router.message(lambda msg: msg.text == "Heist")
async def show_heist(message: Message):
    info = (
    "<b>Mode: Heist 💰</b>\n\n"
    "<i>Description</i>: A 3v3 team mode where teams must protect their own Safe while trying to destroy the enemy Safe. The first team to destroy the opposing Safe wins, or the team with the most Safe health remaining when time runs out. 🏆\n\n"
    "<b>Rules</b>:\n\n"
    "- Each team has a <i>Safe</i> that must be defended from enemy attacks. 🔒\n\n"
    "- Players can attack both enemy Brawlers and the enemy <i>Safe</i>. 💥\n\n"
    "- The match ends immediately if a team's Safe is completely destroyed. 💣\n\n"
    "- If neither Safe is destroyed before the timer ends, the team with the higher Safe health percentage wins. ⏱️\n\n"
    "- Controlling the map and creating opportunities to deal damage to the enemy Safe is the key to victory. 🎯\n\n"
    "- Strong offense and reliable defense are both important for success. 🥇\n\n"
    "<b>Choose a map to see the layout and strategies: </b>")


    video_path = Path('media') / 'Heist_map.mp4'
    video = FSInputFile(video_path)
    await message.answer_video(
        caption = info,
        video = video,
        parse_mode = "HTML",)
    

@router.message(lambda msg: msg.text == "Gem Grab")
async def show_gem_grab(message: Message):
    info = ("<b>Mode: Gem Grab 💎</b>\n\n"
"<i>Description</i>: A 3v3 team mode where teams battle to collect Gems that spawn from the center Gem Mine. Hold 10 Gems and survive the countdown to win the match. 🏆\n\n"
"<b>Rules</b>:\n\n"
"- Gems continuously spawn from the <i>Gem Mine</i> located in the center of the map. 💎\n\n"
"- Players can collect and carry Gems for their team. 🎒\n\n"
"- When a player is defeated, they <i>drop all carried Gems</i> on the ground. 💥\n\n"
"- A team that collects <i>10 or more Gems</i> starts a 15-second countdown. ⏳\n\n"
"- If the countdown reaches zero, that team wins the match. 🥇\n\n"
"- Defeating Gem carriers can stop the countdown and give your team a chance to recover. ⚔️\n\n"
"<b>Choose a map to see the layout and strategies: </b>"
    )

    video_path = Path('media') / 'GemGrab_map.mp4'
    video = FSInputFile(video_path)
    await message.answer_video(
        caption = info,
        video = video,
        parse_mode = "HTML",)
    

@router.message(lambda msg: msg.text == "Hot Zone")
async def show_hot_zone(message: Message):
    info = ("<b>Mode: Hot Zone 🔥</b>\n\n"
    "<i>Description</i>: A 3v3 team mode where teams fight to control designated Hot Zones on the map. Capture and hold the zones to fill your team's progress bar and win the match. 🏆\n\n"
    "<b>Rules</b>:\n\n"
    "- Stand inside a <i>Hot Zone</i> to capture it and earn progress for your team. 🔥\n\n"
    "- Multiple teammates inside the same zone capture it faster. ⚡\n\n"
    "- If both teams are in a zone at the same time, it becomes <i>contested</i> and no progress is earned. ⚔️\n\n"
    "- Some maps contain multiple Hot Zones that must be controlled throughout the match. 🗺️\n\n"
    "- The first team to reach <i>100% capture progress</i> wins instantly. 🥇\n\n"
    "- If time runs out, the team with the highest capture percentage wins the match. ⏱️\n\n"
    "<b>Choose a map to see the layout and strategies: </b>"
    )
    video_path = Path('media') / 'HotZone_map.mp4'
    video = FSInputFile(video_path)
    await message.answer_video(
        caption = info,
        video = video,
        parse_mode = "HTML",)
    

@router.message(lambda msg: msg.text == "Bounty")
async def show_bounty(message: Message):
    info = ("<b>Mode: Bounty ⭐</b>\n\n"
    "<i>Description</i>: A 3v3 team mode where teams earn Stars by defeating opponents. The team with the most Stars when the timer runs out wins the match. 🏆\n\n"
    "<b>Rules</b>:\n\n"
    "- Defeating an enemy grants your team <i>Stars</i>. ⭐\n\n"
    "- Each player starts with a bounty worth <i>2 Stars</i>, which increases as they score eliminations. 📈\n\n"
    "- The more Stars a player carries, the more valuable they become to the enemy team. 🎯\n\n"
    "- When a player is defeated, the opposing team earns Stars equal to that player's bounty. 💥\n\n"
    "- A special <i>Blue Star</i> appears in the center at the start of the match and acts as a tiebreaker. 🔵\n\n"
    "- When time runs out, the team with the most Stars wins the match. 🥇\n\n"
    "<b>Choose a map to see the layout and strategies: </b>"
    )
    video_path = Path('media') / 'Bounty_map.mp4'
    video = FSInputFile(video_path)
    await message.answer_video(
        caption = info,
        video = video,
        parse_mode = "HTML",)



@router.message(F.text == "Back")
async def back_to_main_menu(message: Message):
    await message.answer(
        "Main menu:",
        reply_markup=main_menu
    )

@router.callback_query(F.data == "back_to_modes")
async def back_to_modes(callback: CallbackQuery):
    await callback.message.answer(
        "Choose a mode:",
        reply_markup=modes_menu
    )
    await callback.answer()