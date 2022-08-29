import os, youtube_dl, requests, time
from config import Config
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
import yt_dlp
from telethon import TelegramClient, events
from telethon import Button
from telethon import Button
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)


#config#

bot = Client(
    'moonBot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
client = TelegramClient('client', api_id = Config.API_ID, api_hash = Config.API_HASH).start(bot_token = Config.BOT_TOKEN )
 
#start mesajı






anlik_calisan = []

ozel_list = [1601353177]





grup_sayi = [] 

sayı_calısan = []

@client.on(events.NewMessage(pattern='^/reload ?(.*)'))

async def chatid(event):

    global grup_sayi




  


    

      

         

@client.on(events.NewMessage(pattern='^/start@youtubevcprobot ?(.*)'))

async def chatid(event):

    global grup_sayi

@client.on(events.NewMessage())

async def chatid(event):

  global etiketuye

  if event.is_group:

    if event.chat_id in grup_sayi:

      pass

    else:

      grup_sayi.append(event.chat_id)
@client.on(events.NewMessage())
async def mentionalladmin(event):
  global grup_sayi
  if event.is_group:
    if event.chat_id in grup_sayi:
      pass
    else:
      grup_sayi.append(event.chat_id)

@client.on(events.NewMessage(pattern='^/statik ?(.*)'))
async def son_durum(event):
    global anlik_calisan,grup_sayi,ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**Grup sayısı 🤖**\n\nToplam Grup: `{len(grup_sayi)}`")
                        

 
@client.on(events.NewMessage(pattern='^/deep ?(.*)'))
async def destek(event):
   await client.send_message(event.chat_id, "**Bot Sorunsuz Çalışıyor KRAL**",
                     buttons=(
                      [
                       Button.url('🧑‍💻~𝐒𝐚𝐡𝐢𝐛𝐢𝐦~🧑‍💻', f'https://t.me/YoutubeVcsahip'),
                       Button.url('🧑‍💻~𝐘𝐞𝐭𝐤𝐢𝐥𝐢𝐦~🧑‍💻', f'https://t.me/MissSahip')
                      ]
                    )
                  )    
#musik indirme#

@bot.on_message(filters.command("bul") & ~filters.edited)
def bul(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("<b>• 🔍 𝐀𝐑𝐀𝐍𝐈𝐘𝐎𝐑...</b>")
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
        m.edit("<b>⛔ **❌ Ş𝚊𝚛𝚔ı 𝙱𝚞𝚕𝚞𝚗𝚊𝚖𝚊𝚍ı.\n\n 𝙻𝚄̈𝚃𝙵𝙴𝙽 𝙶𝙴𝙲̧𝙴𝚁𝙻𝙸̇ 𝙱𝙸̇𝚁 𝚂̧𝙰𝚁𝙺𝙸 𝙰𝙳𝙸 𝚅𝙴𝚁𝙸̇𝙽.**</b>")
        print(str(e))
        return
        m.edit("<b>•> 📥 𝙸̇𝙽𝙳𝙸̇𝚁𝙼𝙴 𝙸̇𝚂̧𝙻𝙴𝙼𝙸̇ 𝙱𝙰𝚂̧𝙻𝙰𝚃𝙸𝙻𝙳𝙸...**</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        kisi = f"@{message.from_user.username}"

        mel = f"╔═══════════════╗\nYouTubeMusic\n\n➤🏷Başlık :{audio_file}\n\n➤👤Talep Eden :{kisi}\n\n➤🤖Bot :@YoutubeVcProBot\n\n╚══════════════╝"

        
        rep = f"🎶 𝐈̇𝐍𝐃𝐈̇𝐑𝐈̇𝐋𝐃𝐈̇ 🎶"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("•> **Yükleniyor**...")
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="@YouTubeVcProBot"buttons=([Button.url('🎧 YouTube  Music 🎶',f'https://t.me/YoutubeVcMuzik') ]))
        m.delete()
        bot.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=mel, performer="@YouTubeVcProBot", parse_mode='md', title=title, duration=dur, thumb=thumb_name)

    except Exception as e:
        m.edit("<b>⛔ **Hatanın düzelmesini bekleyin** .</b>")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

bot.run()
