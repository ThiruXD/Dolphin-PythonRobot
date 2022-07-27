from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler

from helpers.game import get_game
from helpers.wrappers import nice_errors


@nice_errors
def callback(update: Update, context: CallbackContext):
    game = get_game(context)

    if game['host'].id == update.effective_user.id:
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

     db.update(update.effective_chat.id, update.effective_chat.title)



handler = CommandHandler('another', callback, Filters.chat_type.groups)
