def to_int(value):
    try:
        return int(str(value).replace(",", ""))
    except:
        return None


def compare_prices(current, previous):

    result = {}
    changed = False

    for key in current:

        cur = to_int(current.get(key))
        old = to_int(previous.get(key))

        if cur is None or old is None:

            result[key] = {
                "changed": False,
                "diff": 0,
                "percent": 0
            }
            continue

        diff = cur - old

        percent = 0

        if old != 0:
            percent = round((diff / old) * 100, 2)

        result[key] = {
            "changed": diff != 0,
            "diff": diff,
            "percent": percent
        }

        if diff != 0:
            changed = True

    return changed, result
