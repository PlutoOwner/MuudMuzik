from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph//file/36a15fa7b75b0f424bda6.jpg")
START_IMAGE = getenv("START_IMAGE", "https://telegra.ph//file/189fe27bff1207dd3eb85.jpg")
BOT_NAME = getenv("BOT_NAME", "🎧 Muud Müzik")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME") 
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "PlutoFederation")
PLAYLIST_NAME = getenv("PLAYLIST_NAME", "PlutoFm") 
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
