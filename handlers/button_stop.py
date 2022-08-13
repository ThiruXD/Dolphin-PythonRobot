
from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler

from helpers.game import end_game
from helpers.wrappers import nice_errors
from helpers.wrappers import hoster_only


@nice_error
def callback(update: Update, context: CallbackContext):
    game = end_game(context)

    if game['host'].id == update.effective_user.id:
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
    except Exception as e:
        update.effective_message.reply_text(f'Aʟʀᴇᴀᴅʏ  Gᴀᴍᴇ  Gᴏɪɴɢ  Oɴ  Usᴇ  /stop Aɴᴅ  Sᴛᴀʀᴛ  Aɢᴀɪɴ 🧐')


handler = CallbackQueryHandler(callback, pattern='button_stop')
