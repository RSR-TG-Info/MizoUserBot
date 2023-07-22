from pyrogram import Client

API_ID = int(input("Enter API ID: "))
API_HASH = input("Enter API HASH: ")
with Client(name="test", api_id=API_ID, api_hash=API_HASH, in_memory=True) as app:
    print(app.export_session_string())
