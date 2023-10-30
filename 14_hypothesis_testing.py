from scipy.stats import norm 

# Cold has mean recovery of 18 days with  1.5 standard deviations
mean = 18
std = 1.5

# Experimental drug has 14.5 days of recovery
x = 14.5

# Probability of 14.5
tail_p = norm.cdf(x, mean, std)

# Get p-value of both tails
p_value = 2*tail_p

print(p_value) # 0.019630657257290667
