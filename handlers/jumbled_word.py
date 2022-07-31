from telegram import Client
from telegram import filters
from random import shuffle
from telegram.ext import oyun
from telegram.ext.helpers.kelimeler import *
from telegram.ext.helpers.keyboards import *
from telegram.errors import FloodWait
from telegram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler
import mongo.chats as db
from helpers.game import new_game
from helpers.game import end_game
from helpers.wrappers import nice_errors

@nice_errors
def callback(update: Update, context: CallbackContext):
    new_game(update.effective_user, context)
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗Tʜᴇ  Gᴀᴍᴇ  Is  Aʟʀᴇᴀᴅʏ  Iɴ  Pʀᴏɢʀᴇss  Iɴ  Yᴏᴜʀ  Gʀᴏᴜᴘ  ✍🏻  \n  Tᴏ  Sᴛᴏᴘ  Tʜᴇ  Gᴀᴍᴇ,  Yᴏᴜ  Cᴀɴ  Tʏᴘᴇ  /cancel")
    else:
        await m.reply(f"**{update.effective_user.mention_html()}** Bʏ!    \n Tʜᴇ  Wᴏʀᴅ  Fɪɴᴅɪɴɢ  Gᴀᴍᴇ  Hᴀs  Sᴛᴀʀᴛᴇᴅ.\n \n Gᴏᴏᴅ  Lᴜᴄᴋ !", reply_markup=kanal)
        
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

  handler = CallbackQueryHandler(callback, pattern='jumbled_word')



