import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_price(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        # روش 1: دقیق (اصلی)
        tag = soup.select_one('span[data-col="info.last_trade.PDrCotVal"]')

        if tag and tag.text.strip():
            return tag.text.strip()

        # روش 2: fallback (اگر اولی شکست خورد)
        alt = soup.find("span", class_="value")
        if alt and alt.text.strip():
            return alt.text.strip()

        return "ERROR"

    except Exception as e:
        print("Scraper error:", e)
        return "ERROR"


def get_all_prices():
    return {
        "usd": get_price("https://www.tgju.org/profile/price_dollar_rl"),
        "eur": get_price("https://www.tgju.org/profile/price_eur"),
        "gold18": get_price("https://www.tgju.org/profile/geram18"),
        "coin": get_price("https://www.tgju.org/profile/sekee"),
    }
