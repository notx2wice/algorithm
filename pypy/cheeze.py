#!/usr/bin/python3
from collections import deque

def check_range(x, y):
    if x < 0 or x >= r or y <0 or y >=c :
        return 0
    return 1

def count_cheeze( map_info , r, c):
    count = 0
    for x in range(r):
        for y in range(c):
            if map_info[x][y] == 1:
                count += 1
    return count

r, c = map(int, input().split())

visited = [ [0 for _  in range(c)] for _ in range(r)]
cz = []
cz_hour = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dq1 = deque()
dq0 = deque()

for _ in range(r):
    cz.append(list(map(int, input().split())))


dq0.append([0,0])
while ( count_cheeze(cz, r, c) ) :
    #치즈 값을 저장 해두기
    bf_cheeze = count_cheeze(cz, r, c)
    #공기랑 닿은 치즈 녹이기
    while dq0:
        node = dq0.pop() #외각의 0 탐색하기 
        visited[node[0]][node[1]] = 1
        tx = 0
        ty = 0
        for t in range(4):
            tx = node[0] + dx[t]
            ty = node[1] + dy[t]
            if check_range(tx, ty) and visited[tx][ty] == 0 :
                if cz[tx][ty] == 1:
                    dq1.append([tx,ty])
                else:
                    dq0.append([tx, ty])
    for tnode in dq1:
        cz[tnode[0]][tnode[1]] = 0
        dq0.append(tnode)
    # print() #맵 출력 로직
    # for tt in range(r):
    #     print(cz[tt])
    dq1.clear()
    #시간 증가.
    cz_hour += 1

print(cz_hour)
print(bf_cheeze)
