# !usr/bin/python3

import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

def dfs(now, cost, d_road, r_road, trap_count, answer, end, s_traps):
    if now == end :
        if answer[0] > cost:
            answer[0] = cost
    
    else:
        if now in s_traps:
            for road in d_road[now] :
                # if road[2] == 1:
                #     continue
                if road[0] in s_traps:
                    if (trap_count[now] + trap_count[road[0]]) % 2 == 1 :
                        continue
                    else :
                        if road[3] < cost + road[1]:
                            continue
                        else:
                            road[3] = cost + road[1]
                        trap_count[road[0]] += 1
                        road[2] = 1
                        dfs(road[0], cost + road[1], d_road, r_road, trap_count, answer, end, s_traps)
                        trap_count[road[0]] -= 1
                        road[2] = 0
                else :
                    if (trap_count[now]) % 2 == 1:
                        continue
                    else :
                        if road[3] < cost + road[1]:
                            continue
                        else:
                            road[3] = cost + road[1]
                        road[2] = 1
                        dfs(road[0], cost + road[1], d_road, r_road, trap_count, answer, end, s_traps)
                        road[2] = 0
            for road in r_road[now] :
                # if road[2] == 1:
                #     continue
                if road[0] in s_traps:
                    if (trap_count[now] + trap_count[road[0]]) % 2 == 0 :
                        continue
                    else :
                        if road[3] < cost + road[1]:
                            continue
                        else:
                            road[3] = cost + road[1]
                        trap_count[road[0]] += 1
                        road[2] = 1
                        dfs(road[0], cost + road[1], d_road, r_road, trap_count, answer, end, s_traps)
                        trap_count[road[0]] -= 1
                        road[2] = 0
                else :
                    if (trap_count[now]) % 2 == 0:
                        continue
                    else :
                        if road[3] < cost + road[1]:
                            continue
                        else:
                            road[3] = cost + road[1]
                        road[2] = 1
                        dfs(road[0], cost + road[1], d_road, r_road, trap_count, answer, end, s_traps)
                        road[2] = 0

        else:
            for road in d_road[now] : #road :::: 0 = end, 1 = cost,  2 = visited
                # if road[2] == 1 :
                #     continue
                if road[0] in s_traps:
                    if trap_count[road[0]] % 2 == 0: #갈수 있다.
                        if road[3] < cost + road[1]:
                            continue
                        else:
                            road[3] = cost + road[1]
                        trap_count[road[0]] += 1
                        road[2] = 1
                        dfs(road[0], cost + road[1], d_road, r_road, trap_count, answer, end, s_traps)
                        trap_count[road[0]] -= 1
                        road[2] = 0
                    else :
                        continue
                else :
                    if road[3] < cost + road[1]:
                            continue
                    else:
                        road[3] = cost + road[1]
                    road[2] = 1
                    dfs(road[0], cost + road[1], d_road, r_road, trap_count, answer, end, s_traps)
                    road[2] = 0
            for road in r_road[now] :
                # if road[2] == 1 :
                #     continue
                if road[0] not in s_traps:
                    continue
                else :
                    if trap_count[road[0]] % 2 == 1:
                        if road[3] < cost + road[1]:
                            continue
                        else:
                            road[3] = cost + road[1]
                        trap_count[road[0]] += 1
                        road[2] = 1
                        dfs(road[0], cost + road[1], d_road, r_road, trap_count, answer, end, s_traps)
                        trap_count[road[0]] -= 1
                        road[2] = 0

def solution(n, start, end, roads, traps):
    answer = [2000000000]
    s_traps = set()
    
    for x in traps:
        s_traps.add(x)
        s_traps.add(x+n)
    
    d_road = [[]  for _ in range(2*(n+1))]
    r_road = [[]  for _ in range(2*(n+1))]

    pq = [] #cost , current, [trap_count]
    trap_count = dict()

    for x in traps:
        trap_count[x] = 0

    for x in roads:
        d_road[x[0]].append( [x[1], x[2] , 0, 2000000000]) #end cost visited
        r_road[x[1]].append( [x[0], x[2] , 0, 2000000000])
    
    dfs(start, 0, d_road, r_road, trap_count, answer, end, s_traps)

    return answer[0]

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

print(solution(n, start, end, roads, traps))