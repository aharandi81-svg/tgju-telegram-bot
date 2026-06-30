import asyncio

from scraper import get_all_prices
from formatter import market_message
from sender import send
from gist_cache import load_cache, save_cache
from compare import compare_prices
from config import CHANNELS


async def main():

    print("=" * 50)
    print("TGJU BOT STARTED")
    print("=" * 50)

    prices = get_all_prices()

    print("Prices received:")
    print(prices)

    cache = load_cache()
    last_prices = cache.get("last", {}) if cache else {}

    used_cache = False

    # اگر ERROR بود از کش استفاده کن
    for key in prices:

        if prices[key] == "ERROR" and key in last_prices:

            prices[key] = last_prices[key]
            used_cache = True

    # مقایسه قیمت ها
    changed, changes = compare_prices(prices, last_prices)

    print("\n========== CHANGES ==========")

    for key, item in changes.items():

        if item["changed"]:

            print(
                f"{key.upper()} : "
                f"{item['diff']:+,} "
                f"({item['percent']:+.2f}%)"
            )

        else:

            print(f"{key.upper()} : No Change")

    print("=============================\n")

    # اگر هیچ تغییری نبود
    if last_prices and not changed:

        print("⛔ No market changes.")
        print("Skip sending message.")
        return

    # ذخیره کش
    if "ERROR" not in prices.values():

        save_cache(prices)
        print("✅ Cache Updated")

    else:

        print("⚠ Cache NOT Updated")

    # ساخت پیام
    message = market_message(prices, changes)

    print("\n===== MESSAGE =====")
    print(message)
    print("===================\n")

    if used_cache:
        print("✅ Some prices loaded from Gist Cache")

    await send(CHANNELS, message)

    print("Finished successfully.")


if __name__ == "__main__":
    asyncio.run(main())
