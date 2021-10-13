'''from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
      dkis
      __Hey this is Zypher__
      **🍿 i can play music in your group/channel voice that with out any type of lag..**
    
      **if you want to add me in your group click on below button.🍿**''',
     ''' reply_markup = InlineKeyboardMarkup(
        [
          [
            InlineKeyboardButton('🍿 Advanced', callback_data='amdvamced'),
          ],
          [
            InlineKeyboardButton('💨 Support group', url='t.me/ZYPHERxSUPPORT'),
            InlineKeyboardButton('💨 Updates channel', url='t.me/ZYPHERxUPDATES'),
          ],
          [
            InlineKeyboardButton(
              '🍿 Add me to your group', url='t.me/ZYPHERx_Bot? startgroup=true'
            )
          ],
        ]),
      disable_web_page_preview=True)
'''
