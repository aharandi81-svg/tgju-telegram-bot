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

    if change["diff"] > 0:
        return f"🟢 +{comma(change['diff'])} (+{change['percent']}%)"

    if change["diff"] < 0:
        return f"🔴 {comma(change['diff'])} ({change['percent']}%)"

    return "➖ بدون تغییر"


def market_message(data, changes):

    date, time = get_persian_datetime()

    return f"""
📊 قیمت لحظه ای بازار

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

🌍 اونس جهانی
${comma(data["ounce"])}
{trend(changes["ounce"])}

₿ بیت کوین
${comma(data["btc"])}
{trend(changes["btc"])}

Ξ اتریوم
${comma(data["eth"])}
{trend(changes["eth"])}

🟡 بایننس کوین
${comma(data["bnb"])}
{trend(changes["bnb"])}

📅 {date}
🕒 {time}

📍 @goldenhook2026
⚜️ Catch The Golden Opportunities
"""
