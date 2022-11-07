import numpy as np
import csv
from matplotlib import pyplot as plt

f = open('money.csv','r')
file = csv.reader(f)    # csv파일 읽어오기
value = list(file)
data = np.array(value,dtype='f')    # csv파일 데이터 타입을 float형으로 바꾸었다.
x = data[:, 0]      # x값에 몸무게를 대입
y = data[:, 1]      # y값에 몸무게를 대입

x = data[:, 0]
y = data[:, 1]

w = np.random.uniform(low=1, high=10)
b = np.random.uniform(low=0, high=10)
print('w: ', w, 'b: ', b)

y_hat = w * x + b

error = (y_hat - y) ** 2
print('error: ', error)
print('shape: ', error.shape)

cost = error.mean()
print('cost: ', cost)