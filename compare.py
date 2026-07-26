from gist_cache import get_old_prices, update_prices


def _to_float(value):
    """
    استخراج عدد از رشته
    مثال:
    دلار1724900(0.93%)15900
    -->
    1724900
    """

    if value is None:
        return None

    if isinstance(value, (int, float)):
        return float(value)

    txt = str(value)

    digits = ""

    started = False

    for ch in txt:
        if ch.isdigit() or ch == ".":
            digits += ch
            started = True
        elif started:
            break

    if digits == "":
        return None

    try:
        return float(digits)
    except:
        return None


def compare_prices(new_prices):

    old_prices = get_old_prices()

    result = {}

    changed = False

    for key, value in new_prices.items():

        new_value = _to_float(value)
        old_value = _to_float(old_prices.get(key))

        if old_value is None:
            result[key] = {
                "changed": True,
                "old": None,
                "new": value
            }
            changed = True
            continue

        if new_value != old_value:

            changed = True

            diff = round(new_value - old_value, 2)

            percent = 0

            if old_value != 0:
                percent = round((diff / old_value) * 100, 2)

            result[key] = {
                "changed": True,
                "old": old_value,
                "new": new_value,
                "diff": diff,
                "percent": percent
            }

        else:

            result[key] = {
                "changed": False,
                "old": old_value,
                "new": new_value
            }

    update_prices(new_prices)

    return changed, result
