# n이 짝수 n이 홀수 일때 첫 무브가 다름.
# n == 1 :: [[1,3]]
# n == 2 :: [[1,2], [1,3], [2,3]]
# n == 3 :: [[1,3], [1,2],[3,2],[1,3],[2,1],[2,3],[1,3]]

def f(x):
    if x == 2:
        return 3
    elif x == 3:
        return 2
    else: 
        return x

def l(x):
    return x % 3 + 1

def solution(n):
    answer = [1,3]
    idx = 1

    while idx < n :
        # 3->2 , 2->3
        fans =list( map( f , answer) )
        tans = list(map(l, fans))
        # add [1,3]
        fans.append(1)
        fans.append(3)
        # x -> x + 1 % 3 , y -> y + 1 % 3
        answer = fans + tans
        idx += 1
    
    al = len(answer) //2
    real_answer = [[] for _ in range(al)]
    for x in range(al):
        real_answer[x].append(answer[2*x])
        real_answer[x].append(answer[2*x + 1])

    return real_answer
#[[1,3], [1,2],[3,2],[1,3],[2,1],[2,3],[1,3]]
print(solution(3)) 