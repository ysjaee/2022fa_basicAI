import sys

file = open("input.csv")
data = file.readlines()
x = []
name = data.pop(0)
print(name)
avg = 0
sum = 0
total = []
result = []
res = []
a = []
for line in data:
    x = line.split(',')
    sum = float(x[1])+float(x[2])+float(x[3])
    avg = sum/3
    total.append(sum)
    result.append(avg)

for line in data:
    for i in range(0,len(data)):
        line.split('\n')
        res = line + "," +str(total[i])+','+str(result[i])
        a.append(res)
print(a)


