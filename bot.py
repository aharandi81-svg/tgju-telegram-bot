import os
import asyncio
from telegram import Bot

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ["CHANNEL_ID"]

bot = Bot(token=TOKEN)

async def main():
    await bot.send_message(
        chat_id=CHANNEL,
        text="✅ ربات با موفقیت از GitHub Actions اجرا شد!"
    )

asyncio.run(main())
