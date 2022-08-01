from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

from helpers.game import end_game
from helpers.wrappers import nice_errors


@nice_errors
def callback(update: Update, context: CallbackContext):
    try:
        end_game(context)
        update.effective_message.reply_text(
            f'{update.effective_user.mention_html()} **Tʜᴇ  Gᴀᴍᴇ  Is  Sᴛᴏᴘᴘᴇᴅ.🔴 /Start@DolphinGameBot,  Yᴏᴜ  Cᴀɴ  Sᴛᴀʀᴛ  A  Nᴇᴡ  Gᴀᴍᴇ  Bʏ  Pʀᴇssɪɴɢ  Tʜᴇ  Bᴜᴛᴛᴏɴ**.',
        )
    except Exception as e:
        update.effective_message.reply_text(f'Error: {e}')


handler = CommandHandler('stop', callback)
