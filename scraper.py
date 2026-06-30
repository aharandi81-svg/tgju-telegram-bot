import requests
from bs4 import BeautifulSoup

from tradingview_scraper import get_tv_prices


URL = "https://www.tgju.org"


def clean(text):
    return (
        text.replace(",", "")
        .replace("ريال", "")
        .replace("ریال", "")
        .replace("\n", "")
        .strip()
    )


def get_all_prices():

    result = {
        "usd": "ERROR",
        "eur": "ERROR",
        "gold18": "ERROR",
        "coin": "ERROR",
    }

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(URL, headers=headers, timeout=20)

        print("Status:", response.status_code)

        soup = BeautifulSoup(response.text, "html.parser")

        # دلار
        tag = soup.find(id="l-price_dollar_rl")
        if tag:
            result["usd"] = clean(tag.text)

        # یورو
        tag = soup.find(id="l-price_eur")
        if tag:
            result["eur"] = clean(tag.text)

        # طلای 18
        tag = soup.find(id="l-geram18")
        if tag:
            result["gold18"] = clean(tag.text)

        # سکه
        tag = soup.find(id="l-sekee")
        if tag:
            result["coin"] = clean(tag.text)

    except Exception as e:

        print("TGJU Error:", e)

    # TradingView
    tv = get_tv_prices()

    result["xauusd"] = tv["xauusd"]["price"]
    result["btcusdt"] = tv["btcusdt"]["price"]
    result["bnbusdt"] = tv["bnbusdt"]["price"]

    print("Prices:", result)

    return result
