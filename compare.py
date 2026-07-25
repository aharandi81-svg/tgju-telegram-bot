import re


def to_number(value):

    if value is None:
        return None

    if isinstance(value, (int, float)):
        return float(value)

    value = str(value)

    value = value.replace(",", "")

    m = re.search(r"-?\d+(\.\d+)?", value)

    if not m:
        return None

    return float(m.group())


def compare_prices(current, previous):

    changes = {}

    changed = False

    keys = set(current.keys()) | set(previous.keys())

    for key in keys:

        old = to_number(previous.get(key))

        new = to_number(current.get(key))

        if old is None or new is None:

            changes[key] = {
                "old": old,
                "new": new,
                "diff": 0,
                "percent": 0,
                "changed": False
            }

            continue

        diff = new - old

        percent = 0

        if old != 0:

            percent = (diff / old) * 100

        is_changed = abs(diff) > 0.000001

        if is_changed:

            changed = True

        changes[key] = {
            "old": old,
            "new": new,
            "diff": round(diff, 2),
            "percent": round(percent, 2),
            "changed": is_changed
        }

    return changed, changes
