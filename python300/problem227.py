def printmxn(str,num):
    line_num = int(len(str)/num)
    for x in range(line_num+1):
        print(str[x * num : x * num+num])
printmxn("아이엠어보이유알어걸", 3)