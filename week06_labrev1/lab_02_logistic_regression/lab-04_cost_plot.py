import numpy as np
from matplotlib import pyplot as plt

# Score
# 0 : Fail, 1 : Pass
data = np.array([
    [45, 0],
    [50, 0],
    [55, 0],
    [60, 1],
    [65, 1],
    [70, 1]
])

x = data[:, 0] / 100            # /100은 정규화 미분할때 미분값이 크면 잘 학습이 안되서 일부러 줄임
# x = data[:, 0]
y = data[:, 1]


def sigmoid(x):  # 시그모이드 함수 정의
    return 1/(1+np.exp(-x))

w = np.random.uniform(low=0, high=20)
b = np.random.uniform(low=-20, high=10)
print('w: ', w, 'b: ', b)

num_epoch = 500000   # 50만 돌리기
learning_rate = 100 #괴장히 빠르게 학습을 할려면 키워줘야 된다.
costs = []
eps = 1e-5

for epoch in range(num_epoch):
    hypothesis = sigmoid(w * x + b)

    cost = y * np.log(hypothesis + eps) + (1 - y) * np.log(1 - hypothesis + eps)
    # eps값을 넣은 것은 log(0)의 값을 방지하기 위해 조금이라도 작은 값을 넣어준 것
    cost = -1 * cost
    cost = cost.mean()

    if cost < 0.00005:
        break

    w = w - learning_rate * ((hypothesis - y) * x).mean()
    b = b - learning_rate * (hypothesis - y).mean()

    costs.append(cost)

    if epoch % 50 == 0:
        print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(
            epoch, w, b, cost))

print("----" * 15)
print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(epoch, w, b, cost))

plt.figure(figsize=(10, 7))
plt.plot(costs)
plt.xlabel('Epochs')
plt.ylabel('Costs')
plt.show()

# learning rate는 경험치로 하는 것
