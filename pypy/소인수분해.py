#!/usr/bin/python3
N = int( input() )

while (N > 1):
    x = 2
    while (x < N):
        if N % x == 0 :
            print(x)
            break
        x+=1
    if x == N:
        print(N)
        break
    N = N//x
