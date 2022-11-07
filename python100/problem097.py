'''
n명의 택배 배달원은 쌓인 택배를 배달해야 합니다.
각 택배는 접수된 순서로 배달이 되며 택배 마다 거리가 주어집니다.
거리1당 1의 시간이 걸린다고 가정하였을 때 모든 택배가 배달 완료될 시간을 구하세요.

1. 모든 택배의 배송 시간 1 이상이며 배달지에 도착하고 돌아오는 왕복시간입니다.
2. 택배는 물류창고에서 출발합니다.
3. 배달을 완료하면 다시 물류창고로 돌아가 택배를 받습니다.
4. 물류창고로 돌아가 택배를 받으면 배달을 시작합니다.
5. 택배를 상차 할 때 시간은 걸리지 않습니다.

입력은 배달원의 수와 택배를 배달하는 배달 시간이 주어집니다.

ex) 배달원이 3명이고 각 거리가 [1,2,1,3,3,3]인 순서로 들어오는 경우

def solution(n,l):
	<코드 작성>


배달원 = 3
배달시간 = [1,2,1,3,3,3]


print(solution(배달원,배달시간))
# 출력값 = 5
'''

def sol(n,l):
    answer = 0
    man = [0]*n
    while sum(l)!=0:
        for j in range(len(man)):
            if man[j] == 0 and l:
                man[j]+=l.pop(0)
        man = list(map(lambda x : x-1,man))
        answer+=1
    answer += max(man)
    print(answer)

def solution(택배원의수, 택배거리):
    time = 0
    택배원택배거리 = [0] * 택배원의수
    while 택배거리:
        for i in range(택배원의수):
            if 택배원택배거리[i] == 0 and 택배거리:
                택배원택배거리[i] = 택배거리.pop(0)
        택배원택배거리 = list(map(lambda x: x-1, 택배원택배거리))
        time += 1
        print('------------')
        print(택배원택배거리, time)
    print('-----end while------')
    print(택배원택배거리, time)
    time += max(택배원택배거리)
    print(time)

배달원 = 3
택배 = [1,2,1,3,3,3]
택배원택배거리 = [0, 0, 0]

print(solution(배달원,택배))
