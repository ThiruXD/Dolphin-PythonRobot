from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import Filters

import mongo.chats as db
from helpers.wrappers import nice_errors


@nice_errors
def callback(update: Update, context: CallbackContext):
    db.update(update.effective_chat.id, update.effective_chat.title)
    update.effective_message.reply_text(
        f'{update.effective_user.mention_html()} Choose Your Game.',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '✍  Wᴏʀᴅ  Pᴀʀᴀᴘʜʀᴀsᴇ',
                        callback_data='paraphrase',
                    ),
                ],
                [
                    InlineKeyboardButton(
                        'Jᴜᴍʙʟᴇᴅ  Lᴇᴛᴛᴇʀs 🆎',
                        callback_data='bgame',
                    ),
                ],
            ],
        ),
    )


  handler = CommandHandler('game', callback)
