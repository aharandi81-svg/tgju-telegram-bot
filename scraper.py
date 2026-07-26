import requests
from bs4 import BeautifulSoup
from config import TGJU_URL, HEADERS


def _clean(text):
    return (
        text.replace("\n", "")
        .replace("\t", "")
        .replace(" ", "")
        .replace(",", "")
        .strip()
    )


def get_prices():

    r = requests.get(
        TGJU_URL,
        headers=HEADERS,
        timeout=20
    )

    r.raise_for_status()

    soup = BeautifulSoup(r.text, "lxml")

    prices = {
        "usd": None,
        "eur": None,
        "gold18": None,
        "coin": None,
    }

    rows = soup.select("tr")

    for row in rows:

        txt = row.get_text(" ", strip=True)

        if "دلار" in txt and prices["usd"] is None:
            tds = row.find_all("td")
            if len(tds) >= 2:
                prices["usd"] = _clean(tds[1].text)

        elif "یورو" in txt and prices["eur"] is None:
            tds = row.find_all("td")
            if len(tds) >= 2:
                prices["eur"] = _clean(tds[1].text)

        elif "طلای ۱۸" in txt and prices["gold18"] is None:
            tds = row.find_all("td")
            if len(tds) >= 2:
                prices["gold18"] = _clean(tds[1].text)

        elif "سکه امامی" in txt and prices["coin"] is None:
            tds = row.find_all("td")
            if len(tds) >= 2:
                prices["coin"] = _clean(tds[1].text)

    if None in prices.values():
        raise Exception("TGJU Parse Error")

    return prices


if __name__ == "__main__":
    print(get_prices())
