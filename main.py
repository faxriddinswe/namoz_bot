import os
import logging
from telethon import TelegramClient, events
from telethon.sessions import StringSession

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Environment variable'lardan ma'lumotlarni olamiz
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
SESSION_STRING = os.environ.get("SESSION_STRING", "")

TARGET_CHANNEL = os.environ.get("TARGET_CHANNEL", "sherobod_muslim",)
RECEIVER_USERS = [user.strip() for user in os.environ.get("RECEIVER_USERS", "").split(",") if user.strip()]

KEYWORDS = ['bomdod', 'peshin', 'asr', 'shom', 'xufton', 'namoz vaqtlari', 'taqvim']

# StringSession orqali ulanamiz
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=TARGET_CHANNEL))
async def handle_new_post(event):
    if not event.message.text:
        return

    text_lower = event.message.text.lower()
    
    if any(word in text_lower for word in KEYWORDS):
        logging.info(f"⚡ Yangi namoz vaqti posti keldi! (ID: {event.message.id})")
        
        for target in RECEIVER_USERS:
            try:
                await event.message.forward_to(target)
                logging.info(f"🚀 Xabar {target} ga yuborildi!")
            except Exception as e:
                logging.error(f"❌ {target} ga yuborishda xatolik: {e}")

async def main():
    logging.info("🤖 Koyeb'da Userbot 24/7 rejimida ishga tushdi.")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()