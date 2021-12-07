#!/usr/bin/python3
#규칙 개수가 최대 만개 -> 한번 계산 에 10000번 * log번 계산 쌉가능
# 4, 10, 2 
# 4, 10, 3
import sys
sys.setrecursionlimit(10**5)

def cal(num, rules):
    sum = 0
    max = 0
    for rule in rules:
        if rule[0] > num :
            continue
        if rule[1] <= num :
            sum = sum + ((rule[1] - rule[0]) // rule[2])
            if (rule[1] - rule[0]) % rule[2] == 0:
                max += 1
        else :
            sum = sum + ((num - rule[0]) // rule[2])
            if (num - rule[0]) % rule[2] == 0:
                max += 1
    
    if max > 0 :
        min = sum + 1
    else:
        min = sum
    return min , sum + max

# cal의 리턴과 
def b_search_min(left, right, D, rules):
    if left == right:
        if cal(left, rules) == D:
            return left
        
    mid = (left + right)// 2
    min, max = cal(mid, rules)
    if min <= D <=max:
        return mid
    else :
        return b_search_min(mid+1, right, D, rules)


N, K, D = map(int, input().split())
# print(N, K, D)
rules =[]
for _ in range(K): 
    a, b, c = map(int, input().split())
    rules.append([a,b,c])

print(b_search_min(1, N, D, rules))

