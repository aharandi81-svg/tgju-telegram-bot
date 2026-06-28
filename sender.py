from telegram import Bot
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)


async def send(channels, text):

    for chat in channels:

        if not chat:
            continue

        try:

            await bot.send_message(
                chat_id=chat,
                text=text
            )

            print(f"Message sent -> {chat}")

        except Exception as e:

            print(f"Send Error: {e}")
