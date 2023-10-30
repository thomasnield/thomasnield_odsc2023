from sympy import * 

x = symbols('x')
f = x**2

# area from 0 to 2.5 
area = integrate(f, (x, 0, 2.5))
print(area) # 5.28033333333333
