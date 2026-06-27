import asyncio

from scraper import get_all_prices

from formatter import market_message

from cache import load,save

from sender import send

from config import CHANNELS


async def main():

    prices=get_all_prices()

    if "ERROR" in prices.values():

        cache=load()

        if cache:

            prices=cache

        else:

            return

    else:

        save(prices)

    msg=market_message(prices)

    await send(CHANNELS,msg)


if __name__=="__main__":

    asyncio.run(main())
