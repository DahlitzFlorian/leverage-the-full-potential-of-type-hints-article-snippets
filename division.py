# division.py
from typing import Union

Number = Union[int, float]

def division(divident: Number, divisor: Number) -> float:
    return divident / divisor


result = division(1.5, 2)
print(result)  # 0.75
