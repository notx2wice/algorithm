#!/usr/bin/python3
N = int(input())
all_s = 0
abil = []
dp = [[0 for _ in range(100 * 500)] for _ in range(51)]
for _ in range(N):
    t = int(input())
    abil.append(t)
    all_s += t

dp[0][0] = 1
for i in range(N):
    for j in range(N//2, 0, -1):
        for k in range(500)