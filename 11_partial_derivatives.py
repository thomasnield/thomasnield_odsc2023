from sympy import * 

x,y = symbols('x y')
f = 2*x**2 + 4*y**3

dx_f = diff(f, x)
dx_y = diff(f, y)

print(dx_f) # 4*x
print(dy_f) # 12*y**2
