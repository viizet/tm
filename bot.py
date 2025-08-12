import asyncio
from pyrogram import Client, compose, idle
import os
import threading
from flask import Flask
from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
STRING = os.environ.get("STRING", "")

# Validate required environment variables
if not TOKEN:
    print("ERROR: TOKEN environment variable is required")
    exit(1)
if not API_ID or API_ID == 0:
    print("ERROR: API_ID environment variable is required")
    exit(1)
if not API_HASH:
    print("ERROR: API_HASH environment variable is required")
    exit(1)

# Create Flask app for health checks
web_app = Flask(__name__)

@web_app.route('/')
def health_check():
    return "Bot is running!", 200

@web_app.route('/health')
def health():
    return {"status": "healthy"}, 200

def run_web_server():
    port = int(os.environ.get("PORT", 80))
    web_app.run(host='0.0.0.0', port=port, debug=False)

bot = Client(
    "Renamer",
    bot_token=TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

if __name__ == "__main__":
    # Start Flask web server in a separate thread
    web_thread = threading.Thread(target=run_web_server)
    web_thread.daemon = True
    web_thread.start()

    if STRING:
        apps = [Client2, bot]
        for app in apps:
            app.start()
        idle()
        for app in apps:
            app.stop()
    else:
        bot.run()