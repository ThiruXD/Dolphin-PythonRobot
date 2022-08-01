from telegram import Update
from telegram.ext import CommandHandler

from helpers.wrappers import nice_errors
from mongo import users


@nice_errors
def callback(update: Update, _):
    total_scores = users.total_scores(update.effective_user.id)
    scores_in_chat = users.scores_in_chat(
        update.effective_chat.id,
        update.effective_user.id,
    ) if (
        update.effective_chat.type == 'supergroup'
    ) else '<code>Nᴏᴛ  Iɴ  Gʀᴏᴜᴘ</code>'

    update.effective_message.reply_text(
        f'Yᴏᴜʀ  Tᴏᴛᴀʟ  Sᴄᴏʀᴇs: {total_scores}\nYᴏᴜʀ  Sᴄᴏʀᴇs  Iɴ  Tʜɪs  Cʜᴀᴛ: {scores_in_chat}',
    )


handler = CommandHandler('scores', callback)
