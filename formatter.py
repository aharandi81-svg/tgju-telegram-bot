from time_utils import get_persian_datetime


def comma(num):

    try:
        return f"{int(str(num).replace(',','')):,}"
    except:
        return num


def market_message(data):

    date,time=get_persian_datetime()

    return f"""
📊 قیمت لحظه ای بازار

💵 دلار
{comma(data["usd"])} ریال
💶 یورو
{comma(data["eur"])} ریال

🥇 طلای ۱۸
{comma(data["gold18"])} ریال
🪙 سکه
{comma(data["coin"])} ریال

📅 {date}
🕒 {time}

📍 @goldenhook2026
⚜️ Catch The Golden Opportunities
"""
