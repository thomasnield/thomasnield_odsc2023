from sympy import * 

x = symbols('x')
f = 1 / (x-3)

result = limit(f,x,3)
print(result) # oo
