# If You Kanged This Module Plz Give Credits It Was Made By @AASFCYBERKING
# I Really Hardworked For This Module
import asyncio
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from SerenaRobot.events import register
from SerenaRobot import telethn as borg
from SerenaRobot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins

edit_time = 5
""" =======================DIWALI====================== """
diwali1 = "https://telegra.ph/file/2fac8d8519f73aec8fda8.jpg"
diwali2 = "https://telegra.ph/file/a4f0842dc0fcb2b391679.jpg"
diwali3 = "https://telegra.ph/file/a8449329aebf8e430111c.jpg"
diwali4 = "https://telegra.ph/file/6aec7a7f258df61f8ffc4.jpg"
diwali5 = "https://telegra.ph/file/c0c9dcf95a51fc5c0ccf5.jpg"
""" =======================DIWALI====================== """

@register(pattern=("/diwali"))
async def hmm(event):
    chat = await event.get_chat()
    await event.delete()
    pm_caption = f"**Happy Diwali From {(event.sender.first_name)} **\n\n"
    pm_caption += "**By Pigasus X Team**\n\n"
    on = await borg.send_file(event.chat_id, file=diwali1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(event.chat_id, on, file=diwali2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(event.chat_id, ok, file=diwali3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(event.chat_id, ok2, file=diwali4)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(event.chat_id, ok3, file=diwali1)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(event.chat_id, ok4, file=diwali2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(event.chat_id, ok5, file=diwali3)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(event.chat_id, ok6, file=diwali4)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(event.chat_id, ok7, file=diwali5)

__mod_name__ = "FESTIVAL🎆"

__help__ = """
 ~ /diwali *:* Tell Happy Diwali To Your Friends. 
 ~ /xmas *:* Tell Merry Christmas To Your Friends.
"""
    
