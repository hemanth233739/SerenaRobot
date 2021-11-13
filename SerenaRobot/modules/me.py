from telethon.sync import events
import asyncio
from SerenaRobot.modules.sql import warns_sql as sql
from .. import telethn as bot
@bot.on(events.NewMessage(pattern="^/fk$"))
async def ok(e):
    if e.is_group:
        fuck = sql.get_warns(e.sender.id, e.chat.id)
        y= await e.client.send_message(e.chat.id, 'collecting info from db', reply_to=e)
        await asyncio.sleep(2)
        await y.edit(f'**First Name:** {(e.sender.first_name)}\n**Rank:** Zero\n**Level:**1\n**Warns:**{fuck}')
