from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler

import mongo.users as db
from helpers.game import get_game
from helpers.game import is_true
from helpers.wrappers import nice_errors


    def stop_and_restart(chat, msg):
        updater.stop()
            f'{chat}_{msg}',
        )

    def stop(update, context):
        update.effective_message.reply_text('Stoping...')
            target=stop_and_restart, args=(
                update.effective_chat.id,
                update.effective_message.message_id,
            ),
        ).start()

    dp.add_handler(CommandHandler('stop', stop))
    add_handlers(dp)

   

