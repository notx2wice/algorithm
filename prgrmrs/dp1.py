# 문제 설명
# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5

# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다. x**8일듯 대충 쌉가능?

check = [ 2147483647 for _ in range(32001)]

can = set()
def rangeCheck(a):
    if a >= 1 and a <= 32000:
        return True
    return False

def solution(N, number):
    answer = 0
    idx = 1
    sum = 0
    while idx <= 5:
        sum *= 10
        sum += N
        if sum < 32001:
            check[sum] = idx
            can.add(sum)
        idx += 1

    maded = [ x for x in can]

    for _ in range(8):
        idx = 0
        rr = len(maded)
        for t in maded:
            can.add(t)
        while idx < rr:
            for acan in can:
                x = acan
                y = maded[idx]
                adds = check[ x ] + check[ y]
                if adds > 8 :
                    continue
                if (rangeCheck( x + y) and check[x+y] > adds):
                    if check[ x + y] == 2147483647:
                        maded.append(x+y)
                    check[x+y] = adds
                    
                if (rangeCheck( x * y) and check[x*y] > adds):
                    if check[ x * y] == 2147483647:
                        maded.append(x*y)
                    check[x*y] = adds

                if (rangeCheck( x - y) and check[x - y] > adds):
                    if check[ x - y] == 2147483647:
                        maded.append(x-y)
                    check[x-y] = adds

                if (rangeCheck( y - x) and check[y - x] > adds):
                    if check[ y - x] == 2147483647:
                        maded.append(y-x)
                    check[y-x] = adds
        
                if (y != 0 and rangeCheck( x // y) and check[x // y] > adds):
                    if check[ x // y] == 2147483647:
                        maded.append(x // y)
                    check[x//y] = adds

                if (x != 0 and rangeCheck( y // x) and check[y // x] > adds):
                    if check[ y // x] == 2147483647:
                        maded.append(y // x)
                    check[y // x] = adds
            idx += 1
    if check[number] > 8:
        return -1
    return check[number]

N = 2
number = 11

N= 8
number = 53
print(solution(N, number))