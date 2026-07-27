from telegram import Bot
from config import BOT_TOKEN, CHANNELS


bot = Bot(BOT_TOKEN)


async def send_message(text):

    if isinstance(CHANNELS, str):
        channels = [CHANNELS]
    else:
        channels = CHANNELS

    for channel in channels:

        if not channel:
            continue

        try:

            await bot.send_message(
                chat_id=channel,
                text=text,
                parse_mode="HTML",
                disable_web_page_preview=True,
            )

            print(f"✅ Sent -> {channel}")

        except Exception as e:

            print(f"❌ Error sending to {channel}")
            print(e)
