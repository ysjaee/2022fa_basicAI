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

print(x)
print(y)
print(x.shape)
print(y.shape)
# 전체 csv파일 그래프로 만드는 법
csv = pd.read_csv('wine.csv')
sns.pairplot(csv, hue='#Wine')
plt.show()
