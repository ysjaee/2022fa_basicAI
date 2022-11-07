x = input()
x = x.split(" ")

if x[2] == "+":
    result = int(x[0]) + int(x[1])
elif x[2] == "-":
    result = int(x[0]) - int(x[1])
elif x[2] == "*":
    result = int(x[0]) * int(x[1])
elif x[2] == "/":
    result = int(x[0]) / int(x[1])
print(result)