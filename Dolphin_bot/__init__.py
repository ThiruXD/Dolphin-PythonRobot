import os
from time import sleep
from pyrogram import Client
import telegram.ext as tg
import logging
from dotenv import load_dotenv, set_key, unset_key
from os import getenv

load_dotenv('config.env')

# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


# Hesap
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
TOKEN = getenv("TOKEN")
USERNAME = getenv("USERNAME")
OWNER_ID = getenv("OWNER_ID", "")
MONGO_URI = getenv('MONGO_URI')
WORKERS = int(os.environ.get('WORKERS', 8))
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split()))

if OWNER_ID and len(OWNER_ID) and OWNER_ID.isdigit():
    OWNER_ID = int(OWNER_ID)  # type: ignore
else:
    OWNER_ID = None  # type: ignore

# BOT CLIENTİ
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="Dolphin_bot/plugins/"),
    workers=16
)

updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)

telethn = TelegramClient("Dolphin", API_ID, API_HASH)

pbot = Client("Dolphingamebot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

# Oyun Verileri
oyun = {}  # type: ignore


# rating
rating = {}  # type: ignore
