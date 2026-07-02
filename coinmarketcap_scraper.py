import requests

URL = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"

WATCHLIST = {
    "BTC": "btc",
    "ETH": "eth",
    "BNB": "bnb",
}


def get_crypto_prices():

    result = {
        "btc": "ERROR",
        "eth": "ERROR",
        "bnb": "ERROR",
    }

    try:

        r = requests.get(
            URL,
            params={
                "start": 1,
                "limit": 20,
                "sortBy": "market_cap",
                "sortType": "desc",
                "convert": "USD",
                "cryptoType": "all",
                "tagType": "all",
                "audited": "false",
            },
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json",
            },
            timeout=20,
        )

        data = r.json()["data"]["cryptoCurrencyList"]

        for coin in data:

            if coin["symbol"] in WATCHLIST:

                result[WATCHLIST[coin["symbol"]]] = round(
                    coin["quotes"][0]["price"], 2
                )

        return result

    except Exception as e:

        print("CoinMarketCap Error:", e)

        return result
