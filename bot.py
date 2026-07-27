import asyncio

from scraper import get_prices
from formatter import build_message
from compare import compare_prices
from sender import send_message


async def main():

    print("=" * 50)
    print("TGJU BOT STARTED")
    print("=" * 50)

    try:

        prices = get_prices()

        print("Prices received:")
        print(prices)

        changed, changes = compare_prices(prices)

        if changed:

            message = build_message(prices)

            await send_message(message)

            print("✅ Message Sent")

        else:

            print("⛔ No market changes.")

    except Exception as e:

        print("BOT ERROR")
        print(e)


if __name__ == "__main__":

    asyncio.run(main())
