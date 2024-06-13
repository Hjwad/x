#sos


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from ZelzalMusic import app
import config


@app.on_message(
    command(["المطور", "السورس", "المصنع"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/ed1651affb1ae9e964550.jpg",
        caption="~ Not ᥉ꪮ᥉ . \n~ Dev BY ᥉ꪮ᥉ 🍓.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- Dev Bot .", url=f"https://t.me/SSSi5"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- Not ᥉ꪮ᥉ . ", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )