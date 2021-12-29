'''
각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.
각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 
solution 함수를 작성하세요.

이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.
'''
def dfs(n, dp, money):
    if n == 0:
        return money[n]
    if n == 1:
        return max(money[0], money[1])
    if dp[n]:
        return dp[n]
    else :
        dp[n] = max(dfs(n-2, dp, money) + money[n] ,dfs(n-1, dp, money))
        return dp[n]

def solution(money):
    dp = [0 for _ in range(len(money))]
    dp1 = [0 for _ in range(len(money))]
    moneya = money[:-1]
    answer1 = dfs(len(moneya) - 1, dp, moneya)
    moneyb = money[1:]
    answer2 = dfs(len(moneyb) - 1, dp1, moneyb)
    # print(moneya, moneyb)
    # print(answer1, answer2)
    return max(answer1, answer2)
    
money = [x for x in range(1000000000)]

print(solution(money))