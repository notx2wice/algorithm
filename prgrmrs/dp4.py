'''
각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.
각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 
solution 함수를 작성하세요.

이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.
'''
import sys
limit_number = 10**9
sys.setrecursionlimit(limit_number)

def dfs(start, n,dp, money):
    if n == start:
        dp[start] = money[n]
        return dp[n]
    if n == start + 1:
        dp[start + 1] = max(money[start], money[start + 1])
        return dp[start + 1]
    if dp[n] > 0:
        return dp[n]
    else :
        dp[n] = max( dfs(start,n-2, dp, money) + money[n] ,dfs(start,n-1, dp, money) )
        return dp[n]

def solution(money):
    dp = [0] * 1000001
    answer1 = dfs(0, len(money) - 2, dp, money)
    dp = [0] * 1000001
    answer2 = dfs(1,len(money) - 1, dp, money)

    return max(answer1, answer2)
    
money = [x for x in range(100000)]

print(solution(money))
'''
def solution(money): 
    dp1 = [0] * len(money) 
    dp2 = [0] * len(money) 
    # 1번 집을 터는 경우 
    dp1[0] = money[0] 
    for i in range(1, len(money) - 1): 
    # # 마지막 집은 털지 못함
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i]) 
        # 1번 집을 안터는 경우 
    dp2[0] = 0 
    for i in range(1, len(money)): 
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i]) 
    return max(dp1[-2], dp2[-1])

import sys
limit_number = 10000000
sys.setrecursionlimit(limit_number)

def get_money(dp, money, st, ed):
    if ed < st:
        return 0
    if st == ed:
        return money[st]
    if dp[st] != -1:
        return dp[st]
    dp[st] = max(get_money(dp, money, st+3, ed)+money[st+1], get_money(dp, money, st+2, ed)+money[st])
    return dp[st]


def solution(money):
    dp = [-1]*1000000
    anwser = get_money(dp, money, 1, len(money)-1)
    dp = [-1]*1000000
    anwser = max(anwser, get_money(dp, money, 2, len(money)-2)+ money[0])
    return anwser
'''