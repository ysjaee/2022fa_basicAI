f = open("C:/a/b.txt", mode="r", encoding="utf-8")
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip()
    k, v = line.split()
    data[k] = v

print(data)
f.close()