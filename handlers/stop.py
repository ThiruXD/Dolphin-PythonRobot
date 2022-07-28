    import os
    import sys
    from threading import Thread 
    from mongo import users

    from helpers.wrappers import nice_errors
    from telegram import Update
    from telegram.ext import CallbackContext, CommandHandler

    def stop_and_restart(chat, msg):
        updater.stop()
            f'{chat}_{msg}',
        )

    def stop(update, context):
        update.effective_message.reply_text('Stoping...')
        Thread(
            target=stop_and_restart, args=(
                update.effective_chat.id,
                update.effective_message.message_id,
            ),
        ).start()

    dp.add_handler(CommandHandler('stop', stop))
    add_handlers(dp)

    updater.start_polling(drop_pending_updates=True)
    updater.idle()
