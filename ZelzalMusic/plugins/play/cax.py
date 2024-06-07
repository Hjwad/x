@app.on_message(command(["مطور", "المطور"]) & filters.group)
async def zilzal(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    async for photo in client.iter_profile_photos(OWNER_ID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""ٴ<b>•✯ سورس الزعيم ✯•</b>
                    
- 𝚆𝙾𝙽𝙴𝚁 :[{usr.first_name}](https://t.me/{OWNER})
- 𝚄𝚂𝙴𝚁 :@{usrnam} 
- 𝙸𝙳 :`{usr.id}`
 
ٴ<b>•✯ سورس الزعيم ✯•</b> """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{usrnam}"),
            ],[
              InlineKeyboardButton("•✯ سورس الزعيم ✯•", url="https://t.me/rr_r_v"),
            ],
          ]
       )                 
    )                    
                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    senderuser = message.from_user.username
                    sender_user = "@{senderuser}" if senderuser else "لا يوجـد"
                    await app.send_message(OWNER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
                    return await app.send_message(LOGGER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")