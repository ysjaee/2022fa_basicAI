import numpy as np
from matplotlib import pyplot as plt
import csv
# 시속 단속
f = open('input.csv','r')
file = csv.reader(f)    # csv파일 읽어오기
value = list(file)
data = np.array(value[1:],dtype='f')

# x w = -79.26862, b = 60.77626
# x = data[:, 0] / 100
x = data[:, 0]
y = data[:, 1]

def sigmoid(x):  # 시그모이드 함수 정의
    return 1/(1+np.exp(-x))

# 예측
w = -64.06770
b = 61.38567
x = 108 # True : 0
x = x / 80
pred_y = sigmoid(w * x + b)
print('x = ', x*80, 'pred: ', pred_y)

x = 50 # True : 1
x = x / 80
pred_y = sigmoid(w * x + b)
print('x = ', x*80, 'pred: ', pred_y)

x = 67 # True : 1
x = x / 80
pred_y = sigmoid(w * x + b)
print('x = ', x*80, 'pred: ', pred_y)


x = 172 # True : 0
x = x / 80
pred_y = sigmoid(w * x + b)
print('x = ', x*80, 'pred: ', pred_y)

x = 120 # True : 0
x = x / 80
pred_y = sigmoid(w * x + b)
print('x = ', x*80, 'pred: ', pred_y)

x = 66 # True : 1
x = x / 80
pred_y = sigmoid(w * x + b)
print('x = ', x*80, 'pred: ', pred_y)

x = 145 # True : 0
x = x / 80
pred_y = sigmoid(w * x + b)
print('x = ', x*80, 'pred: ', pred_y)
