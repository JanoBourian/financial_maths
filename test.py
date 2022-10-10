from basic_operations.annuity import annuity_future, present_annuity, future_annuity, annuity_present
from basic_operations.annuity_due import future_value
from basic_operations.annuity_anticipated import anticipated_annuity_future, anticipated_present_annuity, anticipated_future_annuity, anticipated_annuity_present, anticipated_period_future, anticipated_period_present
from utilities.bisection_method import bisection_method
from mix_operations.present_value import check_flux_money

# 6 
result = anticipated_present_annuity(3559.80, .2544/12, 10)

# 10
result = anticipated_present_annuity(26350, .03, 6)

# 14
result = anticipated_annuity_present(14700, .348/24, 6)

# 18
result = anticipated_period_future(90000, 3500, 0.013/2)
result = anticipated_annuity_future(90000, 0.013/2, 23)

# 22
result = anticipated_period_present(195700, 6700, 0.15/12)

# 26
def function_to_evaluate(x:float) -> float:
    return 591600 - anticipated_future_annuity(12600, x, 30)

result = bisection_method(0.001, 1.0, 0.0000001, function_to_evaluate)

# 30
result = anticipated_present_annuity(28000, .0115/12, 300)

# 34
result = future_value(anticipated_future_annuity(1000, 0.10/24, 16), 0.0115/24, 32) + anticipated_future_annuity(1300, 0.0115/24, 32)

# 36
flux = [
    [0, 100000, 0.16],
    [1, 100000, 0.16],
    [2, 100000, 0.16],
    [3, 300000, 0.16],
    [4, 300000, 0.16],
    [5, 300000, 0.16]
]

new_value = check_flux_money(flux)
result = anticipated_annuity_present(new_value, .16, 6)
result = annuity_present(new_value, .16, 6)

# 42
result = anticipated_future_annuity(10000, 0.1/2, 10)
result = anticipated_annuity_future(81444.21, .05, 4)

# 46
# 26
def function_to_evaluate(x:float) -> float:
    return 45900 - anticipated_present_annuity(4541.38, x, 8) - 15000/((1+x)**2)

result = bisection_method(0.01, 0.05, 0.0000001, function_to_evaluate)

print(result)
print(45900 - anticipated_present_annuity(4541.38, result, 8) - 15000/((1+result)**2))