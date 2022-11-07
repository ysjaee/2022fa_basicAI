# 다음을 출력하기
# 별 1개씩 추가하기 (1,2,3,4,5까지)

for i in range(1,6):
    print("*"*i)


# 1부터  1000까지의 자연수 중 3의 배수의 총합
result = 0
for i in range(1,1001):
    if i % 3 == 0:
        result = result + i
print(result)
