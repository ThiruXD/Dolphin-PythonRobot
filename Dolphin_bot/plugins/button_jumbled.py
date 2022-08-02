from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import CallbackContext

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
    db.update(update.effective_chat.id, update.effective_chat.title)
    update.effective_message.reply_text(
        f"""{update.effective_user.mention_html()} 🎯 Rᴏᴜɴᴅ : {oyun[message.chat.id]['round']}/60 \n💵 Pᴏɪɴᴛs  Eᴀʀɴᴇᴅ : 1 \n📝 Wᴏʀᴅ :   <code>{kelime_list}</code> \n🎲 Cʟᴜᴇ : {oyun[message.chat.id]["kelime"][0]} \n✍🏻 Lᴀʀɢᴇ : {int(len(kelime_list)/2)} \n✏️ Fɪɴᴅ  Tʜᴇ  Cᴏʀʀᴇᴄᴛ  Wᴏʀᴅ  Fʀᴏᴍ  Tʜᴇ  Jᴜᴍʙʟᴇᴅ  Lᴇᴛᴛᴇʀs""",)
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '👀 Sᴇᴇ  Wᴏʀᴅ 👀',
                        callback_data='pass',
                    ),
                ],
            ],
        ),
    )

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


handler = CallbackQueryHandler(callback, pattern='paraphrase')
