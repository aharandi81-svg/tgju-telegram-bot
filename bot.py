import os
import asyncio
from telegram import Bot

from scraper import get_all_prices
from time_utils import get_persian_datetime


# گرفتن توکن و کانال از GitHub Secrets
TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ["CHANNEL_ID"]

bot = Bot(token=TOKEN)


# فرمت عددی (سه‌تا سه‌تا)
def format_number(price):
    if not price:
        return "N/A"

    try:
        num = int(price.replace(",", ""))
        return f"{num:,}"
    except:
        return price


# ساخت پیام نهایی
def format_message(p):
    date, time = get_persian_datetime()

    return f"""
📊 قیمت لحظه‌ای بازار

💵 دلار: {format_number(p['usd'])} ریال
💶 یورو: {format_number(p['eur'])} ریال

🥇 طلای ۱۸ عیار: {format_number(p['gold18'])} ریال
🪙 سکه امامی: {format_number(p['coin'])} ریال

📅 تاریخ: {date}
🕒 ساعت: {time}

 📍 @goldenhook2026
⚜️ Catch The Golden Opportunities
"""


# اجرای اصلی
async def main():
    try:
        prices = get_all_prices()
        message = format_message(prices)

        await bot.send_message(
            chat_id=CHANNEL,
            text=message
        )

        print("✅ Message sent successfully")

    except Exception as e:
        print("❌ Error:", str(e))


if __name__ == "__main__":
    asyncio.run(main())
