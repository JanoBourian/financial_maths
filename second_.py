from basic_operations.annuity import annuity_future, present_annuity, future_annuity, annuity_present
from basic_operations.annuity_due import future_value
from basic_operations.annuity_anticipated import anticipated_annuity_future, anticipated_present_annuity, anticipated_future_annuity, anticipated_annuity_present, anticipated_period_future, anticipated_period_present
from utilities.bisection_method import bisection_method
from mix_operations.present_value import check_flux_money
from rate_operations.rate_inflation import real_rate, efective_rate, inflation
from rate_operations.rate import single_rate, efective_period_rate

# 1
result = real_rate(.0472, .1)

# 2
i = efective_period_rate(.19, 24)
result = efective_rate(i, 0.06)

# 3
i = efective_period_rate(0.151, 12)
result = inflation(0.1253, i)

# 5
result = anticipated_period_future(60000, 495.05, 0.005/2)

# 6
result = anticipated_present_annuity(1019.99, 0.193/24, 26)

# 7
result = anticipated_annuity_future(105000, 0.0870/24, 120)

# 8
result = future_annuity(3477.01, 0.09/12, 48)

# 9
result = annuity_future(405000, 0.0825/12, 22)

# 10
result = future_annuity(600, 0.11/24, 48)

print(result)