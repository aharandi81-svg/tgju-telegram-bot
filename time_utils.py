import jdatetime
from datetime import datetime


def get_persian_datetime():
    now = datetime.now()
    jnow = jdatetime.datetime.fromgregorian(datetime=now)

    date = jnow.strftime("%Y/%m/%d")
    time = now.strftime("%H:%M")

    return date, time
