'''
1~9까지의 숫자 중 하나를 입력하면 그 단의 구구단 결과를 한 줄에 출력하는 프로그램을 작성하세요.
'''

a = int(input())
for i in range(1,10):
    print(a*i, end=' ')