import os
import json
from datetime import datetime

import requests

GIST_ID = os.getenv("GIST_ID")
GIST_TOKEN = os.getenv("GIST_TOKEN")

API_URL = f"https://api.github.com/gists/{GIST_ID}"

HEADERS = {
    "Authorization": f"Bearer {GIST_TOKEN}",
    "Accept": "application/vnd.github+json",
}


def load_cache():
    try:

        r = requests.get(API_URL, headers=HEADERS, timeout=20)
        r.raise_for_status()

        files = r.json()["files"]

        content = files["cache.json"]["content"]

        return json.loads(content)

    except Exception as e:

        print(f"Cache Load Error: {e}")

        return {
            "updated_at": "",
            "last": {},
            "history": []
        }


def save_cache(prices):

    try:

        cache = load_cache()

        history = cache.get("history", [])

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        history.append({
            "time": now,
            **prices
        })

        # فقط آخرین 100 رکورد
        history = history[-100:]

        new_cache = {
            "updated_at": now,
            "last": prices,
            "history": history
        }

        body = {
            "files": {
                "cache.json": {
                    "content": json.dumps(
                        new_cache,
                        ensure_ascii=False,
                        indent=4
                    )
                }
            }
        }

        r = requests.patch(
            API_URL,
            headers=HEADERS,
            json=body,
            timeout=20
        )

        r.raise_for_status()

        print("✅ Gist Cache Updated")

    except Exception as e:

        print(f"Cache Save Error: {e}")
