from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler

from helpers.game import get_game
from helpers.wrappers import nice_errors


@nice_errors
def callback(update, context, CallbackContext):
game = get_game(context)
    query = update.callback_query
    if game['host'].id == update.effective_user.id:
        query.message.edit_text(
            text=""" Hi..🤗 I'm *Lonely king*
                 \nMy source code is private  [support](t.me/thanimaisupport) .""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="I want to be the host", callback_data="host")
                 ]
                ]
            ),
        )



handler = CallbackQueryHandler(callback, pattern='another')
