from pyrogram import Client
from pyrogram import filters
from telegram import Update
from random import shuffle
from pyrogram.types import Message
from Dolphin_bot import oyun
from Dolphin_bot.helpers.kelimeler import *
from Dolphin_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_callback_query(filters.regex(r"jumbled_button"))
async def jumbled_button(_, query: CallbackQuery):
    global oyun
    aktif = False
    try:
        aktif = oyun[CallbackQuery.message.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await query.edit_message_text("**❗Tʜᴇ  Gᴀᴍᴇ  Is  Aʟʀᴇᴀᴅʏ  Iɴ  Pʀᴏɢʀᴇss  Iɴ  Yᴏᴜʀ  Gʀᴏᴜᴘ  ✍🏻  \n  Tᴏ  Sᴛᴏᴘ  Tʜᴇ  Gᴀᴍᴇ,  Yᴏᴜ  Cᴀɴ  Tʏᴘᴇ  /cancel")
    else:
        await query.edit_message_text(f"""🎯 Rᴏᴜɴᴅ : {oyun[CallbackQuery.message.chat.id]['round']}/60 \n💵 Pᴏɪɴᴛs  Eᴀʀɴᴇᴅ : 1 \n📝 Wᴏʀᴅ :   <code>{kelime_list}</code> \n🎲 Cʟᴜᴇ : {oyun[CallbackQuery.message.chat.id]["kelime"][0]} \n✍🏻 Lᴀʀɢᴇ : {int(len(kelime_list)/2)} \n✏️ Fɪɴᴅ  Tʜᴇ  Cᴏʀʀᴇᴄᴛ  Wᴏʀᴅ  Fʀᴏᴍ  Tʜᴇ  Jᴜᴍʙʟᴇᴅ  Lᴇᴛᴛᴇʀs""", reply_markup=kanal)

        oyun[CallbackQuery.message.chat.id] = {"kelime":kelime_sec()}
        oyun[CallbackQuery.message.chat.id]["aktif"] = True
        oyun[CallbackQuery.message.chat.id]["round"] = 1
        oyun[CallbackQuery.message.chat.id]["pass"] = 0
        oyun[CallbackQuery.message.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[CallbackQuery.message.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
   
