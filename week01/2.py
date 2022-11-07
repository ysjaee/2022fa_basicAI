# sin(x)의 함수의 미분을 함수로 정의
# x값을 입력으로 주어졌을 때 미분 값을 출력하는 프로그램을 작성하시오.

import math
result = 0
def der(x):
    return math.cos(x)
print("sin(0)의 미분은",der(0))
print("sin(PI/2)의 미분은",der(math.pi/2))
