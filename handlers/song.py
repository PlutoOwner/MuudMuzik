import wget
import os, youtube_dl, requests, time

from youtube_search import YoutubeSearch

from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
import yt_dlp
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery 
from yt_dlp import YoutubeDL
from config import BOT_USERNAME, PLAYLIST_NAME, PLAYLIST_ID

ydl_opts = {
    'format': 'best',
    'keepvideo': True,
    'prefer_ffmpeg': False,
    'geo_bypass': True,
    'outtmpl': '%(title)s.%(ext)s',
    'quite': True
}


  
#music indirme#

@Client.on_message(filters.command(["bul", "song"]) & ~filters.edited)
async def bul(_, message):
    query = " ".join(message.command[1:])
    m = await message.reply("<b>Şarkınız Aranıyor ... 🔍</b>")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        await m.edit("<b>❌ Üzgünüm şarkı bulunamadı.\n\n Lütfen başka şarkı ismi söyleyin.</b>")
        print(str(e))
        return
    await m.edit("<b>📥 İndirme İşlemi Başladı...</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**00:00 ━━━●───── {duration}\n⇆ㅤ◁ㅤ❚❚ㅤ▷**"
        res = f"**00:00━━━●───── {duration}\n⇆ㅤ◁ㅤ❚❚ㅤ▷\n\n💡 Bot @{BOT_USERNAME}\n\n@{PLAYLIST_NAME} ❤️‍🩹**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await m.edit("📤 Yükleniyor..")
        await message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="@PlutoFm", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎧 𝐌𝐮̈𝐳𝐢𝐤 𝐊𝐚𝐧𝐚𝐥ı", url=f"https://t.me/{PLAYLIST_NAME}")]]))
        await m.delete()
        await _.send_audio(chat_id=PLAYLIST_ID, audio=audio_file, caption=res, performer="@PlutoFm", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        await m.edit("<b>❌ Hatanın, düzelmesini bekleyiniz.</b>")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)



@Client.on_message(
    filters.command(["video", "vsong"]) & ~filters.edited
)
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("📥 **video indiriyorum...**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **Hata:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("📤 **video yüklüyorum...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)
