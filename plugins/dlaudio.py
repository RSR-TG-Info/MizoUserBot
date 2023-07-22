#Audio downloader plugin (Credit Zaid)
import asyncio
from pyrogram import Client, filters
from rsrconfig import Config


@Client.on_message(filters.command("audio", prefixes=[".", ","]) & (filters.me | filters.user(Config.SUDO)))
async def send_music(client, message):
    try:
        cmd = message.command
        song_name = ""
        if len(cmd) > 1:
            song_name = " ".join(cmd[1:])
        elif message.reply_to_message and len(cmd) == 1:
            song_name = (
                    message.reply_to_message.text or message.reply_to_message.caption
            )
        elif not message.reply_to_message and len(cmd) == 1:
            await message.edit("Hla hming dah tel tur.")
            await asyncio.sleep(2)
            await message.delete()
            return

        song_results = await client.get_inline_bot_results("deezermusicbot", song_name)

        try:
            saved = await client.send_inline_bot_result(
                chat_id="me",
                query_id=song_results.query_id,
                result_id=song_results.results[0].id,
            )

            saved = await client.get_messages("me", int(saved.updates[1].message.id))
            reply_to = (
                message.reply_to_message.id
                if message.reply_to_message
                else None
            )
            await client.send_audio(
                chat_id=message.chat.id,
                audio=str(saved.audio.file_id),
                reply_to_message_id=message.id,
            )

            await client.delete_messages("me", saved.id)
        except TimeoutError:
            await message.edit("Hla a download theih loh.")
    except Exception as e:
        print(e)
        await message.edit("Hla a download theih loh.")
