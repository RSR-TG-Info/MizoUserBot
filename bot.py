from pyrogram import Client
from rsrconfig import Config

app = Client(
    "Mizo UserBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    session_string=Config.STRING_SESSION,
    plugins=dict(root = "plugins"),
    in_memory=True,
)

app.run()
