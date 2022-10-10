import math

def anticipated_present_annuity(a:float, i:float, n:int) -> float:
    return a*((1+i)*((((1+i)**n)-1)/(i*((1+i)**n))))

def anticipated_annuity_present(p:float, i:float, n:int) -> float:
    return p*((1+i)**(-1))*((i*((1+i)**n))/(((1+i)**n)-1))

def anticipated_future_annuity(a:float, i:float, n:int) -> float:
    return a*(1+i)*((((1+i)**n)-1)/i)

def anticipated_annuity_future(f:float, i:float, n:int) -> float:
    return f*((1+i)**(-1))*(i/(((1+i)**n)-1))

def anticipated_period_future(f:float, a:float, i:float) -> float:
    return (math.log10((f*i/(a + a*i)) + 1 )) / (math.log10(1+i))

def anticipated_period_present(p:float, a:float, i:float) -> float:
    return -(math.log10(1-p*i/(a+a*i))) / (math.log10(1+i))