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

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(_, m):
             await m.reply_photo(
               photo=random.choice(HMF_IMG),
                caption=PM_START_TEXT.format(m.from_user.mention),                   
                reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/dd8c2a4a6a2294682e892.jpg",caption=HELP) 


 



        
