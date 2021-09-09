import sys
input = sys.stdin.readline

while True:
    inp = list(map(int,input().split()))
    n = inp[0]
    if n == 0:
        break
    ans = 0
    a = inp[1:]
    a.append(0)
    stack = []
    stack.append([-1,0])
    for x in range(0,n + 1):
        if a[x] < stack[-1][1] :
            while stack[-1][1] > a[x] :
                t = stack.pop()
                if ans < (x - t[0]) * t[1] :
                    ans = (x - t[0]) * t[1]
            stack.append([t[0], a[x]])
        elif a[x] == stack[-1][1] :
            continue
        else :
            stack.append([x, a[x]])
    print(ans)