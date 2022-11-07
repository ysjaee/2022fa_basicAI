# 신생아 표준 몸무게 와 키의 관계 (0개월부터 12월까지)
# 신생아 표준 몸무게 와 키의 관계 (0개월부터 12월까지)
import numpy as np
from matplotlib import pyplot as plt
import csv

f = open('money.csv','r')
file = csv.reader(f)    # csv파일 읽어오기
value = list(file)
data = np.array(value,dtype='f')    # csv파일 데이터 타입을 float형으로 바꾸었다.

x = data[:, 0]/100
y = data[:, 1]/100

num_epoch = 3000000              # w,b를 최대한 정확히 찾기 위해 10만번으로 설정

# 학습율 (learning_rate)
learning_rate = 0.01

costs = []

w = np.random.uniform(low=1, high=10)
b = np.random.uniform(low=0, high=10)
print('w: ', w, 'b: ', b)

for epoch in range(num_epoch):
    y_hat = w * x + b

    error = ((y_hat - y)**2)
    cost = error.mean()

    if cost < 0.00002:               # 10만번을 돌리면서 error의 값을 최소화 하기 위해
        break

    w = w - learning_rate * ((y_hat - y) * x).mean()
    b = b - learning_rate * (y_hat - y).mean()

    costs.append(cost)

    if epoch % 10 == 0:
        print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(
            epoch, w, b, cost))

print("----" * 15)
print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(epoch, w, b, cost))


plt.figure(figsize=(10, 7))
plt.plot(costs)
plt.xlabel('Epochs')
plt.ylabel('Costs')
plt.show()