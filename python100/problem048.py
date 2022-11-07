'''
문자열이 주어지면 대문자와 소문자를 바꿔서 출력하는 프로그램을 작성하세요.
'''

a = input()
b = []

for i in a:
    if i.islower():
        b.append(i.upper())
    else:
        b.append(i.lower())

for i in b:
    print(i, end='')