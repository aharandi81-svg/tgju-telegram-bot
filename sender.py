from telegram import Bot
from config import BOT_TOKEN

bot=Bot(BOT_TOKEN)


async def send(channels,text):

    for ch in channels:

        try:

            await bot.send_message(
                chat_id=ch,
                text=text
            )

            print(ch,"OK")

        except Exception as e:

            print(ch,e)
