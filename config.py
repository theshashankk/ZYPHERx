import os
from os import getenv

from dotenv import load_dotenv

from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAXycVEHNyZQZmQYSJCWhv2Up4MB9rNWfEZN-9BWvqEaZlZlo-FsW4zVbtAiR_wqtppgBgTVeBQ1ZCW3inHzPK9a8hTnpdUh_AhpYh_VucvxnOuKycbDCNjjDksSXimhG39fsIjUyhuqVqS-PvOeEmHSk267gLQ3MVe6IMGk_7w6rQihFj0Ct1qVdSARpaPwwvSo18S06rxiPlXJsXpLNOs8k5AzfDyWB6mgSUCPzuBldMAK0yfGYm1q62IWJkoX8Cyt2nznNlBN1GZa3CSc0GA5BqEzQE6OJWPxgQWu5jTcNYY1Iqgxw-5aztlfQVZONhH7f9H7lvbIyawFiJDby-tdquPPgA")
BOT_TOKEN = getenv("BOT_TOKEN", "1988131788:AAHds6rsEEAYLJt6TlS5Kic74KHSmgKunBo")
BOT_NAME = getenv("BOT_NAME", "ZYPHERx_BOT")
BG_IMAGE = getenv("BG_IMAGE", "https://raw.githubusercontent.com/theshashankk/HinataBot/main/background1.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/976bb4ee2f66857cfa317.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/5dd2446cfe99c08a7490a.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/e3c0c7e817f95448473a1.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "ZYPHERx_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "zypher_assist")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ZYPHERXSUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZYPHERxSUPPORT")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "andreobee_xD")
# fill with DISABLE if you want to disable pm-permit
PMPERMIT = getenv("PMPERMIT", "ENABLE")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/Team-Zypher/ZYPHERx"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
