

from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, Message

from telegram.ext import get_string
from telegram.ext import CallbackQueryHandler
from telegram.ext import app
from telegram.ext.mongo import get_lang, set_lang
from telegram.ext.mongo import (ActualAdminCB, language,
                                         languageCB)

# Languages Available


def lanuages_keyboard(_):
    keyboard = InlineKeyboard(row_width=2)
    keyboard.row(
        InlineKeyboardButton(
            text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English",
            callback_data=f"languages:en",
        ),
        InlineKeyboardButton(
            text="🇮🇳 Tamil",
            callback_data=f"languages:ta",
        ),
    )
    return keyboard


handler = CallbackQueryHandler(callback, pattern='yukki_lang')


@app.on_message(
    filters.command(yukki_lang)
    & filters.group
    & ~filters.edited
)

@ActualAdminCB
async def language_markup(client, CallbackQuery, _):
    langauge = (CallbackQuery.data).split(":")[1]
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer(
            "You're already on same language", show_alert=True
        )
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer(
            "Successfully changed your language.", show_alert=True
        )
    except:
        return await CallbackQuery.answer(
            "Failed to change language or Language under update.",
            show_alert=True,
        )
    await set_lang(CallbackQuery.message.chat.id, langauge)
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=keyboard
    )
