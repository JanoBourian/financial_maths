def present_annuity(a:float, i:float, n:int) -> float:
    return a*((((1+i)**n)-1)/(i*((1+i)**n)))

def annuity_present(p:float, i:float, n:int) -> float:
    return p*((i*((1+i)**n))/(((1+i)**n)-1))

def future_annuity(a:float, i:float, n:int) -> float:
    return a*((((1+i)**n)-1)/(i))

def annuity_future(f:float, i:float, n:int) -> float:
    return f*((i)/(((1+i)**n)-1))