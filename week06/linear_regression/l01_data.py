# 신생아 표준 몸무게 와 키의 관계 (0개월부터 12월까지)
import numpy as np
from matplotlib import pyplot as plt
import csv

f = open('money.csv','r')
file = csv.reader(f)    # csv파일 읽어오기
value = list(file)
data = np.array(value,dtype='f')    # csv파일 데이터 타입을 float형으로 바꾸었다.
x = data[:, 0]      # x값에 몸무게를 대입
y = data[:, 1]      # y값에 몸무게를 대입

plt.scatter(data[:, 0], data[:, 1])
plt.title("cm / kg")
plt.xlabel("baby weight (kg)")
plt.ylabel("baby height (cm)")
plt.axis([0,12,0,100])
plt.show()
