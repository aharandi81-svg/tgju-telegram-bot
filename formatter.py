from time_utils import get_persian_datetime


def comma(value):
    try:
        if value == "ERROR":
            return value

        if "." in str(value):
            return f"{float(value):,.2f}"

        return f"{int(str(value).replace(',','')):,}"

    except:
        return value


def trend(change):

    if change["diff"] > 0:
        return f"🟢 +{change['diff']:,} (+{change['percent']}%)"

    if change["diff"] < 0:
        return f"🔴 {change['diff']:,} ({change['percent']}%)"

    return "➖ بدون تغییر"


def market_message(data, changes):

    date, time = get_persian_datetime()

    return f"""
📊 قیمت لحظه‌ای بازار

━━━━━━━━━━━━━━
🇮🇷 بازار ایران

💵 دلار
{comma(data["usd"])} ریال
{trend(changes["usd"])}

💶 یورو
{comma(data["eur"])} ریال
{trend(changes["eur"])}

🥇 طلای ۱۸
{comma(data["gold18"])} ریال
{trend(changes["gold18"])}

🪙 سکه
{comma(data["coin"])} ریال
{trend(changes["coin"])}

━━━━━━━━━━━━━━
🌍 بازار جهانی

🟡 Gold (XAU/USD)
{comma(data["xauusd"])} $
{trend(changes["xauusd"])}

₿ Bitcoin
{comma(data["btcusdt"])} $
{trend(changes["btcusdt"])}

🟡 Binance Coin
{comma(data["bnbusdt"])} $
{trend(changes["bnbusdt"])}

━━━━━━━━━━━━━━

📅 {date}
🕒 {time}

📍 @goldenhook2026
⚜️ Catch The Golden Opportunities
"""
