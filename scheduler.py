from datetime import datetime
import pytz


def is_market_time():

    tz=pytz.timezone(
        "Asia/Tehran"
    )

    now=datetime.now(tz)

    h=now.hour

    return 9<=h<=16scheduler.py
