from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler

import mongo.users as db
from helpers.game import get_game
from helpers.game import is_true


def callback(update: Update, context: CallbackContext):
    try:
        game = get_game(context)

        if game['host'].id != update.effective_user.id:
            if is_true(update.effective_message.text, context):
                update.effective_message.reply_text(
                    f"{update.effective_user.mention_html()} **Gᴜᴇssᴇᴅ  Tʜᴇ  Cᴏʀʀᴇᴄᴛ  Wᴏʀᴅ**  ✨, {game['word']}.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    'I  Wᴀɴᴛ  Tᴏ  Bᴇ  A  Lᴇᴀᴅᴇʀ 🦁',
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


handler = MessageHandler(
    Filters.text & ~Filters.command & Filters.chat_type.supergroup,
    callback,
)

