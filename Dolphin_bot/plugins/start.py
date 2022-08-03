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
**🔮 {} 🔮  Hᴇʟʟᴏ,  Wᴇʟᴄᴏᴍᴇ  Tᴏ  Dᴏʟᴘʜɪɴ  Gᴀᴍᴇ  Bᴏᴛ,  Yᴏᴜ  Cᴀɴ  Pʟᴀʏ  Wᴏʀᴅ  Dᴇʀɪᴠᴀᴛɪᴏɴ  Gᴀᴍᴇ  Oʀ  Wᴏʀᴅ  Nᴀʀʀᴀᴛɪᴏɴ  Wɪᴛʜ  Tʜɪs  Bᴏᴛ ✨.

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
✨ **Hɪ ! I'ᴍ [Dᴏʟᴘʜɪɴ 🐬](https://t.me/DolphinGameBot)  Bᴀsᴇᴅ Oɴ Gᴀᴍᴇ Bᴏᴛ 🇺🇸

I Hᴀᴠᴇ Tᴏᴛᴀʟʟʏ 2 Gᴀᴍᴇ Eɴᴊᴏʏ Wɪᴛʜ Yᴏᴜʀ Fʀɪᴇɴᴅs 🥳
"""
help_buttons = [
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

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(_, m):
             await m.reply_photo(
               photo=random.choice(HMF_IMG),
                caption=PM_START_TEXT.format(m.from_user.mention),                   
                reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_message(filters.command("help"))
async def help(_, m):
             await m.reply_photo(
               photo=random.choice(HMF_IMG),
                caption=HELP.format(m.from_user.mention),                   
                reply_markup=InlineKeyboardMarkup(help_buttons))


 
@Client.on_callback_query(filters.regex("bstart"))
async def bstart(_, query: CallbackQuery):
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
async def bhelp(_, query: CallbackQuery):
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
async def phelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🐬  [ **Jᴜᴍʙʟᴇᴅ Wᴏʀᴅs Gᴀᴍᴇ Cᴍᴅ** ] 🇺🇸

/game_1  -  Sᴛᴀʀᴛ  Jᴜᴍʙʟᴇᴅ  Wᴏʀᴅs  Gᴀᴍᴇ

/stop  -  Tᴏ  Sᴛᴏᴘ  Jᴜᴍʙʟᴇᴅ  Wᴏʀᴅs  Gᴀᴍᴇ

/scores  -  Tᴏ  Sᴇᴇ  Yᴏᴜʀ  Pᴏɪɴᴛs

/rules  -  Tᴏ  Sᴇᴇ  Gᴀᴍᴇ  Rᴜʟᴇs""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Gᴏ Bᴀᴄᴋ", callback_data="bhelp"),
              InlineKeyboardButton("Nᴇxᴛ ❯", callback_data="j_help")]]
        ),
    )

@Client.on_callback_query(filters.regex("j_help"))
async def jhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🐬  [ **Pᴀʀᴀᴘʜʀᴀsᴇ Wᴏʀᴅs Gᴀᴍᴇ Cᴍᴅ** ] 🇺🇸

/game_2  -  Sᴛᴀʀᴛ  Pᴀʀᴀᴘʜʀᴀsᴇ  Wᴏʀᴅs  Gᴀᴍᴇ

/pass  -  Tᴏ  Pᴀss  Cᴜʀʀᴇɴᴛ  Pᴀʀᴀᴘʜʀᴀsᴇ  Wᴏʀᴅ

/cancel  -  Tᴏ  Cᴀɴᴄᴇʟ  Pᴀʀᴀᴘʜʀᴀsᴇ  Wᴏʀᴅs  Gᴀᴍᴇ

/rules  -  Tᴏ  Sᴇᴇ  Gᴀᴍᴇ  Rᴜʟᴇs""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("❮ Nᴇxᴛ", callback_data="p_help"),
              InlineKeyboardButton("🔙 Gᴏ Bᴀᴄᴋ", callback_data="bhelp")]]
        ),
    )
