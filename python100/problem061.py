#문자열을 입력받고 연속되는 문자열을 압축해서 표현하고 싶습니다.

num = input()
s = ''
storeString = num[0]
count = 0
for i in num:
    if i == storeString:
        count += 1
    else:
        s += str(count) + storeString
        storeString = i
        count = 1
s += str(count) + storeString
print(s)
