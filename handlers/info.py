'''
from __future__ import unicode_literals

import asyncio
import math
import os
import time
from random import randint
from urllib.parse import urlparse

import aiofiles
import aiohttp
import requests
import wget
import youtube_dl
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from config import BOT_USERNAME as bn
from helpers.decorators import humanbytes
from helpers.filters import command

@Client.on_message(command(['info', f'info@{BOT_USERNAME}']) & ~filters.edited)
async def infoo(message):
  query = " ".join(message.command[1:])
  m = message.reply("🔎 finding song...")
  ydl_ops = {"format": "bestaudio[ext=m4a]"}
  try:
    results = YoutubeSearch(query, max_results=1).to_dict()
    link = f"https://youtube.com{results[0]['url_suffix']}"
    title = results[0]["title"][:40]
    thumbnail = results[0]["thumbnails"][0]
    thumb_name = f"thumb-{title}.jpg"
    thumb = requests.get(thumbnail, allow_redirects=True)
    open(thumb_name, "wb").write(thumb.content)
    duration = results[0]["duration"]
    
    message.edit("📥 downloading...")'''
    
