import asyncio
import logging
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
import re
import sys
from os import getenv
from config import BANNED_USERS
from dotenv import load_dotenv
import config
from ZelzalMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       is_on_off,
                                       )

# تكوين سجل التسجيلات
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

OWNER_ID = getenv("OWNER_ID")
OWNER_ID = int(getenv("OWNER_ID", ""))


@app.on_message(command(["السورس", "المطور", "البرمجه"]))
async def zohary(client: Client, message: Message):
    logging.debug('بدء تنفيذ الأمر المطور')
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    user = await client.get_chat(OWNER_ID)
    Bio = user.bio
    logging.debug(f'الحصول على معلومات المستخدم: {usr}')
    logging.debug(f'الحصول على معلومات المستخدم: {user}')
    async for photo in client.iter_profile_photos(OWNER_ID, limit=1):
        await message.reply_photo(photo.file_id, caption=f"""Ⴆ᥆ƚ ᥆᭙ꪀᥱᖇ | - [{usr.first_name}](tg://user?id={OWNER_ID}) 
                         
ႦᎥ᥆ | - {Bio}         

Ꭵժ | - {OWNER_ID}  """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"tg://user?id={OWNER_ID}")
            ],                   
          ]              
       )                 
    )                    
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name
    logging.debug(f'إرسال رسالة إلى المطور: الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}')
    await app.send_message(OWNER_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
    if await is_on_off(config.LOG):
        logging.debug(f'تسجيل الحدث: الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}')
        await app.send_message(
            config.LOGGER_ID,
            f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}",
        )