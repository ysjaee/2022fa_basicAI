f = open("C:/a/b.txt", mode="r", encoding="utf-8")
lines = f.readlines()

codes = []
for line in lines:
    code = line.strip()
    codes.append(code)

print(codes)
f.close()