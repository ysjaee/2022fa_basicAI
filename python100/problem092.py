'''
P회사 회계를 처리하던 은정은 커피를 마시다가 키보드에 커피를 쏟고 말았습니다.
휴지로 닦고 말려보았지만 숫자 3, 4, 6이 도통 눌리지 않습니다.
10분 뒤, 모든 직원들에게 월급을 입금해주어야 합니다.
여유 키보드는 없으며, 프로그래밍을 매우 잘하고, 모든 작업을 수작업(?)으로 하고 있습니다.

이에 눌리지 않는 키보드를 누르지 않고 월급 입금을 두 번에 나눠주고 싶습니다.

1. 직원은 2000명이며, 3초 이내 수행을 해야합니다.
2. 입력값의 형식은 csv파일이며 이과장 '3,000,000', 'S은행', '100-0000-0000-000' 형식으로 주어집니다.
3. 출력값의 형식은 csv 파일이며 이과장 '1,500,000', '1,500,000', 'S은행', '100-0000-0000-000' 입니다. 또는 '1,000,000', '2,000,000', 'S은행', '100-0000-0000-000' 도 괜찮습니다.
4. 라이브러리 사용할 수 있습니다.
'''

import csv

f = open('test.csv', 'r', encoding='utf-8')
r = csv.reader(f)
for line in r:
    s1, s2 = '', ''
    for i in line[1].replace(',', ''):
        if i == '3':
            s1 += '1'
            s2 += '2'
        elif i == '4':
            s1 += '2'
            s2 += '2'
        elif i == '6':
            s1 += '1'
            s2 += '5'
        else:
            s1 += i
            s2 += '0'
    print(int(s1), int(s2))