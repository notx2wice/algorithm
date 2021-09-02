#!/usr/bin/python3
import sys
import heapq
import math
sys.setrecursionlimit(10**5) # 5로 했을 떄 통과과 됨... 뭐지

def union(a, b, parent, height):
    pa = find_parent(a, parent)
    pb = find_parent(b, parent)
    if (pa == pb) :
        return
    else :
        parent[pb] = pa


def find_parent(a, parent):
    if (a == parent[a]) :
        return a
    else :
        parent[a] = find_parent(parent[a], parent)
        return parent[a]

def test():
    global m #글로벌 키워드 사용법 
    m = m + 1

class data:
    def __init__(self, end, value):
        self.end= end
        self.value = value

class node:
    def __init__(self, A, B):
        self.num= A
        self.value = B

    def __lt__(self, other):
        if self.value <= other.value:   #오름차순
            return True  #첫번재 변수가 같으면 두번재 변수로 내림차순
        else:
            return False

if __name__ == "__main__" :
    # n, m = map(int, sys.stdin.readline().split())
    # parent = [ x for x in range(n + 1)]
    # height = [1 for x in range(n + 1)]
    # for _ in range(m):
    #     a, b, c = map(int, sys.stdin.readline().split())
    #     if (a == 0):
    #         union(b,c, parent, height)
    #     elif (a == 1):
    #         if find_parent(b, parent) == find_parent(c, parent) :
    #             print("YES\n")
    #         else :
    #             print("NO\n")
    input = sys.stdin.readline

    V, E = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(V+1)]
    heap = []

    for _ in range(E):
        v1, v2, c = map(int, input().split())
        graph[v1].append([c, v2])

    cost = [math.inf] * (V+1)
    cost[start] = 0

    heapq.heappush(heap, [0, start])
    while(heap): #최단거리가 중복으로 큐에들어가는 경우가 있음!! 갔던데 가는경우
        prev_cost, node = heapq.heappop(heap)
        if cost[node] < prev_cost :
            continue
        for next_cost, vertex in graph[node]:
            if next_cost+prev_cost < cost[vertex]:
                cost[vertex] = next_cost+prev_cost
                heapq.heappush(heap, [next_cost + prev_cost, vertex])

    for i in range(1, len(cost)):
        if cost[i] != math.inf:
            print(cost[i])
        else:
            print("INF")