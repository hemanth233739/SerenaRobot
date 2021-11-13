from telethon.tl.types import *
from SerenaRobot.events import register

@register(pattern="^/owo ?(.*)")
async def stats(e): 
   await e.edit("`Please wait...`") 
   msg = str((await e.client.get_messages(e.chat_id, limit=0)).total) 
   img = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterPhotos())).total) 
   vid = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterVideo())).total) 
   msc = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterMusic())).total) 
   ses = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterVoice())).total) 
   rvid = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterRoundVideo())).total) 
   doc = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterDocument())).total) 
   url = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterUrl())).total) 
   gif = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterGif())).total) 
   geo = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterGeo())).total) 
   stat = f"✉️ **Messages:** `{msg}`\n🖼️ **Photos:** `{img}`\n📹 **Videos:** `{vid}`\n🎵 **Music:** `{msc}`\n🎤 **Voice Messages:** `{ses}`\n🎥 **Videos:** `{rvid}`\n📂 **Folders:** `{doc}`\n🔗 **Links:** `{url}`\n🎞️ **GIFs:** `{gif}`\n🗺 *locations*:** `{geo}`"
   await e.edit(stat)
