import requests
from bs4 import BeautifulSoup

URL = "https://www.tgju.org"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
}

MARKETS = {
    "price_dollar_rl": "usd",
    "price_eur": "eur",
    "geram18": "gold18",
    "sekee": "coin",
}


def get_all_prices():

    result = {}

    try:

        response = requests.get(
            URL,
            headers=HEADERS,
            timeout=20,
        )

        response.raise_for_status()

        print("Status:", response.status_code)

        soup = BeautifulSoup(response.text, "html.parser")

        for market_id, key in MARKETS.items():

            value = None

            # ---------- روش اول ----------
            item = soup.find(id=f"l-{market_id}")

            if item:

                price = item.find("span", class_="info-price")

                if price:
                    value = price.get_text(strip=True)

            # ---------- روش دوم ----------
            if value is None:

                row = soup.find(
                    "tr",
                    attrs={"data-market-row": market_id},
                )

                if row:

                    td = row.find("td", class_="market-price")

                    if td:
                        value = td.get_text(strip=True)

            if value:
                result[key] = value

            else:
                result[key] = "ERROR"

        print("Prices:", result)

        return result

    except Exception as e:

        print("SCRAPER ERROR:", e)

        return {
            "usd": "ERROR",
            "eur": "ERROR",
            "gold18": "ERROR",
            "coin": "ERROR",
        }
