from telegram.ext import Defaults
from telegram.ext import Updater

from config import BOT_TOKEN


updater = Updater(
    token=BOT_TOKEN,
    defaults=Defaults(
        parse_mode='HTML',
        disable_web_page_preview=True,
        quote=False,
        run_async=True,
    ),
)

dp = updater.dispatcher


if __name__ == '__main__':
    import os
    import sys
    from threading import Thread 
    from mongo import users
    
    from helpers.wrappers import nice_errors
    from telegram import Update
    from telegram.ext import CallbackContext, CommandHandler

    from handlers import add_handlers


    if '-stop' in sys.argv:
            msg = await message.reply_text("Restarting")

    def stop_and_restart(chat, msg):
        updater.stop()
        os.execl(
            sys.executable,
            sys.executable,
            *sys.argv,
            '-r',
            f'{chat}_{msg}',
        )

    def restart(update: Update, context: CallbackContext):
        update.effective_message.reply_text('Restarting...')
        Thread(
            target=stop_and_restart, args=(
                update.effective_chat.id,
                update.effective_message.message_id,
            ),
        ).start()

    dp.add_handler(CommandHandler('stop', restart))
    add_handlers(dp)

    updater.start_polling(drop_pending_updates=True)
    updater.idle()
