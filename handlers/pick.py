import os

from aiogram import Router
from aiogram.types import Message

from keyboards import modes_menu

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
        

    