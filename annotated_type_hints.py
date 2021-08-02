# annotated_type_hints.py
import typing

Dollar = typing.Annotated[float, "in dollar"]
Months = typing.Annotated[int, "number of months"]
Dollar_Per_Month = typing.Annotated[float, "dollar per month"]


def money_per_month(
    money: Dollar,
    months: Months
) -> Dollar_Per_Month:
    return money / months


print(typing.get_type_hints(money_per_month, include_extras=True))
