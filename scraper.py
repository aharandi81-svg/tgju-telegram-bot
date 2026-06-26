import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_price(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        price = soup.find("span", {"data-col": "info.last_trade.PDrCotVal"})

        if price:
            return price.text.strip()

        return "N/A"

    except Exception as e:
        return "Error"


def get_all_prices():
    data = {
        "usd": get_price("https://www.tgju.org/profile/price_dollar_rl"),
        "eur": get_price("https://www.tgju.org/profile/price_eur"),
        "gold18": get_price("https://www.tgju.org/profile/geram18"),
        "coin": get_price("https://www.tgju.org/profile/sekee_emami"),
    }

    return data
