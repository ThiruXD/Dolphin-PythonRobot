from telegram import Update
from Dolphin_bot import CallbackContext
from Dolphin_bot import CallbackQueryHandler

from helpers.game import get_game
from helpers.game import next_word
from helpers.wrappers import nice_errors


@nice_errors
def callback(update: Update, context: CallbackContext):
    game = get_game(context)

    if game['host'].id == update.effective_user.id:
        word = next_word(context)
        update.callback_query.answer(word, show_alert=True)
    else:
        update.callback_query.answer('This is not for you.', True)


handler = CallbackQueryHandler(callback, pattern='next')
