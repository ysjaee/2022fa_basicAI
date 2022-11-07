import numpy as np
from matplotlib import pyplot as plt
import csv
# 시속 단속
f = open('input.csv','r')
file = csv.reader(f)    # csv파일 읽어오기
value = list(file)
data = np.array(value[1:],dtype='f')


x = data[:, 0]
y = data[:, 1]

def sigmoid(x):  # 시그모이드 함수 정의
    return 1/(1+np.exp(-x))
eps = 1e-5
w = np.random.uniform(low=0, high=1)
b = np.random.uniform(low=0, high=1)
print('w: ', w, 'b: ', b)

hypothesis = sigmoid(w * x + b)

# 방법 1 -> 최적화 어려움, local minimum에 빠질 우려가 있음
error = (hypothesis - y) ** 2
cost = error.mean()
print('cost: ', cost)  # 이와 같은 cost는 최적화가 어려움

# 방법 2
cost = y * np.log(hypothesis+eps) + (1 - y) * np.log(1 - hypothesis+eps)
cost = -cost.mean()
print('cost: ', cost)
