import math

def future_value(p:float, i:float, n:int)->float:
    return p*((1+i)**n)

def present_value(f:float, i:float, n:int)->float:
    return f/((1+i)**n)

def rate_value(f:float, p:float, n:int)->float:
    return ((f/p)**(1/n)) - 1

def periods_aprox(f:float, p:float, i:float)->float:
    return math.log10(f/p)/math.log10(1+i)