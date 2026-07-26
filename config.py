import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

CHANNEL_ID = os.getenv("CHANNEL_ID", "")

GIST_ID = os.getenv("GIST_ID", "")

GIST_TOKEN = os.getenv("GIST_TOKEN", "")

PORT = int(os.getenv("PORT", "10000"))

WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")

TGJU_URL = "https://www.tgju.org/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}

CHANNELS = [CHANNEL_ID] if CHANNEL_ID else []
