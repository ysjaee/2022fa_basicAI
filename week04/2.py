file = open("C:/2th_Grade/AI_basic/week04/list.txt",'r',encoding='utf-8')
x = file.readlines()
a=[]
ma = 0  # max_a
for i in range(0,len(x)):
    x[i]=x[i].replace("\n","")
    a.append(int(x[i]))
print("max:",max(a))
print("min:",min(a))