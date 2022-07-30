from telegram import Update
from Dolphin_bot import CallbackContext
from Dolphin_bot import CommandHandler

from helpers.game import end_game
from helpers.wrappers import admin_only


@admin_only
def callback(update: Update, context: CallbackContext):
    try:
        end_game(context)
        update.effective_message.reply_text(
            f'{update.effective_user.mention_html()} The Game Is Stopped.🔴 /Start@DolphinGameBot, You Can Start a New Game By Pressing The Button.',
        )
    except Exception as e:
        update.effective_message.reply_text(f'Error: {e}')


handler = CommandHandler('stop', callback)
