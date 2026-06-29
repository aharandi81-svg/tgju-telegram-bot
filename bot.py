import asyncio

from scraper import get_all_prices
from formatter import market_message
from sender import send
from gist_cache import load_cache, save_cache
from config import CHANNELS


async def main():

    print("=" * 50)
    print("TGJU BOT STARTED")
    print("=" * 50)

    # دریافت قیمت‌ها
    prices = get_all_prices()

    print("Prices received:")
    print(prices)

    # خواندن کش
    cache = load_cache()

    # اگر یکی از قیمت‌ها ERROR بود
    if cache:
        cache = cache.get("last", {})
        
        for key in prices:
            if prices[key] == "ERROR":
                prices[key] = cache.get(key, "ERROR")

    # ذخیره کش
    save_cache(prices)

    # ساخت متن پیام
    message = market_message(prices)

    print("\n===== MESSAGE =====")
    print(message)
    print("===================\n")

    # ارسال
    await send(CHANNELS, message)

    print("Finished successfully.")


if __name__ == "__main__":
    asyncio.run(main())
