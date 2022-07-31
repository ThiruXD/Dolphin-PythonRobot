from pyrogram import Client
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)
from random import shuffle
from pyrogram.types import Message
from pyrogram import __version__ as pyro
from pyrogram.types import *
from Dolphin_bot import oyun
from Dolphin_bot.helpers.kelimeler import *
from Dolphin_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

# Oyunu başlat. 
@Client.on_callback_query(filters.regex("jumbled"))
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗  Tʜᴇ  Gᴀᴍᴇ  Is  Aʟʀᴇᴀᴅʏ  Iɴ  Pʀᴏɢʀᴇss  Iɴ  Yᴏᴜʀ  Gʀᴏᴜᴘ  ✍🏻  \n  Tᴏ  Sᴛᴏᴘ  Tʜᴇ  Gᴀᴍᴇ,  Yᴏᴜ  Cᴀɴ  Tʏᴘᴇ  /cancel .")
    else:
        await m.reply(f"**{m.from_user.mention}** Bʏ!    \n Tʜᴇ  Wᴏʀᴅ  Fɪɴᴅɪɴɢ  Gᴀᴍᴇ  Hᴀs  Sᴛᴀʀᴛᴇᴅ.\n \n Gᴏᴏᴅ  Lᴜᴄᴋ !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["pass"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Rᴏᴜɴᴅ : {oyun[m.chat.id]['round']}/60 
📝 Wᴏʀᴅ :   <code>{kelime_list}</code>
💰 Pᴏɪɴᴛs  Eᴀʀɴᴇᴅ : 1
🔎 I𝗉𝗎𝖼𝗎 : 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Lᴀʀɢᴇ : {int(len(kelime_list)/2)} 

✏️ Fɪɴᴅ  Tʜᴇ  Cᴏʀʀᴇᴄᴛ  Wᴏʀᴅ  Fʀᴏᴍ  Tʜᴇ  Jᴜᴍʙʟᴇᴅ  Lᴇᴛᴛᴇʀs
        """
        await c.send_message(m.chat.id, text) 
  
  dispatcher.add_handler(jumbled_callback_handler)
