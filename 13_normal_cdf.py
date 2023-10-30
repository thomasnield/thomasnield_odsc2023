from scipy.stats import norm

mean = 64.53
std = 3.05

area_up_to_70 = norm.cdf(70, mean, std)
area_up_to_65 = norm.cdf(65, mean, std)
area_65_to_70 = area_up_to_70 - area_up_to_65

print(area_up_to_70) # prints 0.9635489113038331
print(area_up_to_65) # prints 0.5612339095753831
print(area_65_to_70) # prints 0.40231500172845003
