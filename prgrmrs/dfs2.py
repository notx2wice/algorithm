def dfs(now, computers, visited):
    if visited[now] == 0:
        return
    visited[now] = 0
    idx = 0
    for link in computers[now]:
        if link:
            dfs(idx, computers, visited)
        idx += 1

def solution(n, computers):
    answer = 0
    visited = [ 1 ] * n
    for x in range(n):
        if visited[x]:
            answer += 1
            dfs(x,computers, visited)
    return answer

n = 3
computers = [[1, 1, 0],
             [1, 1, 0],
             [0, 0, 1]]

print(solution(n, computers))