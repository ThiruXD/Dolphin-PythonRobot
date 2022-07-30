from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from Dolphin_bot import CallbackContext
from Dolphin_bot import CallbackQueryHandler
from Dolphin_bot import CommandHandler
from Dolphin_bot import Filters

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
        parse_mode=ParseMode.MARKDOWN,
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


  handler = CallbackQueryHandler(callback, pattern='game')
