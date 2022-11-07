'''
빈 종이에 stamp 모양으로 생긴 도장을 90*k 도로 회전하며 찍습니다.
도장은 N*N 크기이며 각 도장이 찍히는 부분은 1이상의 자연수와 도장이 찍히지 않는 0으로 이루어져 있습니다.

도장의 크기 N과,
종이에 찍힌 도장 횟수를 표현한 stmp배열과,
얼만큼 회전할 것인지를 알려주는 회전수 k를 입력받았을 때
각 위치에서 몇 번 도장이 찍혔는지 그 결과값을 출력하세요
'''

N = int(input())
stmp = []
for i in range(N):
    stmp.append(list(map(int, input().split(' '))))
k = int(input())


def solution(stmp, n):
    N = len(stmp)
    p = [[0] * N for _ in range(N)]
    p = sum_matrix(p, stmp)
    for i in range(n):
        stmp = rotate(stmp)
        p = sum_matrix(p, stmp)
    return p

def rotate(stmp):
    N = len(stmp)
    rot = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rot[j][N - 1 - i] = stmp[i][j]
    return rot

def sum_matrix(p, stmp):
    for i in range(len(p)):
        for j in range(len(p[0])):
            p[i][j] = p[i][j] + stmp[i][j]
    return p

print(solution(stmp, k))