def single_rate(i:float, n:int) -> float:
    return i/n

def efective_period_rate(i:float, n:int) -> float:
    return (1+i/n)**n  -1 