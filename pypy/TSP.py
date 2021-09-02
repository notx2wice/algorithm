#!/usr/bin/python3
N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
dp_table = [[-1 for _ in range(1<<N)] for _ in range(N)]

def dp(current, visited):
    ret = dp_table[current][visited]
    if ret != -1:
        return ret
    if visited == (1<<N)-1: # 모두 방문한경우 
        if G[current][0] != 0: # 0으로 돌아갈 길이 있다면 
            return G[current][0] 
        return 200000000
    ret = 200000000
    for i in range(N):
        if visited & (1<<i) or G[current][i] == 0: 
            continue #방문 했었거나 현재에서 도달할수 있는 길이 없다면
        ret = min(ret, dp(i, visited|(1<<i)) + G[current][i])
    dp_table[current][visited] = ret
    return ret

print(dp(0,1))