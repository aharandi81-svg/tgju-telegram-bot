import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}


def get_price(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        tag = soup.select_one('span[data-col="info.last_trade.PDrCotVal"]')

        if tag:
            return tag.text.strip()

        return "ERROR"

    except:
        return "ERROR"


def get_all_prices():
    return {
        "usd": get_price("https://www.tgju.org/profile/price_dollar_rl"),
        "eur": get_price("https://www.tgju.org/profile/price_eur"),
        "gold18": get_price("https://www.tgju.org/profile/geram18"),
        "coin": get_price("https://www.tgju.org/profile/sekee"),
    }
