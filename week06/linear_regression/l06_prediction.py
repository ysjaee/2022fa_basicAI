# 신생아 표준 몸무게 와 키의 관계 (0개월부터 12월까지)
import numpy as np
from matplotlib import pyplot as plt
import csv

f = open('money.csv','r')
file = csv.reader(f)    # csv파일 읽어오기
value = list(file)
print(value)
data = np.array(value,dtype='f')    # csv파일 데이터 타입을 float형으로 바꾸었다.

x = data[:, 0]      # x값에 몸무게를 대입
y = data[:, 1]      # y값에 몸무게를 대입
print(x)
print(y)

w = np.random.uniform(low=1, high=10)
b = np.random.uniform(low=0, high=10)
print('w: ', w, 'b: ', b)

y_hat = w * x + b

error = (y_hat - y) ** 2
print('error: ', error)
print('shape: ', error.shape)

cost = error.mean()
print('cost: ', cost)

w = 4.79174
b = 0.30931
org_x = np.linspace(0, 420, 100)
pred_x = org_x / 100  # 정규화
pred_y = w * pred_x + b
pred_y = pred_y * 100 # 정규화 반대 과정


x = 8.9 # True : 74
y_predict = x / 100 * w + b
print(y_predict * 100)

x = 7.9 # True : 67.6
y_predict = x / 100 * w + b
print(y_predict * 100)

x = 8.5 # True : 71.5
y_predict = x / 100 * w + b
print(y_predict * 100)

x = 11 # True: 82.4
y_predict = x / 100 * w + b
print(y_predict * 100)

