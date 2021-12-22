#!/usr/bin/python3
#규칙 개수가 최대 만개 -> 한번 계산 에 10000번 * log번 계산 쌉가능
# 4, 10, 2 
# 4, 10, 3
# 200 2 4
# 200 2 5 
# 100 150 10
# 110 150 15
# 100 110 110 120 125
import sys, math
sys.setrecursionlimit(10**5)

def cal(num, rules):
    ans , flag = 0, 0
    
    for r in rules:
        if r[0] > num :
            continue
        if r[1] >= num:
            ans += ( (num - r[0]) // r[2]  ) + 1
            if (num - r[0]) % r[2] == 0:
                flag += 1
        else:
            ans += ( (r[1] - r[0]) // r[2] ) + 1
        
    if flag :
        return ans - flag + 1, ans, flag
    else :
        return ans , ans , flag
     
   

# cal의 리턴과 
def b_search_min(left, right, D, rules):
    print(left, right)
    mid = (left + right)// 2
    min, max , real = cal(mid, rules)
    print(min, max, real, mid)
    if min <= D <=max and real > 0:
        return mid
    elif min <= D <= max and real == 0:
        return b_search_min(left, mid, D, rules)
    elif max < D :
        return b_search_min(mid+1, right, D, rules)
    else:
        return b_search_min(left, mid -1, D, rules)


N, K, D = map(int, input().split())

rules =[]
for _ in range(K): 
    a, b, c = map(int, input().split())
    rules.append([a,b,c])

print(b_search_min(1, N, D, rules))

