from basic_operations.annuity import annuity_future, present_annuity, future_annuity, annuity_present
from basic_operations.annuity_due import future_value
from basic_operations.annuity_anticipated import anticipated_annuity_future, anticipated_present_annuity, anticipated_future_annuity, anticipated_annuity_present

# 5
result = anticipated_annuity_future(140000, 0.0995/24, 56)
print(result)

# 6
result = anticipated_present_annuity(1550, 0.155/12, 46)
print(1550*46 - result)

# 7
result = anticipated_annuity_present(85000, 0.24/12, 12)
print(result)

# 8
result = future_annuity(500, 0.09/24, 56)
print(result)

# 9
result = future_annuity(550, 0.1/24, 52)
print(result)

# 10
result = future_annuity(1200, 0.097/12, 28)
print(result - 1200*28)