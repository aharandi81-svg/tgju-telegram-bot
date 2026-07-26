import json
import requests
from config import GIST_ID, GIST_TOKEN

GIST_URL = f"https://api.github.com/gists/{GIST_ID}"

HEADERS = {
    "Authorization": f"Bearer {GIST_TOKEN}",
    "Accept": "application/vnd.github+json"
}


def load_cache():
    try:
        r = requests.get(GIST_URL, headers=HEADERS, timeout=20)
        r.raise_for_status()

        data = r.json()

        files = data.get("files", {})
        if "cache.json" not in files:
            return {}

        content = files["cache.json"]["content"]

        if not content.strip():
            return {}

        return json.loads(content)

    except Exception as e:
        print("Cache Load Error:", e)
        return {}


def save_cache(cache):

    body = {
        "files": {
            "cache.json": {
                "content": json.dumps(
                    cache,
                    ensure_ascii=False,
                    indent=2
                )
            }
        }
    }

    try:
        r = requests.patch(
            GIST_URL,
            headers=HEADERS,
            json=body,
            timeout=20
        )

        r.raise_for_status()
        return True

    except Exception as e:
        print("Cache Save Error:", e)
        return False


def get_old_prices():
    cache = load_cache()
    return cache.get("prices", {})


def update_prices(prices):

    cache = {
        "prices": prices
    }

    save_cache(cache)
