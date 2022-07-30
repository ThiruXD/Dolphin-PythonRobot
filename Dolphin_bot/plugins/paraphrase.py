from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from Dolphin_bot import CallbackContext
from Dolphin_bot import CommandHandler
from Dolphin_bot import Filters
from Dolphin_bot import CallbackQueryHandler
import mongo.chats as db
from helpers.game import new_game
from helpers.game import end_game
from helpers.wrappers import nice_errors


@nice_errors
def callback(update: Update, context: CallbackContext):
    new_game(update.effective_user, context)
    db.update(update.effective_chat.id, update.effective_chat.title)
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
                        'I Changed My Mind',
                        callback_data='button_stop',
                    ),
                 ],
                 [
                    InlineKeyboardButton(
                        'language',
                        callback_data='yukki_lang',
                    ),
                ],
            ],
        ),
    )


handler = CallbackQueryHandler(callback, pattern='paraphrase')