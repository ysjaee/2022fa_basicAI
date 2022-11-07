import numpy as np

x = np.arange(40)
print(x)
x = x.reshape(5,8)
print(x)

print(x[:3,:5])
print(x[2:,-3:])
print(x[-3:,-3:])
print(x[:,3])
print(x[1,3:6])
print(x[1::2,::3])