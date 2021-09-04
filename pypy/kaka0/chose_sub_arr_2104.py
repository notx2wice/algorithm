import sys
n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
ans = 0
arr.append(0)
stack = []
stack.append([-1,0]) #sum, value
for x in range(n + 1):
    if arr[x] > stack[-1][1]:
        if arr[x] ** 2 > ans:
            ans = arr[x] ** 2
        stack.append([ arr[x], arr[x] ])
    elif arr[x] == stack[-1][1]:
        stack[-1][0] += arr[x]
    elif arr[x] < stack[-1][1]:
        temp = arr[x]
        ttemp = 0
        while arr[x] <= stack[-1][1] and len(stack) != 1:
            temp += stack[-1][0]
            ttemp += stack[-1][0]
            if stack[-1][0] * stack[-1][1] > ans:
                ans = stack[-1][0] * stack[-1][1]
            if ttemp * stack[-1][1] > ans:
                ans = ttemp * stack[-1][1]
            stack.pop()
        stack.append([temp, arr[x]])
print(ans)