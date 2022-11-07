'''
지식이는 게임을 만드는 것을 좋아합니다. 하지만 매번 다른 크기의 지도와 장애물을 배치하는데 불편함을 겪고있습니다. 이런 불편함을 해결하기 위해 지도의 크기와 장애물의 위치, 캐릭터의 위치만 입력하면 게임 지형을 완성해주는 프로그램을 만들고 싶습니다.  지식이를 위해 게임 지형을 만드는 프로그램을 작성해 주세요

가로:n /세로:m 크기가 주어집니다.
지형의 테두리는 벽으로 이루어져 있습니다.
캐릭터가 있는 좌표가 배열형태로 주어집니다.
장애물이 있는 좌표가 2차원 배열 형태로 주어집니다.
지도는 n x m 크기의 배열이며 배열안의 값은
   -움직일수 있는 공간(0)
   -캐릭터(1)
   -벽(2)
3개로 구분되어 있습니다.
'''

def make_map(n,m,char,obj):
    world_map = [[0]*(n+2) for i in range(m+2)]
    for i in range(len(world_map)):
        for j in range(len(world_map[0])):
            if i==0 or j==len(world_map[0])-1 or j==0 or i ==len(world_map)-1:
                world_map[i][j]=2
    world_map[char[0]+1][char[1]+1] = 1
    for i in obj:
        world_map[i[0]+1][i[1]+1] = 2 if world_map[i[0]+1][i[1]+1] != 1 else 1
    for i in world_map:
        print(i)