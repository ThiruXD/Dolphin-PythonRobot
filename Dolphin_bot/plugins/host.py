from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from Dolphin_bot import CallbackContext
from Dolphin_bot import CallbackQueryHandler

import mongo.chats as db
from helpers.game import new_game
from helpers.wrappers import nice_errors


@nice_errors
def callback(update: Update, context: CallbackContext):
    new_game(update.effective_user, context)

    update.effective_message.reply_text(
        f'{update.effective_user.mention_html()} talks about a word.',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        'View',
                        callback_data='view',
                    ),
                ],
                [
                    InlineKeyboardButton(
                        'Next',
                        callback_data='next',
                    ),
                ],
                [
                    InlineKeyboardButton(
                        'I Change My Mind',
                        callback_data='button_stop',
                    ),
                ],
            ],
        ),
    )

    db.update(update.effective_chat.id, update.effective_chat.title)
    update.callback_query.answer()


handler = CallbackQueryHandler(callback, pattern='host')
