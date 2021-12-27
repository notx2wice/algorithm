LIMIT = 1000000007

def dfs(x, y, dp):
    if dp[y][x] >= 0:
        return dp[y][x] % LIMIT
    else:
        dp[y][x] = (dfs( x-1, y, dp) % LIMIT + dfs( x, y-1, dp) % LIMIT ) % LIMIT
        return dp[y][x]

    
def solution(x, y, puddles):
    answer = 0

    dp = [[ -1 for _ in range(x)] for _ in range(y)]
    for p in puddles:
        dp[p[1] - 1][p[0] - 1] = 0
    flag = 1
    for idx in range(x):
        if dp[0][idx] == 0:
            flag = 0
        dp[0][idx] = flag
    flag = 1
    for idx in range(y):
        if dp[idx][0] == 0:
            flag = 0
        dp[idx][0] = flag
    
    for t in dp:
        print(t)
    print()
    
    return dfs(x - 1, y - 1,dp)
x = 4
y = 3
puddles = [[2,2]]
print(solution(x, y, puddles))