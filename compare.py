def to_number(value):

    try:

        return float(str(value).replace(",", ""))

    except:

        return None


def compare_prices(current, previous):

    result = {}
    changed = False

    for key in current:

        cur = to_number(current.get(key))
        old = to_number(previous.get(key))

        if cur is None or old is None:

            result[key] = {
                "changed": False,
                "diff": 0,
                "percent": 0,
            }

            continue

        diff = round(cur - old, 2)

        percent = 0

        if old != 0:

            percent = round((diff / old) * 100, 2)

        result[key] = {
            "changed": diff != 0,
            "diff": diff,
            "percent": percent,
        }

        if diff != 0:

            changed = True

    return changed, result
