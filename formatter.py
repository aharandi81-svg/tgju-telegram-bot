from time_utils import get_persian_datetime


def comma(num):
    try:
        value = float(str(num).replace(",", ""))

        if value.is_integer():
            return f"{int(value):,}"

        return f"{value:,.2f}"

    except:
        return num


def trend(change):
    diff = change["diff"]
    percent = change["percent"]

    if diff > 0:
        return f"📈 +{comma(diff)} (+{percent:.2f}%)"

    if diff < 0:
        return f"📉 {comma(diff)} ({percent:.2f}%)"

    return "➖ بدون تغییر"


def line(icon, title, value, unit, change):
    return (
        f"{icon} {title}\n"
        f"💰 {value}{unit}   {trend(change)}"
    )


def market_message(data, changes):
    date, time = get_persian_datetime()

    return f"""📊 قیمت لحظه‌ای بازار

{line("💵", "دلار", comma(data["usd"]), " ریال", changes["usd"])}

{line("💶", "یورو", comma(data["eur"]), " ریال", changes["eur"])}

{line("🥇", "طلای ۱۸ عیار", comma(data["gold18"]), " ریال", changes["gold18"])}

{line("🪙", "سکه", comma(data["coin"]), " ریال", changes["coin"])}

{line("🟡", "اونس طلا (XAU/USD)", "$" + comma(data["ounce"]), "", changes["ounce"])}

{line("₿", "بیت‌کوین (BTC/USD)", "$" + comma(data["btc"]), "", changes["btc"])}

{line("Ξ", "اتریوم (ETH/USD)", "$" + comma(data["eth"]), "", changes["eth"])}

{line("🟨", "بایننس کوین (BNB/USD)", "$" + comma(data["bnb"]), "", changes["bnb"])}

━━━━━━━━━━━━━━━━━━━━

📅 تاریخ: {date}
🕒 ساعت: {time}

📍 @goldenhook2026
⚜️ Catch The Golden Opportunities
"""
