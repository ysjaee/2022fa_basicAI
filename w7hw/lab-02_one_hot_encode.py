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
print(encoding)
print(encoding.shape)
