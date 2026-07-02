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

    return "➖ No Change"


def line(icon, title, value, unit, change):
    return (
        f"{icon} {title}\n"
        f"💰 {value}{unit}   {trend(change)}"
    )


def market_message(data, changes):
    date, time = get_persian_datetime()

    return f"""📊 Live Market Prices

{line("🇺🇸", "USD", comma(data["usd"]), " IRR", changes["usd"])}

{line("🇪🇺", "EUR", comma(data["eur"]), " IRR", changes["eur"])}

{line("🥇", "Gold 18K", comma(data["gold18"]), " IRR", changes["gold18"])}

{line("🪙", "Coin", comma(data["coin"]), " IRR", changes["coin"])}

{line("🟡", "XAU/USD", "$" + comma(data["ounce"]), "", changes["ounce"])}

{line("₿", "BTC/USD", "$" + comma(data["btc"]), "", changes["btc"])}

{line("Ξ", "ETH/USD", "$" + comma(data["eth"]), "", changes["eth"])}

{line("🟨", "BNB/USD", "$" + comma(data["bnb"]), "", changes["bnb"])}

━━━━━━━━━━━━━━━━━━━━

🗓️ {date}   🕒 {time}

📢 @goldenhook2026
⚜️ Catch The Golden Opportunities
"""
