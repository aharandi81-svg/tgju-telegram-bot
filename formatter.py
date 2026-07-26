from datetime import datetime
import jdatetime


def _fa_number(text):
    english = "0123456789"
    persian = "۰۱۲۳۴۵۶۷۸۹"

    text = str(text)

    for e, p in zip(english, persian):
        text = text.replace(e, p)

    return text


def _format_price(value):

    if value is None:
        return "-"

    txt = str(value)

    digits = ""

    started = False

    for ch in txt:
        if ch.isdigit():
            digits += ch
            started = True
        elif started:
            break

    if digits == "":
        return txt

    number = "{:,}".format(int(digits))

    return _fa_number(number)


def _arrow(diff):

    if diff > 0:
        return "🟢"

    if diff < 0:
        return "🔴"

    return "⚪"


def build_message(prices):

    now = jdatetime.datetime.fromgregorian(
        datetime=datetime.now()
    )

    date = now.strftime("%Y/%m/%d")
    time = now.strftime("%H:%M")

    text = f"""💹 قیمت لحظه‌ای بازار

🗓 {_fa_number(date)}
🕒 {_fa_number(time)}

💵 دلار
{_format_price(prices.get("usd"))} ریال

💶 یورو
{_format_price(prices.get("eur"))} ریال

🥇 طلای ۱۸ عیار
{_format_price(prices.get("gold18"))} ریال

🪙 سکه امامی
{_format_price(prices.get("coin"))} ریال

🌍 انس جهانی طلا
{prices.get("xauusd","-")}

₿ بیت‌کوین
{prices.get("btcusdt","-")} USDT

🟡 بایننس کوین
{prices.get("bnbusdt","-")} USDT

🌐 @YourChannel
"""

    return text


def build_change_message(prices, changes):

    msg = build_message(prices)

    msg += "\n━━━━━━━━━━━━━━\n"

    for key, item in changes.items():

        if not item["changed"]:
            continue

        diff = item.get("diff", 0)

        msg += f"{_arrow(diff)} {key.upper()} : {diff:+,.0f}\n"

    return msg
