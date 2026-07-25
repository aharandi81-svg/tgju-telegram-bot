import os
import json
import requests
from datetime import datetime


GIST_ID = os.getenv("GIST_ID")
GIST_TOKEN = os.getenv("GIST_TOKEN")

FILE_NAME = "cache.json"


HEADERS = {
    "Authorization": f"token {GIST_TOKEN}",
    "Accept": "application/vnd.github+json"
}


def load_cache():

    try:

        url = f"https://api.github.com/gists/{GIST_ID}"

        r = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        r.raise_for_status()

        data = r.json()

        content = data["files"][FILE_NAME]["content"]

        return json.loads(content)

    except Exception as e:

        print("Cache Load Error:", e)

        return {}


def save_cache(prices):

    try:

        cache = load_cache()

        history = cache.get("history", [])

        history.append({

            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            **prices

        })

        history = history[-100:]

        body = {

            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "last": prices,

            "history": history

        }

        payload = {

            "files": {

                FILE_NAME: {

                    "content": json.dumps(
                        body,
                        indent=4,
                        ensure_ascii=False
                    )

                }

            }

        }

        url = f"https://api.github.com/gists/{GIST_ID}"

        r = requests.patch(
            url,
            headers=HEADERS,
            json=payload,
            timeout=20
        )

        r.raise_for_status()

        print("✅ Gist Cache Updated")

    except Exception as e:

        print("Cache Save Error:", e)
