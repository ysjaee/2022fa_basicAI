import numpy as np
import matplotlib.pylab as plt
'''
def step_function(x):
    return np.array(x>0,dtype=np.int)
x = np.arange(-5.0,5.0,0.1)
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()
'''
def sigmoid(x):
    return 1 / (1+np.exp(-x))
x = np.arange(-5.0,5.0,0.1)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()
# y값에 계단함수 대신 sigmoid를 쓰면 계단함수를 경계로 부드러운 곡선으로 바뀐다.
'''
두 함수의 공통점은 비선형 함수이다. 
일반적으로 회귀에는 항등 함수 분류에는 소프트맥스 함수 사용
softmax 함수를 이용함으로써 문제를 확률적으로 대응 
'''