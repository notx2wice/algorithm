
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

visited = [[1 for _ in range(n) ] for _ in range(n)]

def dfs(x, y):
    

def solution(n, computers):
    answer = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                dfs(x, y)
    return answer

print(solution(n, computers))