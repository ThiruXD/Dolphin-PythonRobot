from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from Dolphin_bot import CallbackContext
from Dolphin_bot import Filters
from Dolphin_bot import MessageHandler

import mongo.users as db
from helpers.game import get_game
from helpers.game import is_true

     update.effective_message.reply_text(
        f'{update.effective_user.mention_html()} talks about a word.',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        'English',
                        callback_data='view',
                    ),
                ],
                [
                    InlineKeyboardButton(
                        'Next',
                        callback_data='Tamil',
                    ),
                ],
            ],
        ),
    )

   handler = CallbackQueryHandler(callback, pattern='settings')
