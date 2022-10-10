from basic_operations.annuity import annuity_future, present_annuity, future_annuity, annuity_present
from basic_operations.annuity_due import future_value
from basic_operations.annuity_anticipated import anticipated_annuity_future, anticipated_present_annuity, anticipated_future_annuity, anticipated_annuity_present, anticipated_period_future, anticipated_period_present
from utilities.bisection_method import bisection_method
from mix_operations.present_value import check_flux_money
from rate_operations.rate_inflation import real_rate, efective_rate, inflation
from rate_operations.rate import single_rate, efective_period_rate

# 1
result = annuity_present(42000, 0.21/24 ,46)

# 2
result = 3200*27 - present_annuity(3200, 0.143/12, 27)

# 3
result = annuity_present(46000, 0.23/24 , 42)

# 4
i = efective_period_rate(0.167, 6)
result = inflation(0.094, i)

# 5
i = efective_period_rate(0.12, 24)
result = efective_rate(i, 0.07)

# 6
result = efective_rate(0.0873, 0.105)

# 7
ie = efective_period_rate(0.152, 12)
result = inflation(0.1237, ie)

# 8
result = anticipated_present_annuity(1009.99, 0.196/24, 25)

# 9
result = anticipated_annuity_present(80000, 0.26/12, 11)

# 10
result = anticipated_period_future(60000, 495.05, 0.005/2)

print(result)