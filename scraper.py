import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/137.0 Safari/537.36",
    "Accept-Language": "fa-IR,fa;q=0.9,en;q=0.8"
}


def get_price(url):
    try:
        r = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        print("URL:", url)
        print("Status:", r.status_code)

        soup = BeautifulSoup(r.text, "html.parser")

        tag = soup.select_one(
            'span[data-col="info.last_trade.PDrCotVal"]'
        )

        if tag:
            value = tag.get_text(strip=True)
            print("Value:", value)
            return value

        print("Price Not Found")
        return "ERROR"

    except Exception as e:
        print(e)
        return "ERROR"


def get_all_prices():
    return {
        "usd": get_price("https://www.tgju.org/profile/price_dollar_rl"),
        "eur": get_price("https://www.tgju.org/profile/price_eur"),
        "gold18": get_price("https://www.tgju.org/profile/geram18"),
        "coin": get_price("https://www.tgju.org/profile/sekee"),
    }
