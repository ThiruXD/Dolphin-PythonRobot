import importlib
import time
import random
import re
from sys import argv
from typing import Optional
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown


HMF_IMG = (
      "https://telegra.ph/file/9332b113ddb8555bf6ffe.jpg",
      "https://telegra.ph/file/357a3279b2960dd79a549.jpg",
  )


PM_START_TEXT = """
**🔮 {} 🔮  Hᴇʟʟᴏ,  Wᴇʟᴄᴏᴍᴇ  Tᴏ  Mᴀᴊᴇsᴛʏ  Wᴏʀᴅ  Bᴏᴛ,  Yᴏᴜ  Cᴀɴ  Pʟᴀʏ  Wᴏʀᴅ  Dᴇʀɪᴠᴀᴛɪᴏɴ  Gᴀᴍᴇ  Oʀ  Wᴏʀᴅ  Nᴀʀʀᴀᴛɪᴏɴ  Wɪᴛʜ  Tʜɪs  Bᴏᴛ ✨.

➤  Cʟɪᴄᴋ  👉  /help  Fᴏʀ  Iɴғᴏʀᴍᴀᴛɪᴏɴ. ᴛʜᴇ  Cᴏᴍᴍᴀɴᴅs  Aʀᴇ  Eᴀsʏ  Aɴᴅ  Sɪᴍᴘʟᴇ 💖

➤  Eɴᴊᴏʏ  Wɪᴛʜ  Yᴏᴜʀ  Fʀɪᴇɴᴅs ✨..**
"""
buttons = [
    [
        InlineKeyboardButton("➕ Aᴅᴅ  Tᴏ  Yᴏᴜʀ  Gʀᴏᴜᴘ ➕", url=f"http://t.me/DolphinGameBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("📢  Uᴘᴅᴀᴛᴇs", url="https://t.me/+u-YFXF8x-Rw0M2Rl"),
        InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ ⚠️", url="https://t.me/+u-YFXF8x-Rw0M2Rl"),
    ],
    [
        InlineKeyboardButton("📚  Cᴏᴍᴍᴀɴᴅs  Aɴᴅ  Hᴇʟᴘ  📚", callback_data="host"),   
    ],
]



HELP = """
**✌️  Wᴇʟᴄᴏᴍᴇ  Tᴏ  Cᴏᴍᴍᴀɴᴅs  Mᴇɴᴜ.**

/game  -  Gᴇɴᴇʀᴀᴛᴇ  Wᴏʀᴅ  Sᴛᴀʀᴛs  Tʜᴇ  Gᴀᴍᴇ.
  /pass  -  Pᴀss  Tʜᴇ  Wᴏʀᴅ.
  /score  -  Cᴏᴍᴘᴇᴛɪᴛɪᴠᴇ  Iɴғᴏʀᴍᴀᴛɪᴏɴ  Bᴇᴛᴡᴇᴇɴ  Pʟᴀʏᴇʀs.
  /cancel  -  Eɴᴅs  Tʜᴇ  Wᴏʀᴅ  Dᴇʀɪᴠᴀᴛɪᴏɴ  Gᴀᴍᴇ.
"""

       
    def start(update: Update, context: CallbackContext):
             await m.reply_photo(
               photo=random.choice(HMF_IMG),
                caption=PM_START_TEXT.format(m.from_user.mention),                   
                reply_markup=InlineKeyboardMarkup(buttons))
          )


    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)
