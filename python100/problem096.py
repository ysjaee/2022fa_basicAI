'''
수연이는 밭 농사를 시작하기로 마음을 먹었다. 집 앞 텃밭을 만들기로 하고 돌들을 제거하고 있는데 매우 큰 바위는 옮기지 못해 고심하고 있다.

이에 수연이는 다음과 같은 규칙을 정한다.

1. 바위를(바위는 '1'로 표기한다.) 피해 텃밭을 만들되 정사각형 모양으로 텃밭을 만든다.
2. 텃밭은 가장 넓은 텃밭 1개만 만들고 그 크기를 반환한다.
3. 만든 텃밭은 모두 '#'으로 처리한다.
## 문제 ##
텃밭 = [] #입력받은 텃밭 리스트
가꾼텃밭 = [] #텃밭을 가꾼 후 저장된 리스트
for i in range(5):
    텃밭.append(input('텃밭을 입력하세요 :').split(' '))

<코드를 작성해주세요>

print(가꾼텃밭)
'''
텃밭 = [[0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0]]
def solution(텃밭):
    넓이 = len(텃밭[0])
    높이 = len(텃밭)
    텃밭합 = [[0] * 넓이 for i in range(len(텃밭))]
    for i in range(0, 높이):
        for j in range(0, 넓이):
            if 텃밭[i][j] == 0:
                텃밭합[i][j] = 1
            else:
                텃밭합[i][j] = 0

    for i in range(1, 높이):
        for j in range(1, 넓이):
            if 텃밭합[i][j] == 1:
                텃밭합[i][j] = min(텃밭합[i - 1][j - 1], min(텃밭합[i - 1][j], 텃밭합[i][j - 1])) + 1

    maxValue = 0
    x = 0
    y = 0
    for i in range(0, 높이):
        for j in range(0, 넓이):
            if maxValue < 텃밭합[i][j]:
                maxValue = 텃밭합[i][j]
                x = i
                y = j

    print(maxValue, x, y)
    print(maxValue, 'X', maxValue)

    for i in range(x - (maxValue - 1), x + 1):
        for j in range(y - (maxValue - 1), y + 1):
            텃밭[i][j] = '#'

    print(텃밭)


solution(텃밭)