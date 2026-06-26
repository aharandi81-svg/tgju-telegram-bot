import jdatetime
from datetime import datetime


def get_persian_datetime():
    now = datetime.now()
    jnow = jdatetime.datetime.fromgregorian(datetime=now)

    return jnow.strftime("%Y/%m/%d"), now.strftime("%H:%M")
