from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.private & filters.incoming & filters.command(["start"]))
async def startvro(message):
  kk = '''
  __Hey this is Zypher__
**🍿 i can play music in your group/channel voice that with out any type of lag..**

**U can use these buttons to know more about me..**
**if you want to add me in your group click on below button.🍿**'''
  await message.reply_sticker('CAACAgUAAxkBAAEMJNthZnwtCOE9AAE4bMZW-xc03wbAy_EAAgkDAALXoDBVy5Gfi4ANJREhBA')
  await message.reply_text(
    kk,
    reply_markup=InlineKeyboardMarkup(
            [[
               InlineKeyboardButton("🍿 Advanced", callback_data='amdvamced')
            ],
            [
               InlineKeyboardButton("💨 Support Group", url="https://t.me/ZYPHERxSUPPORT"),
               InlineKeyboardButton("💨 Updates Channel", url="https://t.me/ZYPHERxUPDATES")
            ],
            [
               InlineKeyboardButton("🙋 Add me to your group", url="t.me/ZYPHERx_BOT?startgroup=true")
           ]]
        ),
        reply_to_message_id=message.message_id,
    )
