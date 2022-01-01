arr = []
g_num = []
def dfs(level, answer, target):
    if level == len(arr):
        #print(arr, target[0])
        tans = 0
        idx = 0
        for x in arr:
            if x == 0:
                tans+= g_num[idx]
            else:
                tans-= g_num[idx]
            idx += 1
        if tans == target[0]:
            answer[0] += 1
        #print(tans)
    else :
        arr[level] = 0
        dfs(level + 1, answer, target)
        arr[level] = 1
        dfs(level + 1, answer, target)

def solution(numbers, ttarget):
    target = [ttarget]
    answer = [0]
    for _ in numbers:
        arr.append(0)
    for x in numbers:
        g_num.append(x)
    dfs(0, answer, target)
    return answer[0]