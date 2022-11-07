import math
def function(x):
    fx = 1 / (1+math.exp(-x))
    result = fx*(1-fx)
    print(result)

num = int(input())
function(num)