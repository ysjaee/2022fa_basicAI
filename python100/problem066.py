'''
탑을 쌓기 위해 각 크기별로 준비된 블럭들을 정해진 순서에 맞게 쌓아햐 합니다.
순서에 맞게 쌓지 않으면 무너질 수 있습니다.
예를 들면 정해진 순서가 BAC 라면 A 다음 C가 쌓아져야 합니다.
선행으로 쌓아야 하는 블럭이 만족된 경우라면 탑이 무너지지 않습니다.

- B를 쌓지 않아도 A와 C를 쌓을 수 있습니다.
- B 다음 블럭이 C가 될 수 있습니다.

쌓아져 있는 블럭 탑이 순서에 맞게 쌓아져 있는지 확인하세요.

1. 블럭은 알파벳 대문자로 표기합니다.
2. 규칙에 없는 블럭이 사용될 수 있습니다.
3. 중복된 블럭은 존재하지 않습니다.
입력
탑 = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
규칙 = "ABD"

출력
["가능","불가능","가능","가능]
'''

def solution(ab, 규칙):
    answer = []
    for bp in ab:
        answer.append(rc(bp, 규칙))
    return answer

def rc(bp, 규칙):
    임시변수 = 규칙.index(규칙[0])
    for 문자 in bp:
        if 문자 in 규칙:
            if 임시변수 > 규칙.index(문자):
                return '불가능'
            임시변수 = 규칙.index(문자)
    return '가능'

ab = ['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG', 'AEBFDGCH']
규칙 = 'ABCD'

print(solution(ab, 규칙))
