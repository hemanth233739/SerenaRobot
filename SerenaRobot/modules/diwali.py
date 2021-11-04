# If You Kanged This Module Plz Give Credits It Was Made By @AASFCYBERKING
# I Really Hardworked For This Module
import asyncio
import os
import requests
import datetime
import html
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from Sophia.events import register
from Sophia import telethn as borg
from Sophia import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins
from telegram.utils.helpers import escape_markdown, mention_html

edit_time = 5
""" =======================CONSTANTS====================== """
diwali1 = "https://telegra.ph/file/cf73748c573be66cb2b56.jpg"
diwali2 = "https://telegra.ph/file/a1c250048ef1fe7a3921c.jpg"
diwali3 = "https://telegra.ph/file/4ee14dca0bb7270d2e9a6.jpg"
diwali4 = "https://telegra.ph/file/359c8e1592cd643574f3b.jpg"
""" =======================CONSTANTS====================== """

@register(pattern=("/diwali"))
async def hmm(yes, context: CallbackContext):
    bot, args = context.bot, context.args
    chat = await yes.get_chat()
    await yes.delete()
    user = bot.get_chat(user_id)
    user_id = extract_user(msg, args)
    pm_caption = "** Happy Diwali From {html.escape(user.first_name)} **\n\n"
    pm_caption += "**By Pigasus X Team**\n\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=diwali2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=diwali3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=diwali1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=diwali3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=diwali2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=diwali1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=diwali4)

__mod_name__ = "ALIVE💖"

__help__ = """
 ~ /alive *:* Get A Alive Message Like Userbot. 
Credits @AASFCYBERKING
"""
