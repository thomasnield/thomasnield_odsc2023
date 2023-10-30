from sympy import * 

x = symbols('x')
f = 2*x**2

dx_f = diff(f,x)
print(dx_f) # 4*x
