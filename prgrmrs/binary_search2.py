'''
징검다리
문제 설명
출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 
그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 
바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.

제거한 바위의 위치	각 바위 사이의 거리	거리의 최솟값
            0    [2, 11, 14, 17, 21]    25
               [2, 9,   3,  3,  4,  4] 여기서 n번 째 이려남.
[2,11]  [0,14,17,21,25] [14,3,4,4] 3
[2,14]  [0,11,17,21,25] [11,6,4,4] 4
[2,17]  [0,11,14,21,25] [11,3,7,4] 3
[2,21]  [0,11,14,17,25] [11,3,3,8] 3

[11,14] [0,2,17,21,25]  [2,15,4,4] 2
[11,17] [0,2,14,17,25]  [2,12,3,8] 2
[11,21] [0,2,17,21,25]  [2,15,4,4] 2

[14,17] [0,2,11,21,25] [2,9,10,4] 2
[14,21] [0,2,11,17,25] [2,9,6,8] 2

[17,21] [0,2,11,14,25] [2,9,3,11] 2

위에서 구한 거리의        최솟값 중에 가장 큰       값은 4입니다.

출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 
제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 
가장 큰 값을 return 하도록 solution 함수를 작성해주세요.

제한사항
도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
바위는 1개 이상 50,000개 이하가 있습니다.
n 은 1 이상 바위의 개수 이하입니다.
'''
from collections import defaultdict
#0  [2, 11, 14, 17, 21]  25
def cal(mid,rocks):
    removed = 0
    prev = 0
    for rock in rocks:
        if mid > rock - prev:
            removed += 1
        else :
            prev = rock
    return removed

def find(start, end, rocks, n):
    mid = (start + end) //2
    too_short = cal(mid, rocks)
    if start >= end :
        if too_short <= n :
            return mid
        else :
            -999
    if too_short <= n:
        return max(mid, find(mid + 1, end, rocks,n))
    elif too_short > n:
        return find(start ,mid - 1, rocks, n)

def solution(distance, rocks, n):
    rocks.sort()
    return find(0, distance + 1, rocks, n)


distance = 23
rocks = [3, 6, 9, 10, 14, 17]
n = 2 # ans == 4

# distance = 25
# rocks = [2, 11, 14, 17, 21] 
# n = 2

print(solution(distance, rocks, n))