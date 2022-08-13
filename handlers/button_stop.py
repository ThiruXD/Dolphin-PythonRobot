
from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler

from helpers.game import end_game
from helpers.wrappers import nice_errors


@nice_errors
def callback(update: Update, context: CallbackContext):
    try:
        end_game(context)
        update.effective_message.reply_text(
            f'{update.effective_user.mention_html()} Rᴇғᴜsᴇᴅ  Tᴏ  Lᴇᴀᴅ ! 🥺✨',
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    'I  Wᴀɴᴛ  Tᴏ  Bᴇ  A  Lᴇᴀᴅᴇʀ  🦁',
                                    callback_data='host',
                                ),
                            ],
                        ],
                    ),
                )
      else:
        update.callback_query.answer('Hᴏsᴛᴇʀ  Oɴʟʏ  Cᴀɴ  Sᴇᴇ  Tʜᴇ  Wᴏʀᴅ  !  😑')


handler = CallbackQueryHandler(callback, pattern='button_stop')
