# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
from collections import deque

def solution(prices):

    answer = [ -1] * len(prices)
    dq = deque()
    time = 0

    while time < len(prices):
        if len(dq) == 0:
            dq.append([prices[time], time])
        elif dq[-1][0] <= prices[time]:
            dq.append([prices[time], time])
        else:
            while len(dq) and dq[-1][0] > prices[time]:
                t = dq.pop()
                answer[t[1]] = time - t[1]
            dq.append([prices[time], time])
        time += 1
    while dq:
        t = dq.pop()
        answer[t[1]] = len(prices) - t[1] - 1
    return answer

prices = [1, 2, 3, 2, 3]	#	return [4, 3, 1, 1, 0]
print(solution(prices))