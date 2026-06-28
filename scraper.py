import requests
from bs4 import BeautifulSoup

URL = "https://www.tgju.org"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/137.0 Safari/537.36"
}

MARKETS = {
    "price_dollar_rl": "usd",
    "price_eur": "eur",
    "geram18": "gold18",
    "sekee": "coin"
}


def get_all_prices():

    result = {}

    try:

        r = requests.get(
            URL,
            headers=HEADERS,
            timeout=20
        )

        r.raise_for_status()

        soup = BeautifulSoup(r.text, "html.parser")

        for market, key in MARKETS.items():

            item = soup.find(id=f"l-{market}")

            if item:

                price = item.find("span", class_="info-price")

                if price:
                    result[key] = price.get_text(strip=True)
                else:
                    result[key] = "ERROR"

            else:
                result[key] = "ERROR"

    except Exception as e:

        print("Scraper Error:", e)

        for key in MARKETS.values():
            result[key] = "ERROR"

    print("Prices:", result)

    return result
