import os
import requests
import yt_dlp
from pyrogram import filters
from strings.filters import command
from youtube_search import YoutubeSearch
from ZelzalMusic import app

@app.on_message(command(["/song", "بحث","تحميل","تنزيل","يوت","yt"]))
def song(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = message.from_user.mention

    query = ""
    for i in message.command[1:]:
        query += " " + str(i)
    print(query)
    m = message.reply("جاري البحث لحظة...")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)

    except Exception as e:
        m.edit(
            "لم يتم العثور على الأغنية، يرجى المحاولة مرة أخرى!"
        )
        print(str(e))
        return
    m.edit("جارٍ التنزيل... الرجاء الانتظار!")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"الاسم: {title[:25]}\nبواسطة:​ {chutiya}"
        message.reply_audio(
            audio_file,
            caption=rep,
            performer="@mmmsc .",
            thumb=thumb_name,
            title=title,
        )
        m.delete()
    except Exception as e:
        m.edit(
            f"[Victorious] **\n\**خطأ :** {e}"
        )
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

__mod_name__ = "اليوتيوب"
__help__ = """
بحث أو تحميل مع رابط الأغنية أو اسمها """