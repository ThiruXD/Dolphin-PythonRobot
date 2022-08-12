from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler

from helpers.game import end_game
from helpers.wrappers import nice_errors
from helpers.wrappers import hoster_only
from helpers.game import is_true

@nice_errors
def callback(update: Update, context: CallbackContext):
    try:
        game = end_game(context)

      if game['host'].id != update.effective_user.id:
            update.callback_query.answer("Okay", True)
      else:
        update.callback_query.answer('Hᴏsᴛᴇʀ  Oɴʟʏ  Cᴀɴ  Sᴇᴇ  Tʜᴇ  Wᴏʀᴅ  !  😑', True)


handler = CallbackQueryHandler(callback, pattern='button_stop')
