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
""" =======================CHRISTMAS====================== """
xmas1 = "https://telegra.ph/file/e93bddf11579a952fb3e9.jpg"
xmas2 = "https://telegra.ph/file/68cb54e5f8a85b2027094.jpg"
xmas3 = "https://telegra.ph/file/18adf069643f60037c4b8.jpg"
xmas4 = "https://telegra.ph/file/808b5ae57cd50ecac0941.jpg"
xmas5 = "https://telegra.ph/file/30265f2301037244fb1bc.jpg"
""" =======================CHRISTMAS====================== """

@register(pattern=("/xmas"))
async def hmm(event):
    chat = await event.get_chat()
    await event.delete()
    pm_caption = f"**Happy Christmas From {(event.sender.first_name)} **\n\n"
    pm_caption += "**By Aasf**\n\n"
    on = await borg.send_file(event.chat_id, file=xmas1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(event.chat_id, on, file=xmas2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(event.chat_id, ok, file=xmas3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(event.chat_id, ok2, file=xmas4)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(event.chat_id, ok3, file=xmas1)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(event.chat_id, ok4, file=xmas2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(event.chat_id, ok5, file=xmas3)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(event.chat_id, ok6, file=xmas4)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(event.chat_id, ok7, file=xmas5)
    
