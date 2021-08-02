# arbitrary_metadata.py
import json


def money_per_month(money: "in dollar", months: "number of months") -> "dollar per month":
    return money / months


print(money_per_month(3_000, 2))
print(json.dumps(money_per_month.__annotations__, indent=4))
