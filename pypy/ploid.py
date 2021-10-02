import sys
n = (int)(input())
m = (int)(input())
dp = [ [ 10000000000 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a ,b, c = map(int, input().split())
    if c < dp[a][b]:
        dp[a][b] = c

for t in range(1, n+1):
    dp[t][t] = 0

for mid in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if dp[x][y] > dp[x][mid] + dp[mid][y]:
                dp[x][y] = dp[x][mid] + dp[mid][y]

for x in range( 1, n+ 1):
    for y in range(1, n+ 1):
        if dp[x][y] >= 10000000000:
            print(0 ,end= " ")
        else:
            print(dp[x][y], end=" ")
    print()
