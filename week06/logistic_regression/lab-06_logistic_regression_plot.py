import numpy as np
from matplotlib import pyplot as plt
import csv
# 시속 단속
f = open('input.csv','r')
file = csv.reader(f)    # csv파일 읽어오기
value = list(file)
data = np.array(value[1:],dtype='f')
# text file input/output

# x = data[:, 0] / 80
x = data[:, 0]
y = data[:, 1]

def sigmoid(x):  # 시그모이드 함수 정의
    return 1/(1+np.exp(-x))

w = np.random.uniform(low=0, high=20)
b = np.random.uniform(low=-20, high=10)
print('w: ', w, 'b: ', b)

num_epoch = 100000

learning_rate = 100

costs = []

eps = 1e-5

for epoch in range(num_epoch):
    hypothesis = sigmoid(w * x + b)

    cost = y * np.log(hypothesis + eps) + (1 - y) * np.log(1 - hypothesis + eps)
    cost = -1 * cost
    cost = cost.mean()

    if cost < 0.0005:
        break
    w = w - learning_rate * ((hypothesis - y) * x).mean()
    b = b - learning_rate * (hypothesis - y).mean()

    costs.append(cost)

    if epoch % 5000 == 0:
        print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(
            epoch, w, b, cost))

print("----" * 15)
print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(epoch, w, b, cost))


# 예측
w = -64.08008
b = 61.39749
x = 45 # True : 0
x = x / 80
pred_y = sigmoid(w * x + b)
print(pred_y)

x = 60 # True : 1
x = x / 80
pred_y = sigmoid(w * x + b)
print(pred_y)

x = data[:, 0]
y = data[:, 1]

org_x = np.linspace(0, 200, 10)
pred_y = sigmoid(w * (org_x / 80) + b)

plt.scatter(x, y) 
plt.title("Pay/Fail vs km/h")
plt.xlabel("km/h")
plt.ylabel("Pay/Fail")
plt.plot(org_x, pred_y, 'r')
# plt.axis([0, 420, 0, 50])
plt.show()