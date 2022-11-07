x = input('입력:')
x = x.split(' ')

def func(x):
    if x[2] =='+':
        result = int(x[0]) + int(x[1])
    elif x[2] =='-':
        result = int(x[0]) - int(x[1])
    elif x[2] =='*':
        result = int(x[0]) * int(x[1])
    elif x[2] == '/':
        result = int(x[0]) / int(x[1])
    elif x[2] == '%':
        result = int(x[0]) % int(x[1])
    print(result)

func(x)