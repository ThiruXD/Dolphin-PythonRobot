from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

from helpers.game import end_game
from helpers.wrappers import admin_only

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Filters
import mongo.chats as db
from helpers.game import new_game
from helpers.wrappers import nice_errors

     if game['host'].id != update.effective_user.id:
           if is_true(update.effective_message.text, context):
              def callback(update: Update, context: CallbackContext):
         try:
             end_game(context)
                update.effective_message.reply_text(
                    f"{update.effective_user.mention_html()} Host any one.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    'I want to be the host',
                                    callback_data='host',
                                ),
                            ],
                        ],
                    ),
                )

                db.update(
                    update.effective_chat.id,
                    update.effective_user.id,
                    update.effective_user.first_name,
                    update.effective_user.username,
                )
    except:
        pass

        handler = CallbackQueryHandler(callback, pattern='mind_changed')


