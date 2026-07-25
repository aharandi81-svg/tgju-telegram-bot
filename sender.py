from telegram import Bot
import asyncio
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)


async def send(channels, message):

    for chat_id in channels:

        try:

            await bot.send_message(
                chat_id=chat_id,
                text=message,
                disable_web_page_preview=True
            )

            print(f"✅ Sent -> {chat_id}")

        except Exception as e:

            print(f"❌ {chat_id}")
            print(e)

        # جلوگیری از Flood تلگرام
        await asyncio.sleep(2)
