x = open("input.txt","r",encoding = "utf-8")
xtxt = x.readlines()
xlist = []
for i in range(len(xtxt)):
    xlist.append(xtxt[i].split())
    if xlist[i][-1] == '+':
        print(int(xlist[i][0]) + int(xlist[i][1]))
    elif xlist[i][-1] == '-':
        print(int(xlist[i][0]) - int(xlist[i][1]))
    elif xlist[i][-1] == '*':
        print(int(xlist[i][0]) * int(xlist[i][1]))
    else:
        print(int(xlist[i][0]) / int(xlist[i][1]))