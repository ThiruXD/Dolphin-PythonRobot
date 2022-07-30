from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler

from helpers.game import end_game
from helpers.wrappers import admin_only


@admin_only
def callback(update: Update, context: CallbackContext):
    try:
        end_game(context)
        update.effective_message.reply_text(
            f'{update.effective_user.mention_html()} refused to lead!.',
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    'I want to be the host',
                                    callback_data='host',
                                ),
                            ],
                        ],
                    ),
                )
    except Exception as e:
        update.effective_message.reply_text(f'Error: {e}')


handler = CallbackQueryHandler(callback, pattern='button_stop')
