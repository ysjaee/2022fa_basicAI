import numpy as np
from matplotlib import pyplot as plt
import csv
import seaborn as sns
import pandas as pd
f=[]
file = open('wine.csv', 'r', encoding='UTF-8')
f_data = csv.reader(file)

for i in f_data:
   f.append(i)
data = np.array(f)

x = np.array(data[1:, 1:], dtype=np.float16)  # 와인 정보 뽑아내기
y = np.array(data[1:, 0], dtype=np.float16)   # 정답
# 2. 선택
# # 정규화 방법
x_max = x.max(axis=0)
x_normal = x / x_max
label = []

for wine in y:
    if wine == 1:
        label.append(0)
    if wine == 2:
        label.append(1)
    if wine == 3:
        label.append(2)

num = np.unique(label, axis=0)
num = num.shape[0]

encoding = np.eye(num)[label]
print(encoding.shape)
encoding_y = encoding.copy()
dim = 13
nb_classes = 3
#x shape:  (178, 13) y shape:  (178,)

w = np.random.normal(size=[dim, nb_classes])
b = np.random.normal(size=[nb_classes])
#w shape:  (13, 3) b shape:  (3,)

def cross_entropy_error(predict, target):
    delta = 1e-7
    return -np.mean(target * np.log(predict + delta))

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T
    else:
        c = np.max(x)
        exp_a = np.exp(x-c)
        sum_exp_a = np.sum(exp_a)
        y = exp_a / sum_exp_a
        return y

hypothesis = softmax(np.dot(x_normal, w) + b)
print('hypothesis: ', hypothesis.shape)

eps = 1e-7
cost = encoding_y * np.log(hypothesis + eps)
cost = -cost.mean()
print('cost: ', cost)

learning_rate = 100000
costs = []

m, n = x_normal.shape
c = 0
while True:
    c += 1
    z = np.dot(x_normal, w) + b
    hypothesis = softmax(z)
    cost = encoding_y * np.log(hypothesis + eps)
    cost = -cost.mean()
    if cost < 0.0001:
        break
    w_grad = (1/m)*np.dot(x_normal.T, (hypothesis - encoding_y))
    b_grad = (1/m)*np.sum(hypothesis - encoding_y)

    w = w - learning_rate * w_grad
    b = b - learning_rate * b_grad
    costs.append(cost)
plt.figure(figsize=(10, 7))
plt.plot(costs)
plt.xlabel('Epochs')
plt.ylabel('Costs')
plt.show()

#예측 (10,000번)
success_cnt = 0
for i in range(10000):
    random_num = np.random.randint(0, len(x_normal)-1)
    x1 = x_normal[random_num]
    t = np.dot(x1, w) + b
    z = softmax(t)
    print('t: ', t, 'z: ', z)
    prediction = np.argmax(z) #수 내에 array와 비슷한 형태(리스트 등 포함)의 input을 넣어주면 가장 큰 원소의 인덱스를 반환
    print('prediction: ', prediction)
    print('label: ', encoding_y[random_num])
    print('@@@@' * 20)
    if prediction == np.argmax(encoding_y[random_num]):
        success_cnt += 1
        print('success')
    else:
        print('fail')

print('----' * 30)
print('The End')
print('정확도: %.2f' %((success_cnt/10000)*100), '%')
