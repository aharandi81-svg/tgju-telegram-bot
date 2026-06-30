import os
import json
import requests

TOKEN = os.getenv("GIST_TOKEN")
GIST_ID = os.getenv("GIST_ID")

URL = f"https://api.github.com/gists/{GIST_ID}"

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}


def default_cache():

    return {

        "updated_at": "",

        "last": {

            "usd": "",
            "eur": "",
            "gold18": "",
            "coin": "",

            "xauusd": "",
            "btcusdt": "",
            "bnbusdt": ""

        },

        "history": []

    }


def load_cache():

    try:

        r = requests.get(URL, headers=HEADERS)

        r.raise_for_status()

        files = r.json()["files"]

        if "cache.json" not in files:

            return default_cache()

        return json.loads(files["cache.json"]["content"])

    except Exception as e:

        print("Cache Load Error:", e)

        return default_cache()


def save_cache(prices):

    cache = load_cache()

    from datetime import datetime

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cache["updated_at"] = now

    cache["last"] = prices

    cache["history"].append({

        "time": now,

        **prices

    })

    cache["history"] = cache["history"][-500:]

    body = {

        "files": {

            "cache.json": {

                "content": json.dumps(
                    cache,
                    indent=4,
                    ensure_ascii=False
                )

            }

        }

    }

    try:

        requests.patch(

            URL,

            headers=HEADERS,

            json=body

        )

        print("✅ Gist Cache Updated")

    except Exception as e:

        print("Cache Save Error:", e)
