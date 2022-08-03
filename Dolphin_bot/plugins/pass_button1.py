from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from Dolphin_bot.helpers.keyboards import *
from Dolphin_bot.helpers.kelimeler import kelime_sec
from Dolphin_bot import *

@Client.on_message(filters.command("pass_button") & ~filters.private & ~filters.channel)
async def pass_button(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["pass"] < 3:
            oyun[m.chat.id]["pass"] += 1 
            await c.send_message(m.chat.id,f"❗  Yᴏᴜ  Hᴀᴠᴇ  3  Pᴀssᴇs  Iɴ  Tᴏᴛᴀʟ!\n➡️  Wᴏʀᴅ  Pᴀss  Is  ᴏᴜᴛ! \n✏️  Cᴏʀʀᴇᴄᴛ  Wᴏʀᴅ 🥳 : **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)

            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
🎯 Rᴏᴜɴᴅ : {oyun[m.chat.id]['round']}/60 
💵 Pᴏɪɴᴛs  Eᴀʀɴᴇᴅ : 1
📝 Wᴏʀᴅ :   <code>{kelime_list}</code>
🎲 Cʟᴜᴇ : {oyun[m.chat.id]["kelime"][0]}
✍🏻 Lᴀʀɢᴇ : {int(len(kelime_list)/2)} 
✏️ Fɪɴᴅ  Tʜᴇ  Cᴏʀʀᴇᴄᴛ  Wᴏʀᴅ  Fʀᴏᴍ  Tʜᴇ  Jᴜᴍʙʟᴇᴅ  Lᴇᴛᴛᴇʀs
            """
            await c.send_message(m.chat.id, text)

