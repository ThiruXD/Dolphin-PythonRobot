from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from Dolphin_bot import pbot as bot
from Dolphin_bot import OWNER_ID

@bot.on_message(
    filters.private
    & filters.incoming
 )
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id == 1989750989:
        fwded_mesg = await message.forward(
            chat_id=OWNER_ID,
            disable_notification=True
        )
