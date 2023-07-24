#Credit RSR
import asyncio
from pyrogram import Client, filters
from rsrconfig import Config


@Client.on_message(filters.command("shazam", prefixes=[".", ","]) & (filters.me | filters.user(Config.SUDO)))
async def mzshazam(client, message):
    ee = await message.reply("Zawng mek...")
    chat = message.chat.id
    reply = message.reply_to_message
    if reply:
        try:
            await client.send_message(chat_id="@auddbot", text="/start")
        except RPCError:
           await ee.edit("@auddbot unblock la ti leh rawh.")
        await reply.forward("@auddbot")
        await asyncio.sleep(5)
        async for rsr in client.get_chat_history("@auddbot", limit=1):
            hmm = rsr.text
            if hmm.startswith("Forward"):
                await ee.edit("I privacy setting sut la fuh ber.")
                return
            
            else:
                await ee.delete()
                await rsr.copy(chat, reply_to_message_id=message.id)
    else:
        await ee.edit("Video emaw Audio emaw Doc file reply tur.")
