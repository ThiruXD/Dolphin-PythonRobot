
import random
from pyrogram.types import *
from pyrogram import __version__ as pyro
from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from Dolphin_bot import oyun
from Dolphin_bot.helpers.kelimeler import *
from Dolphin_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

GAM_IMG = (
      "https://telegra.ph/file/357a3279b2960dd79a549.jpg",
  )


GAME_TEXT = """
** ➤  Eɴᴊᴏʏ  Wɪᴛʜ  Yᴏᴜʀ  Fʀɪᴇɴᴅs ✨..**
"""
buttons = [
    [
        InlineKeyboardButton("✍  Wᴏʀᴅ  Pᴀʀᴀᴘʜʀᴀsᴇ", callback_data="paraphrase"),
    ],
    [
        InlineKeyboardButton("Jᴜᴍʙʟᴇᴅ  Lᴇᴛᴛᴇʀs 🆎", callback_data="jumbled_button"),
    ]
]


# Komutlar. 
@Client.on_message(filters.command("game"))
async def start(_, m):
             await m.reply_photo(
               photo=random.choice(GAM_IMG),
                caption=GAME_TEXT.format(m.from_user.mention),                   
                reply_markup=InlineKeyboardMarkup(buttons))

