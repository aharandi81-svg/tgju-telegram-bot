import asyncio

from scraper import get_all_prices
from coinmarketcap_scraper import get_crypto_prices
from formatter import market_message
from sender import send
from gist_cache import load_cache, save_cache
from compare import compare_prices
from config import CHANNELS


async def main():

    print("=" * 60)
    print("TGJU BOT STARTED")
    print("=" * 60)

    # ---------- TGJU ----------
    prices = get_all_prices()

    # ---------- CoinMarketCap ----------
    crypto = get_crypto_prices()

    prices.update(crypto)

    print("Prices received:")
    print(prices)

    # ---------- Load Cache ----------
    cache = load_cache()

    if cache:
        last_prices = cache.get("last", {})
    else:
        last_prices = {}

    used_cache = False

    # ---------- اگر قیمت ERROR بود ----------
    for key in prices:

        if prices.get(key) == "ERROR":

            if key in last_prices:

                prices[key] = last_prices[key]
                used_cache = True

    # ---------- Compare ----------
    changed, changes = compare_prices(
        prices,
        last_prices
    )

    print("\n========== CHANGES ==========")

    for key, value in changes.items():

        if value["changed"]:

            print(
                f"{key.upper():10}"
                f"{value['diff']:+,}"
                f" ({value['percent']:+.2f}%)"
            )

        else:

            print(f"{key.upper():10}No Change")

    print("=============================\n")

    # ---------- اگر هیچ تغییری نبود ----------
    if last_prices and not changed:

        print("⛔ No market changes.")
        print("Skip sending.")
        return

    # ---------- Save Cache ----------
    if "ERROR" not in prices.values():

        save_cache(prices)

        print("✅ Cache Updated")

    else:

        print("⚠ Cache NOT Updated")

    # ---------- Message ----------
    message = market_message(
        prices,
        changes
    )

    print("\n===== MESSAGE =====")
    print(message)
    print("===================\n")

    if used_cache:

        print("✅ Some values loaded from Gist Cache")

    # ---------- Send ----------
    await send(
        CHANNELS,
        message
    )

    print("Finished Successfully.")


if __name__ == "__main__":

    asyncio.run(main())
