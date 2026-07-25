import requests
from bs4 import BeautifulSoup


URL = "https://www.tgju.org/"


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


def clean(text):

    return (
        text.replace("\n", "")
        .replace("\t", "")
        .replace("\xa0", "")
        .strip()
    )


def get_value(soup, id_name):

    try:

        td = soup.find("td", {"data-market-nameslug": id_name})

        price = clean(
            td.find("span", class_="price").text
        )

        change = clean(
            td.find("span", class_="change").text
        )

        percent = clean(
            td.find("span", class_="percent").text
        )

        return f"{price} ({percent}) {change}"

    except Exception:

        return "ERROR"


def get_all_prices():

    try:

        r = requests.get(
            URL,
            headers=HEADERS,
            timeout=20
        )

        print("Status:", r.status_code)

        soup = BeautifulSoup(
            r.text,
            "html.parser"
        )

        prices = {

            "usd": get_value(
                soup,
                "price_dollar_rl"
            ),

            "eur": get_value(
                soup,
                "price_eur"
            ),

            "gold18": get_value(
                soup,
                "geram18"
            ),

            "coin": get_value(
                soup,
                "sekeb"
            )

        }

        print("Prices:", prices)

        return prices

    except Exception as e:

        print(e)

        return {

            "usd": "ERROR",
            "eur": "ERROR",
            "gold18": "ERROR",
            "coin": "ERROR"

        }
