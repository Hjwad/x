import asyncio

from Auput import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME, OWNER_USERNAME, SUPPORT_CHANNEL
from Auput.utils.bk import command

@app.on_message(filters.command("سورس", ["/", ".", "!",""]))
async def kontolmasukmemek(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/536acb5435c3afe9e5fd6.mp4",
        caption=f"- Hi {message.from_user.mention}\n\n I am {MUSIC_BOT_NAME}\n\n I am Fast and Powerful music player bot with some awesome features.\n\n||Yowai Mo 🍓.||",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="↺ ˹᥉ꪮ᥉˼ 𒂟", url=f"https://t.me/{OWNER_USERNAME}"
            ),
            InlineKeyboardButton(
                text="Not ᥉ꪮ᥉", url=f"{SUPPORT_CHANNEL}"
            ),
        ],
                [
                    InlineKeyboardButton(
                        "ᴄʟᴏsᴇ", callback_data="close"
                    )
                ],
            ]
        )
    )