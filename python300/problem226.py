def print_5xn(line):
    num = int(len(line) / 5)
    for x in range(num + 1) :
        print(line[x * 5: x * 5 + 5])

print_5xn("아이엠어보이유알어걸")