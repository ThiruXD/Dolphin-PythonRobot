from telegram import Update
from datetime import datetime
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler

from helpers.game import get_game
from helpers.game import next_word
from helpers.wrappers import nice_errors

CHOOSING_PLAYER = range(2)

def stop(update, context):
    """
    Stops the current game
    """
    if 'is_playing' in context.chat_data and context.chat_data["host"]:
        # Emptying all the temporary chat variables
        context.chat_data['view'] = None
        context.chat_data['next'] = None
        context.chat_data["host"] = False
        update.message.reply_text("Я зупинив гру")

        # Changing the state to CHOOSING_PLAYER
        return CHOOSING_PLAYER

    else:
        update.message.reply_text("Немає гри, яку я можу зупинити")


  handler = CallbackQueryHandler(callback, pattern='stop')

states={
            CHOOSING_PLAYER: [CallbackQueryHandler(next_word, pattern="next_word"),
                              CommandHandler('stop', stop)],

        }

                            


