
from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler

import mongo.users as db
from helpers.game import end_game
from helpers.wrappers import nice_errors


@nice_errors
def callback(update: Update, context: CallbackContext):
    try:
        game = end_game(context)
          if game['host'].id != update.effective_user.id:
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
        update.callback_query.answer('Hᴏsᴛᴇʀ  Oɴʟʏ  Cᴀɴ  Sᴇᴇ  Tʜᴇ  Wᴏʀᴅ  !  😑', True)

     db.update(
                    update.effective_chat.id,
                    update.effective_user.id,
                    update.effective_user.first_name,
                    update.effective_user.username,
                )
    except:
        pass

handler = CallbackQueryHandler(callback, pattern='button_stop')
