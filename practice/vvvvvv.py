import numpy as np
'''
c = np.array([1])
print(np.zeros(c))
print(np.shape(np.zeros(c)))
b = np.array([1,2])
print("aa",b.shape)
print(b)
print(np.zeros(b))
print(np.shape(np.zeros(b)))
a = np.array([1,2,3])
print(a)
print(np.zeros(a)2
print(np.shape(np.zeros(a)))
'''
'''
z = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(z)
print(np.shape(z))
zx = np.reshape(z,(1,2,2,3))
print("zxzxzx",zx)
s = np.reshape(z,(3,2,2))
print(s)
print(s.shape)

print(np.zeros((2,2,3)))
a = np.array([1,2,3])

print(a)
print(np.shape(a))
b = [[1,2,3],[4,5,6]]
c = np.array([b])
print("a",c)
print(np.shape(c))
print("v",c[1])
print(c)
print(np.shape(c))
print(np.array([1,2,3]))

x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.concatenate((x,y),axis = 0)
print(z)
'''
a = np.array([[1,2,3,4],[0,0,0,0]])
b = np.array([[5,6,7,8],[1,1,1,1]])
print("a",np.shape(a))

c = np.concatenate((a,b),axis=1)
d = np.concatenate((a,b),axis=0)
print("c",c)
print(np.shape(c))
print("d",d)
print(np.shape(d))

aa = np.array([[[1,2],[3,4]],[[10,20],[30,40]]])
bb = np.array([[[6,7],[8,9]],[[60,70],[80,90]]])
print(np.shape(aa))
zz = np.concatenate((aa,bb),axis = 0)
print(zz)
print(np.shape(zz))
cc = np.concatenate((aa,bb),axis = 1)
print(cc)
print(np.shape(cc))

dd = np.concatenate((aa,bb),axis=2)
print(dd)
print(np.shape(dd))