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
print("Checking environment variables...")
if not TOKEN:
    print("ERROR: TOKEN environment variable is required")
    exit(1)
else:
    print("✓ TOKEN found")
    
if not API_ID or API_ID == 0:
    print("ERROR: API_ID environment variable is required")
    exit(1)
else:
    print("✓ API_ID found")
    
if not API_HASH:
    print("ERROR: API_HASH environment variable is required")
    exit(1)
else:
    print("✓ API_HASH found")

print("All required environment variables are set!")

# Create Flask app for health checks
web_app = Flask(__name__)

@web_app.route('/')
def health_check():
    return "Gangster Baby Renamer Bot is running!", 200

@web_app.route('/health')
def health():
    return {"status": "healthy", "bot": "active"}, 200

@web_app.route('/ping')
def ping():
    return "pong", 200

def run_web_server():
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting web server on port {port}")
    web_app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

bot = Client(
    "Renamer",
    bot_token=TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

if __name__ == "__main__":
    print("Starting Gangster Baby Renamer Bot...")
    
    # Start Flask web server in a separate thread
    web_thread = threading.Thread(target=run_web_server)
    web_thread.daemon = True
    web_thread.start()
    print("Web server started")

    try:
        if STRING:
            print("Starting with STRING session...")
            apps = [Client2, bot]
            for app in apps:
                app.start()
            print("Both clients started successfully")
            idle()
            for app in apps:
                app.stop()
        else:
            print("Starting bot only...")
            bot.run()
    except Exception as e:
        print(f"Error starting bot: {e}")
        import traceback
        traceback.print_exc()