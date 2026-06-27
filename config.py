import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNELS = os.getenv(
    "CHANNELS",
    "@channel1"
).split(",")

ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

TIMEZONE = "Asia/Tehran"
