from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.command("rules"))
async def rules(c:Client, m:Message):
    await query.edit_message_text(
        f""" 🐬  **Dᴏʟᴘʜɪɴ  Gᴀᴍᴇ  Rᴜʟᴇs**  📖

🌷  Tʜᴇ  ᴘᴇʀsᴏɴ  ᴡʜᴏ  ᴡʀɪᴛᴇs  ᴛʜᴇ  ɴᴀᴍᴇ  ᴏɴ  ᴛʜᴇ  ʙᴏᴛ  ɪs  ᴛʜᴇ  ᴘᴇʀsᴏɴ  ᴡʜᴏ  ᴏғғᴇʀs  ᴛʜᴇ  ᴡᴏʀᴅ.  

🌷  Yᴏᴜ  ᴄᴀɴ  ᴀᴅᴅ  ᴛʜᴇ  ᴡᴏʀᴅ  ʏᴏᴜ  ᴡᴀɴᴛ  ᴡɪᴛʜ  ᴛʜᴇ  ᴡʀɪᴛᴇ  ᴀ  ᴡᴏʀᴅ  ʙᴜᴛᴛᴏɴ  ᴀɴᴅ  ʏᴏᴜ  ᴄᴀɴ  ᴜsᴇ  ᴛʜᴇ  ᴇxᴀᴍɪɴᴇ  ʙᴜᴛᴛᴏɴ  ᴛᴏ  ʟᴏᴏᴋ  ᴀᴛ  ʏᴏᴜʀ  ᴡᴏʀᴅ.

🌷  Tʜᴇ  ᴘᴇʀsᴏɴ  ᴡʜᴏ  ᴋɴᴏᴡs  ᴛʜᴇ  ᴡᴏʀᴅ  ʜᴀs  8  ᴍɪɴᴜᴛᴇs  ᴛᴏ  ᴇxᴘʟᴀɪɴ.  ᴛʜᴇ  ᴡᴏʀᴅ  ᴛʜᴀᴛ  ɪs  ɴᴏᴛ  ᴇxᴘʟᴀɪɴ  ᴡɪᴛʜɪɴ  ᴛʜɪs  ᴘᴇʀɪᴏᴅ  ɪs  ᴄᴀɴᴄᴇʟᴇᴅ  ᴀɴᴅ  ᴛʜᴇ  ʀɪɢʜᴛ  ᴏғ  ᴀ  ɴᴇᴡ  ɴᴀʀʀᴀᴛᴏʀ  ᴄᴏᴍᴇs  ᴏᴜᴛ.

🌷  Tᴏ  ᴀᴅᴅ  ʏᴏᴜʀ  ᴏᴡɴ  ᴡᴏʀᴅ,  ʏᴏᴜ  ᴍᴜsᴛ  ᴇɴᴛᴇʀ  ᴛʜᴇ  ʙᴏᴛs  ᴘʀᴏғɪʟᴇ  ᴀɴᴅ  sᴇɴᴅ  ᴛʜᴇ  ʙᴏᴛ  ᴀ  ᴏɴᴇ-ᴛɪᴍᴇ  ғɪʀsᴛ  ᴍᴇssᴀɢᴇ.  ᴛʜᴇɴ,  ᴡʜᴇɴ  ʏᴏᴜ  ᴄʟɪᴄᴋ  ᴏɴ  ᴡʀɪᴛᴇ  ᴀ  ᴡᴏʀᴅ  ʙᴜᴛᴛᴏɴ,  ʏᴏᴜ  ᴄᴀɴ  ᴀᴅᴅ  ʏᴏᴜʀ  ᴏᴡɴ  ᴡᴏʀᴅ  ʙʏ  ʀᴇᴘʟʏɪɴɢ  ᴛᴏ  ᴛʜᴇ  ᴍᴇssᴀɢᴇ  ᴛʜᴀᴛ  ᴛʜᴇ  ʙᴏᴛ  sᴇɴᴛ  ʏᴏᴜ.

🌷  Yᴏᴜ  ᴄᴀɴ  ᴏʀɢᴀɴɪᴢᴇ  ᴄᴏᴍᴘᴇᴛɪᴛɪᴏɴs  ᴡɪᴛʜ  ᴡᴇᴇᴋʟʏ  sᴄᴏʀᴇs  ᴀɴᴅ  ɢʟᴏʙᴀʟ  ᴡᴇᴇᴋʟʏ  sᴄᴏʀᴇs  ᴡɪᴛʜɪɴ  ᴛʜᴇ  ɢʀᴏᴜᴘ.""")

