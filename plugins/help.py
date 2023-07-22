from pyrogram import Client, filters
from rsrconfig import Config

@Client.on_message(filters.command("help", prefixes=[".", ","]) & (filters.me | filters.user(Config.SUDO)))
async def mzhelp(client, message):
    await client.send_message(chat_id=message.chat.id, text="Helpline group: @helptereuhte", reply_to_message_id=message.id)
    return
