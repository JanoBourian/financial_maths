def anticipated_present_annuity(a:float, i:float, n:int) -> float:
    return a*((1+i)*((((1+i)**n)-1)/(i*((1+i)**n))))

def anticipated_annuity_present(p:float, i:float, n:int) -> float:
    return p*((1+i)**(-1))*((i*((1+i)**n))/(((1+i)**n)-1))

def anticipated_future_annuity(a:float, i:float, n:int) -> float:
    return a*(1+i)*((((1+i)**n)-1)/i)

def anticipated_annuity_future(f:float, i:float, n:int) -> float:
    return f*((1+i)**(-1))*(i/(((1+i)**n)-1))