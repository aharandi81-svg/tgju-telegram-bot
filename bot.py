import os
import asyncio
import json
from datetime import datetime
import pytz

from telegram import Bot
from scraper import get_all_prices
from time_utils import get_persian_datetime


TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ["CHANNEL_ID"]

bot = Bot(token=TOKEN)

def is_valid_data(p):
    return p and any(v not in ["ERROR", "N/A", None] for v in p.values())
# ---------- عدد تمیز ----------
def format_number(price):
    if not price:
        return "N/A"
    try:
        num = int(price.replace(",", ""))
        return f"{num:,}"
    except:
        return price


# ---------- cache ----------
def load_cache():
    try:
        with open("cache.json", "r") as f:
            return json.load(f)
    except:
        return {}


def save_cache(data):
    with open("cache.json", "w") as f:
        json.dump(data, f)


# ---------- زمان مجاز (ایران) ----------
def is_allowed_time():
    tehran = pytz.timezone("Asia/Tehran")
    now = datetime.now(tehran)
    return 9 <= now.hour <= 16


# ---------- پیام ----------
def format_message(p):
    date, time = get_persian_datetime()

    return f"""
📊 قیمت لحظه‌ای بازار

💵 دلار: {format_number(p.get('usd'))} ریال
💶 یورو: {format_number(p.get('eur'))} ریال

🥇 طلای ۱۸ عیار: {format_number(p.get('gold18'))} ریال
🪙 سکه امامی: {format_number(p.get('coin'))} ریال

📅 تاریخ: {date}
🕒 ساعت: {time}

📡 منبع: TGJU
"""


# ---------- main ----------
async def main():

    # ⛔ کنترل ساعت
    if not is_allowed_time():
        print("⛔ خارج از بازه زمانی (09-16)")
        return

    cache = load_cache()
    prices = get_all_prices()

    # ❌ اگر خطا داشت → استفاده از cache
    if "ERROR" in prices.values():
        print("⚠️ Scrape failed → using cache")
        prices = cache
    else:
        print("✅ Fresh data → saving cache")
        save_cache(prices)

    message = format_message(prices)

    await bot.send_message(
        chat_id=CHANNEL,
        text=message
    )

    print("📩 sent")


if __name__ == "__main__":
    asyncio.run(main())
