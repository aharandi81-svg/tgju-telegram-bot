import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNELS = [
    os.getenv("CHANNEL_ID")
]

GIST_ID = os.getenv("GIST_ID")
GIST_TOKEN = os.getenv("GIST_TOKEN")

TGJU_URL = "https://www.tgju.org"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}
