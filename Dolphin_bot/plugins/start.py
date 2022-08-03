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
        InlineKeyboardButton("📚  Cᴏᴍᴍᴀɴᴅs  Aɴᴅ  Hᴇʟᴘ  📚", callback_data="bhelp"),   
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


 
@Client.on_callback_query(filters.regex("bstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hᴇʟʟᴏ,  Wᴇʟᴄᴏᴍᴇ  Tᴏ  Mᴀᴊᴇsᴛʏ  Wᴏʀᴅ  Bᴏᴛ,  Yᴏᴜ  Cᴀɴ  Pʟᴀʏ  Wᴏʀᴅ  Dᴇʀɪᴠᴀᴛɪᴏɴ  Gᴀᴍᴇ  Oʀ  Wᴏʀᴅ  Nᴀʀʀᴀᴛɪᴏɴ  Wɪᴛʜ  Tʜɪs  Bᴏᴛ ✨.

➤  Cʟɪᴄᴋ  👉  /help  Fᴏʀ  Iɴғᴏʀᴍᴀᴛɪᴏɴ. ᴛʜᴇ  Cᴏᴍᴍᴀɴᴅs  Aʀᴇ  Eᴀsʏ  Aɴᴅ  Sɪᴍᴘʟᴇ 💖

➤  Eɴᴊᴏʏ  Wɪᴛʜ  Yᴏᴜʀ  Fʀɪᴇɴᴅs ✨..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("➕ Aᴅᴅ  Tᴏ  Yᴏᴜʀ  Gʀᴏᴜᴘ ➕", url=f"http://t.me/DolphinGameBot?startgroup=new")
                ],
                [
                    InlineKeyboardButton("📢  Uᴘᴅᴀᴛᴇs", url="https://t.me/+u-YFXF8x-Rw0M2Rl"),
                    InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ ⚠️", url="https://t.me/+u-YFXF8x-Rw0M2Rl"),
                ],
                [
                    InlineKeyboardButton("📚  Cᴏᴍᴍᴀɴᴅs  Aɴᴅ  Hᴇʟᴘ  📚", callback_data="bhelp"),   
                ],
             ]
         ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("bhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hɪ ! I'ᴍ [Dᴏʟᴘʜɪɴ 🐬](https://t.me/DolphinGameBot)  Bᴀsᴇᴅ Oɴ Gᴀᴍᴇ Bᴏᴛ 🇺🇸

I Hᴀᴠᴇ Tᴏᴛᴀʟʟʏ 2 Gᴀᴍᴇ Eɴᴊᴏʏ Wɪᴛʜ Yᴏᴜʀ Fʀɪᴇɴᴅs 🥳""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✍ Pᴀʀᴀᴘʜʀᴀsᴇ", callback_data="p_help"),
                    InlineKeyboardButton("Jᴜᴍʙʟᴇᴅ 🆎", callback_data="j_help"),
                ],
                [
                    InlineKeyboardButton("❮ Nᴇxᴛ", callback_data="p_help"),
                    InlineKeyboardButton("🔙 Gᴏ Bᴀᴄᴋ", callback_data="bstart"),  
                    InlineKeyboardButton("Nᴇxᴛ ❯", callback_data="j_help"),
                ],
             ]
         ),
         disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("p_help"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🐬  [ **Jᴜᴍʙʟᴇᴅ Wᴏʀᴅs Gᴀᴍᴇ Cᴍᴅ** ] 🇺🇸

/game_1  -  Sᴛᴀʀᴛ  Jᴜᴍʙʟᴇᴅ  Wᴏʀᴅs  Gᴀᴍᴇ

/stop  -  Tᴏ  Sᴛᴏᴘ  Jᴜᴍʙʟᴇᴅ  Wᴏʀᴅs  Gᴀᴍᴇ

/scores  -  Tᴏ  Sᴇᴇ  Yᴏᴜʀ  Pᴏɪɴᴛs

/rules  -  Tᴏ  Sᴇᴇ  Gᴀᴍᴇ  Rᴜʟᴇs""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Gᴏ Bᴀᴄᴋ", callback_data="bhelp")]]
        ),
    )

@Client.on_callback_query(filters.regex("j_help"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🐬  [ **Pᴀʀᴀᴘʜʀᴀsᴇ Wᴏʀᴅs Gᴀᴍᴇ Cᴍᴅ** ] 🇺🇸

/game_2  -  Sᴛᴀʀᴛ  Pᴀʀᴀᴘʜʀᴀsᴇ  Wᴏʀᴅs  Gᴀᴍᴇ

/pass  -  Tᴏ  Pᴀss  Cᴜʀʀᴇɴᴛ  Pᴀʀᴀᴘʜʀᴀsᴇ  Wᴏʀᴅ

/cancel  -  Tᴏ  Cᴀɴᴄᴇʟ  Pᴀʀᴀᴘʜʀᴀsᴇ  Wᴏʀᴅs  Gᴀᴍᴇ

/rules  -  Tᴏ  Sᴇᴇ  Gᴀᴍᴇ  Rᴜʟᴇs""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Gᴏ Bᴀᴄᴋ", callback_data="bhelp")]]
        ),
    )
