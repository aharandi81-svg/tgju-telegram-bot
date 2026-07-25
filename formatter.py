import jdatetime
from datetime import datetime


def fmt(value):

    try:

        if isinstance(value, str):
            return value

        if abs(value) >= 1000:
            return f"{value:,.0f}"

        return f"{value}"

    except:
        return str(value)


def arrow(v):

    if v > 0:
        return "🟢"

    if v < 0:
        return "🔴"

    return "⚪"


def market_message(prices, changes):

    now = jdatetime.datetime.fromgregorian(
        datetime=datetime.now()
    )

    text = []

    text.append("📊 قیمت لحظه‌ای بازار\n")

    # ---------------- TGJU ----------------

    items = [
        ("usd", "💵 دلار"),
        ("eur", "💶 یورو"),
        ("gold18", "🥇 طلای ۱۸"),
        ("coin", "🪙 سکه")
    ]

    for key, title in items:

        value = prices.get(key, "-")

        text.append(title)

        text.append(str(value))

        if key in changes:

            c = changes[key]

            if c["changed"]:

                text.append(
                    f"{arrow(c['diff'])} "
                    f"{c['diff']:+,} ریال"
                )

                text.append(
                    f"({c['percent']:+.2f}%)"
                )

        text.append("")

    # ---------------- GLOBAL ----------------

    text.append("🌍 بازار جهانی\n")

    globals_items = [
        ("xauusd", "🥇 Gold"),
        ("btcusdt", "₿ Bitcoin"),
        ("bnbusdt", "🟡 BNB")
    ]

    for key, title in globals_items:

        value = prices.get(key)

        if value:

            text.append(title)
            text.append(str(value))

            if key in changes:

                c = changes[key]

                if c["changed"]:

                    text.append(
                        f"{arrow(c['diff'])} "
                        f"{c['diff']:+}"
                    )

                    text.append(
                        f"({c['percent']:+.2f}%)"
                    )

            text.append("")

    text.append(f"📅 {now.strftime('%Y/%m/%d')}")
    text.append(f"🕒 {now.strftime('%H:%M')}")

    text.append("")
    text.append("📍 ***")
    text.append("⚜️ Catch The Golden Opportunities")

    return "\n".join(text)
