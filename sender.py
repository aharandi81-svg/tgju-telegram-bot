from telegram import Bot
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)


async def send(channels, text):

    for channel in channels:

        if not channel:
            continue

        try:

            await bot.send_message(
                chat_id=channel,
                text=text
            )

            print(f"✅ Sent -> {channel}")

        except Exception as e:

            print(f"❌ Send Error -> {e}")
