
import asyncio
import os
import re

from pyrogram import Client, filters
from pyrogram.types import (
    InputMediaPhoto,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)

bot = Client(
    "Bot",
    api_id = 14706934,
 api_hash = "fc81a74886bae0a8499886ff4561be65",
 bot_token = "5448584711:AAEDCP1Glg7fjIhBWnaROKsKBWQHY-nJWGw"
)


@bot.on_message(filters.command("post") & filters.group)
async def start(client, message):
    from pyrogram.enums import ChatMemberStatus
    state = (await client.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)).status
    if state == ChatMemberStatus.OWNER:
        bots = []
        async for m in bot.get_chat_members(message.chat.id):
            bots.append(m.user.id)
        for b in bots:
            import random,time
            username = (await client.get_chat(b)).username
            l = ["فايت للكروب وماتتفاعل ؟ ","تعال اعزمك  ع موطه ","تحبني لولا؟","ممكن نتعرف ؟","ناس تريدك تعالل !","شلونك؟","هلو","ها","تعال محتاجك " ,"مشتاقلك ","شلونك","ممكن بوسه","هلو"]
            r = random.choice(l)
            await bot.send_message(message.chat.id,f"{r} @{username}")
            await asyncio.sleep(210)
        start(client,message)

bot.run()
