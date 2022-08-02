from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from Dolphin_bot import oyun
from Dolphin_bot.helpers.kelimeler import *
from Dolphin_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_callback_query(filters.regex(r"jumbled_button"))
async def jumbled_button(c:Client, m:Message):
    if aktif:
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
        
        text_down = f"""
🎯 Rᴏᴜɴᴅ : {oyun[m.chat.id]['round']}/60 
💵 Pᴏɪɴᴛs  Eᴀʀɴᴇᴅ : 1
📝 Wᴏʀᴅ :   <code>{kelime_list}</code>
🎲 Cʟᴜᴇ : {oyun[m.chat.id]["kelime"][0]}
✍🏻 Lᴀʀɢᴇ : {int(len(kelime_list)/2)} 

✏️ Fɪɴᴅ  Tʜᴇ  Cᴏʀʀᴇᴄᴛ  Wᴏʀᴅ  Fʀᴏᴍ  Tʜᴇ  Jᴜᴍʙʟᴇᴅ  Lᴇᴛᴛᴇʀs
        """
        await m.reply_text(text_down)
