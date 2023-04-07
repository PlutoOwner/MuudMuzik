from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph//file/36a15fa7b75b0f424bda6.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph//file/189fe27bff1207dd3eb85.jpg")
BOT_NAME = getenv("BOT_NAME", "gє¢є кυѕ̧υ")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME") 
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "sohbeti_muhabbet")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "vorovskayamusic") 
OWNER_NAME = getenv("OWNER_NAME", "emily_team")
ALIVE_NAME = getenv("ALIVE_NAME", "Emily Music")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
