from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler

from helpers.game import get_game
from helpers.wrappers import nice_errors


@nice_errors
def callback(update: Update, context: CallbackContext):
    game = get_game(context)

    if game['host'].id == update.effective_user.id:
    if is_true(update.effective_message.text, context):
                update.effective_message.reply_text(
                    f"{update.effective_user.mention_html()} I Changed.",
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


handler = CallbackQueryHandler(callback, pattern='another')
