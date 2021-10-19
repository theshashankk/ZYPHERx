impore re
from pyrogram import Client, errors
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from youtubesearchpython import VideosSearch

@Client.on_message(filters.command(["info"]))
async def lolinfo(_, message: Message):
  song_p = message.text.split('_', 1)
  query = song_p[1]
  regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
  match = re.match(regex,query)
  search = VideosSearch(query, limit=70)
  
  for result in search.result()["result"]:
    title=result["title"]
    description="{}, {} views.".format(
      result["duration"], result["viewCount"]["short"]
    )
    input_message_content=InputTextMessageContent(
      "🔗 https://www.youtube.com/watch?v={}".format(result["id"])
    )
    thumb_url=result["thumbnails"][0]["url"]
    await message.reply_text(f'''
🧾 __Here Is the info about song__.

**name**: {title}
**Description**: {description}
**Youtube Link**: {thumb_url}'''
    )
