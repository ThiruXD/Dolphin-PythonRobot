from pyrogram import Client
from pyrogram import filters
from telegram import Update
from random import shuffle
from pyrogram.types import Message
from Dolphin_bot import oyun
from Dolphin_bot.helpers.kelimeler import *
from Dolphin_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_callback_query(filters.regex(r"jumbled_button"))
async def kelimeoyun(_, query: CallbackQuery, message: Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[message.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await message.reply("**❗Tʜᴇ  Gᴀᴍᴇ  Is  Aʟʀᴇᴀᴅʏ  Iɴ  Pʀᴏɢʀᴇss  Iɴ  Yᴏᴜʀ  Gʀᴏᴜᴘ  ✍🏻  \n  Tᴏ  Sᴛᴏᴘ  Tʜᴇ  Gᴀᴍᴇ,  Yᴏᴜ  Cᴀɴ  Tʏᴘᴇ  /cancel")
    else:
        await message.reply_text(f"""🎯 Rᴏᴜɴᴅ : {oyun[message.chat.id]['round']}/60 \n💵 Pᴏɪɴᴛs  Eᴀʀɴᴇᴅ : 1 \n📝 Wᴏʀᴅ :   <code>{kelime_list}</code> \n🎲 Cʟᴜᴇ : {oyun[message.chat.id]["kelime"][0]} \n✍🏻 Lᴀʀɢᴇ : {int(len(kelime_list)/2)} \n✏️ Fɪɴᴅ  Tʜᴇ  Cᴏʀʀᴇᴄᴛ  Wᴏʀᴅ  Fʀᴏᴍ  Tʜᴇ  Jᴜᴍʙʟᴇᴅ  Lᴇᴛᴛᴇʀs""", reply_markup=kanal)

        oyun[message.chat.id] = {"kelime":kelime_sec()}
        oyun[message.chat.id]["aktif"] = True
        oyun[message.chat.id]["round"] = 1
        oyun[message.chat.id]["pass"] = 0
        oyun[message.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[message.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
