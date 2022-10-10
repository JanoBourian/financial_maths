def real_rate(ie:float, inflation:float) -> float:
    return (ie - inflation)/( 1 + inflation)

def efective_rate(ir:float, inflation:float) -> float:
    return (ir*(1+inflation) + inflation)

def inflation(ir:float, ie:float) -> float:
    return (ie-ir)/(1+ir)