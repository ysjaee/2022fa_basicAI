'''
사용자가 입력한 양의 정수의 각 자리수의 합을 구하는 프로그램을 만들어주세요
'''

n = list(map(int, input()))
result = 0
for i in n:
    result += i

print(result)