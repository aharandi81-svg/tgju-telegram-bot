import jdatetime
from datetime import datetime
import pytz


def get_persian_datetime():
    tehran = pytz.timezone("Asia/Tehran")
    now = datetime.now(tehran)

    jnow = jdatetime.datetime.fromgregorian(datetime=now)

    date = jnow.strftime("%Y/%m/%d")
    time = now.strftime("%H:%M")

    return date, time
