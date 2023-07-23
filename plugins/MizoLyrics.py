#Credit RSR
import asyncio
from pyrogram import Client, filters
from rsrconfig import Config


@Client.on_message(filters.command("mlyrics", prefixes=[".", ","]) & (filters.me | filters.user(Config.SUDO)))
async def mzlyrics(client, message):
    ee = await message.reply("Zawng mek...")
    query = message.text.split(None, 1)[1]
    chat = message.chat.id
    try:
        await client.send_message(chat_id="@tereuhte_bot",text=f"/mlyrics {query}")
    except RPCError:
        await ee.edit("@tereuhte_bot unblock la ti leh rawh.")
        return
    await asyncio.sleep(7)
    async for rsr in client.get_chat_history("@tereuhte_bot", limit=1):
        hmm = rsr.text
        if hmm.startswith("Forward"):
            await ee.edit("I privacy setting sut la fuh ber.")
            return
            
        else:
            await ee.delete()
            await rsr.copy(chat)
    
