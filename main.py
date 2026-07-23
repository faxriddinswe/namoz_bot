import asyncio
import logging
from telethon import TelegramClient, events

# Konsolda nima bo'layotganini tartibli ko'rib turish uchun log sozlamalari
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ------------------- SOZLAMALAR -------------------
API_ID = 38984573  # O'zingizning api_id (raqam ko'rinishida)
API_HASH = 'b23432de9f10b5e49e24d859fab7f33f'  # O'zingizning api_hash

# Kuzatmoqchi bo'lgan kanal username'i ('@' belgisiz)
TARGET_CHANNEL = 'question_prep' 

# Post borishi kerak bo'lgan akkauntlar ro'yxati (username yoki Telegram ID)
RECEIVER_USERS = [
    'Mark_zukerberk',
]

# Namoz vaqtlarini aniqlovchi kalit so'zlar
KEYWORDS = ['bomdod', 'peshin', 'asr', 'shom', 'xufton', 'namoz vaqtlari', 'taqvim']
# --------------------------------------------------

client = TelegramClient('user_session', API_ID, API_HASH)


@client.on(events.NewMessage(chats=TARGET_CHANNEL))
async def handle_new_post(event):
    """
    Kanalga yangi post tushishi bilan bir zumda ishlaydi.
    """
    if not event.message.text:
        return

    text_lower = event.message.text.lower()
    
    # Post ichida namoz vaqtlari haqida so'z borligini tekshiramiz
    if any(word in text_lower for word in KEYWORDS):
        logging.info(f"⚡ Yangi namoz vaqti posti keldi! (Message ID: {event.message.id})")
        
        for target in RECEIVER_USERS:
            try:
                await event.message.forward_to(target)
                logging.info(f"🚀 Xabar {target} ga avtomatik forward qilindi!")
            except Exception as e:
                logging.error(f"❌ {target} ga yuborishda xatolik: {e}")


async def main():
    logging.info("🤖 Userbot 24/7 real-vaqt rejimida ishga tushdi.")
    logging.info(f"📢 '{TARGET_CHANNEL}' kanali kuzatilmoqda...")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()