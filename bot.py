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

    used_cache = False

    if cache:

        last_prices = cache.get("last", {})

        for key in prices:

            if prices.get(key) == "ERROR":

                if key in last_prices:
                    prices[key] = last_prices[key]
                    used_cache = True

    # فقط اگر همه قیمت‌ها معتبر بودند کش را بروزرسانی کن
    if "ERROR" not in prices.values():

        save_cache(prices)
        print("✅ Cache Updated")

    else:

        print("⚠ Cache NOT Updated")

    # ساخت پیام
    message = market_message(prices)

    print("\n===== MESSAGE =====")
    print(message)
    print("===================\n")

    if used_cache:
        print("✅ Some prices loaded from Gist Cache")

    # ارسال به کانال‌ها
    await send(CHANNELS, message)

    print("Finished successfully.")


if __name__ == "__main__":
    asyncio.run(main())
