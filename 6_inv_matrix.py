import numpy as np 

A = np.array([[2,1],[5,2])
inv_A = np.linalg.inv(A)

print(inv_A)

I = inv_A @ A 
print(I)
