import numpy as np
from matplotlib import pyplot as plt
import csv
# 시속 단속
f = open('input.csv','r')
file = csv.reader(f)    # csv파일 읽어오기
value = list(file)
data = np.array(value[1:])

# plt.plot(data[:, 0], data[:, 1])
plt.scatter(data[:, 0], data[:, 1])   # 점으로 데이터 표현
plt.title("fine Pay/Pass vs km/h")
plt.xlabel("km/h")
plt.ylabel("Pay/Pass")
plt.grid()

plt.show()

