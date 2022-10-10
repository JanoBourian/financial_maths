from basic_operations.annuity_due import present_value
from typing import List

def check_flux_money(values:List) -> float:
    total = 0.0
    for value in values:
        total = total + present_value(value[1], value[2], value[0])
    return total