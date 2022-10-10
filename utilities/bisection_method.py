def bisection_method(a:float, b:float, tol:float, function_to_evaluate) -> float:
    c = (a + b) / 2
    fa = function_to_evaluate(a)
    fb = function_to_evaluate(b)
    fc = function_to_evaluate(c)
    count = 1
    while ((fa - fb) > tol):
        if fa*fc < 0:
            b = c
        elif fa*fc > 0:
            a = c
        else: 
            break
        c = (a + b) / 2
        fa = function_to_evaluate(a)
        fb = function_to_evaluate(b)
        fc = function_to_evaluate(c)
        count = count + 1
    
    return c
            