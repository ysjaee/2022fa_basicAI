'''
쉔은 회전초밥집에 갔습니다.
초밥집에 간 쉔은 각 초밥에 점수를 매기고 낮은 점수의 순서로 초밥을 먹으려 합니다.
이때 n위치에 놓여진 초밥을 쉔은 접시가 몇 번 지나가고 나서 먹을지 출력하세요.

1. 초밥은 놓여진 위치에서 옮겨지지 않습니다.
2. 지나간 초밥은 나머지 초밥이 지나간 후에 다시 돌아옵니다.
3. 초밥은 1개 이상 존재합니다.

예:
A, B, C, D, E 초밥이 있고 각 점수가 1, 1, 3, 2, 5 일 때 3번째(C초밥)을 먹게 되는 순서는
1인 초밥 A와 B를 먹고 다음 2인 D 초밥을 먹어야 됩니다.
A B C D E 의 순서로 접시가 도착하지만 C가 도착했을때 먹지 못하는 상황이 옵니다.
2점을 주었던 D를 먼저 먹어야 C를 먹을 수 있습니다.
즉, A B C D E C , 접시가 5번 지나가고 먹게 된다.
'''
def solution(point, dish):
    dish -=1
    answer = 0
    s = sorted(point)
    while True:
        p = point.pop(0)

        if s[0]==p:
            if dish == 0:
                break
            dish-=1
            s.pop(0)
        else:
            point.append(p)
            dish = len(point)-1 if dish==0 else dish-1
        answer+=1
    print(answer)
point = [1,1,3,2,5]
dish = 3
solution(point,dish)