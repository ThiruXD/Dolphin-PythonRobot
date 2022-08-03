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
        f'{update.effective_user.mention_html()}  Is  Exᴘʟᴀɪɴɪɴɢ  Tʜᴇ  Wᴏʀᴅ  !  🍬',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '👀 Sᴇᴇ  Wᴏʀᴅ 👀',
                        callback_data='view',
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text='❮ Nᴇxᴛ Wᴏʀᴅ', callback_data='next'),
                    InlineKeyboardButton(
                        text='Nᴇxᴛ Wᴏʀᴅ ❯', callback_data='next'),
                ],
                [
                    InlineKeyboardButton(
                        '💀  I  Cʜᴀɴɢᴇᴅ  Mʏ  Mɪɴᴅ  💀',
                        callback_data='button_stop',
                    ),
                ],
            ],
        ),
    )


handler = CallbackQueryHandler(callback, pattern='paraphrase')

