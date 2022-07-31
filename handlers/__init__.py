from telegram.ext import Dispatcher

from . import stop
from . import button_stop
from . import host
from . import message
from . import paraphrase
from . import jumbled_word
from . import next
from . import scores
from . import another
from . import view


def add_handlers(dp: Dispatcher):
    dp.add_handler(stop.handler)
    dp.add_handler(button_stop.handler)
    dp.add_handler(host.handler)
    dp.add_handler(message.handler)
    dp.add_handler(jumbled_word.handler)
    dp.add_handler(paraphrase.handler)
    dp.add_handler(next.handler)
    dp.add_handler(scores.handler)
    dp.add_handler(another.handler)
    dp.add_handler(view.handler)


