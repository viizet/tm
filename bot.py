import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "8271624089:AAGPR01siAHqOYGMoc-x2f1yC7ToqG8HQKU")

API_ID = int(os.environ.get("API_ID", "26176218"))

API_HASH = os.environ.get("API_HASH", "4a50bc8acb0169930f5914eb88091736")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
