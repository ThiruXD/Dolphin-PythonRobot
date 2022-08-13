from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler

from helpers.game import end_game
from helpers.game import get_game
from helpers.wrappers import nice_errors
from helpers.wrappers import admin_only


def callback(update: Update, context: CallbackContext):
       end_game(context)
       game = get_game(context)
       if not game['host'].id == update.effective_user.id:
              update.callback_query.answer('Leader Only can Refused   !  😑', True)    
              return                      
       else:
            update.effective_message.reply_text(
            f'{update.effective_user.mention_html()} Rᴇғᴜsᴇᴅ  Tᴏ  Lᴇᴀᴅ ! 🥺✨',
            reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton('I  Wᴀɴᴛ  Tᴏ  Bᴇ  A  Lᴇᴀᴅᴇʀ  🦁', callback_data='host')]]))
            return

          
    

                    

handler = CallbackQueryHandler(callback, pattern='button_stop')
