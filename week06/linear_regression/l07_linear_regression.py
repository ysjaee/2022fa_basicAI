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

w = 4.13194
b = 0.35780
org_x = np.linspace(0, 420, 100)
pred_x = org_x / 100  # 정규화
pred_y = w * pred_x + b
pred_y = pred_y * 100 # 정규화 반대 과정

plt.scatter(x, y)
plt.title("baby's height and weight")
plt.xlabel("baby weight (kg)")
plt.ylabel("baby height (cm)")
plt.plot(org_x, pred_y)
plt.axis([0, 12, 0, 100])
plt.show()
