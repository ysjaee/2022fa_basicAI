# 입력을 한 줄로 받기 (두 수와 연산자 순으로)
a = input()
a = a.split()
result = 1
if a[2] == "+":
    result = int(a[0]) + int(a[1])
elif a[2] == "-":
    result = int(a[0]) -int(a[1])
elif a[2] == "*":
    result = int(a[0]) * int(a[1])
elif a[2] == "/":
    result = int(a[0]) / int(a[1])
print(result)