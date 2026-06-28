import json

CACHE_FILE = "cache.json"


def load():

    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except:
        return {}


def save(data):

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )
