from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update

from helpers.game import get_game
from helpers.wrappers import nice_errors
import mongo.chats as db
from telegram.ext import get_lang, set_lang
from telegram.ext import (ActualAdminCB, language,
                                         languageCB)


@nice_errors
def callback(update: Update, context: CallbackContext):
    game = get_game(context)
    query = update.callback_query
    if game['host'].id == update.effective_user.id:
        query.message.edit_text(
            text=f"""Choose Your Language .""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="English", callback_data=f"languages:en")
                 ],
                 [
                    InlineKeyboardButton(text="Tamil", callback_data=f"languages:ta",)
                 ]
                ]
            ),
        )



handler = CallbackQueryHandler(callback, pattern='another')
