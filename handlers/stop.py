from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler

from helpers.game import get_game
from helpers.game import next_word
from helpers.wrappers import nice_errors

def stop(update, context):
    """
    Stops the current game
    """
    if 'is_playing' in context.chat_data and context.chat_data["is_playing"]:
        # Emptying all the temporary chat variables
        context.chat_data['current_player'] = None
        context.chat_data['current_word'] = None
        context.chat_data["is_playing"] = False
        update.message.reply_text("Я зупинив гру")

        # Changing the state to CHOOSING_PLAYER
        return CHOOSING_PLAYER

    else:
        update.message.reply_text("Немає гри, яку я можу зупинити")


     CHOOSING_PLAYER: [CallbackQueryHandler(next_player, pattern="next_word"),
                              CommandHandler('stop', stop)],


