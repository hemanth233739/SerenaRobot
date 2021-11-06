# Pokedex Module Credits Pranav Ajay 🐰Github = Red-Aura 🐹 Telegram= @madepranav

import aiohttp
from pyrogram import filters
from SerenaRobot import pbot as asuna

@asuna.on_message(filters.command('pokedex'))
async def PokeDex(_, message):
    if len(message.command) != 2:
        await message.reply_text("/pokedex Pokemon Name")
        return
    pokemon = message.text.split(None, 1)[1]
    pokedex = f'https://some-random-api.ml/pokedex?pokemon={pokemon}'
    async with aiohttp.ClientSession() as session:
        async with session.get(pokedex) as request:
            if request.status == 404:
                return await message.reply_text("Wrong Pokemon Name")

            result = await request.json()
            try:
                pokemon = result['name']
                pokedex = result['id']
                type = result['type']
                poke_img = f"https://img.pokemondb.net/artwork/large/{pokemon}.jpg"
                abilities = result['abilities']
                height = result['height']
                weight = result['weight']
                gender = result['gender']
                stats = result['stats']
                description = result['description']
                caption = f"""
**Pokemon:** `{pokemon}`
**Pokedex:** `{pokedex}`
**Type:** `{type}`
**Abilities:** `{abilities}`
**Height:** `{height}`
**Weight:** `{weight}`
**Gender:** `{gender}`
**Stats:** `{stats}`
**Description:** `{description}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=poke_img, caption=caption)

@asuna.on_message(filters.command('pokecard'))
async def pokecard(event):
    pokename = event.pattern_match.group(1)
    if not pokename:
        await eor(event, "`Give A Pokemon name`")
        return
    rw = f"https://api.pokemontcg.io/v1/cards?name={pokename}"
    r = requests.get(rw)
    a = r.json()
    try:
        o = a["cards"][0]["imageUrlHiRes"]
        await event.client.send_file(
            await event.client.get_input_entity(event.chat_id), o
        )
        await event.delete()
    except BaseException:
        await eor(event, "`Be sure To give correct Name`")
        return
