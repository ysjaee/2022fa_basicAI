import math
def f(x):
    result = (1/(1+math.exp(-x)))*(1-1/(1+math.exp(-x)))
    return result

x = int(input())
print(f(x))
