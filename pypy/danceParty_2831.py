#!/usr/bin/python3
import sys
import math
import heapq

if __name__ == "__main__":
    global N
    N = int( input() )
    pgirl = []
    ngirl = []
    pboy = []
    nboy = []
    for g in map(int, sys.stdin.readline().split()) :
        if  g > 0:
            heapq.heappush(pgirl, g)
        else:
            heapq.heappush(ngirl, -1 * g)
    for g in map(int, sys.stdin.readline().split()) :
        if  g > 0:
            heapq.heappush(pboy, g)
        else:
            heapq.heappush(nboy, -1 * g)
    
    # girl = sorted(girl, key = abs) # sorted 는 재할당을 해줘야함
    #boy = sorted(boy , key = lambda x:abs(x))
    # boy.sort(key = lambda x : abs(x))
    answer = 0
    while (pgirl and nboy): #젤 작은 놈 부터 팝 
        if (nboy[0] > pgirl[0]):
            heapq.heappop(nboy)
            heapq.heappop(pgirl)
            answer += 1
        else:
            heapq.heappop(nboy)
     
    while (ngirl and pboy):
        if (pboy[0] < ngirl[0]):
            heapq.heappop(pboy)
            heapq.heappop(ngirl)
            answer += 1
        else:
            heapq.heappop(ngirl)
    print(answer)


# 7
# -1900 -2000 -2500 1500 1600 2500 -2500 
# 1700 1800 2200 -1550 2100 -2500 -1700 
