import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)
print(np.shape(a))
a2 =a[np.newaxis,:]
print(a2)
b = np.array([[1,2,3],[4,5,6]])
print(b.shape)
print("0",b)
a2 = b[np.newaxis,:]
print("1",a2)
print(a2.shape)
a2 = a[:,np.newaxis]
print(a2)
a3 = b[:,:,np.newaxis]
print(a3)

a = np.arange(0,40)
print(a)
a2 = np.reshape(a,(5,8))
print(a2)
print(a2[1::2])
print(a2[,::3])
