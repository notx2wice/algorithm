# !usr/bin/python3
import heapq
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

def solution(n, start, end, roads, traps):
    answer = [2000000000]
    s_traps = set()
    d_traps = dict()
    idx = 0
    for x in traps:
        s_traps.add(x)
        d_traps[x] = idx
        idx += 1
    d_road = [ []  for _ in range(n+1) ]
    r_road = [ []  for _ in range(n+1) ]
    cost1024 = [[2000000000 for _ in range(n + 1)] for _ in range(1025)] #[map][node]
    pq = [] #cost , current, trap_info

    for x in roads:
        d_road[x[0]].append( [x[1], x[2]]) #end cost
        r_road[x[1]].append( [x[0], x[2]])
    
    pq.append([0 , start, 0]) #cost , start, map_info
    min_end = 2000000000
    while pq:
        # print(pq , bin( pq[0][2]) )
        temp = heapq.heappop(pq)
        now_cost = temp[0]
        now_pos = temp[1]
        now_map = temp[2]

        if now_pos == end:
            if min_end > now_cost:
                min_end = now_cost

        if now_cost >= min_end :
            continue
        
        for road in d_road[now_pos]:  #end cost
            if now_pos not in s_traps and road[0] not in s_traps:
                if now_cost + road[1] > cost1024[now_map][road[0]] :
                    continue
                else:
                    cost1024[now_map][road[0]]  = now_cost + road[1]
                    heapq.heappush( pq, [cost1024[now_map][road[0]], road[0], now_map] )

            elif now_pos not in s_traps and road[0] in s_traps:
                if now_map & (1 << d_traps[road[0]]) > 0 : #흠...이거 앞에가 더크면 어케 되?
                    continue
                else :
                    new_map = now_map + (1 << d_traps[road[0]])
                    if now_cost + road[1] < cost1024[new_map][road[0]] :
                        cost1024[new_map][road[0]] = now_cost + road[1]
                        heapq.heappush(pq,[cost1024[new_map][road[0]], road[0], new_map] )

            elif now_pos in s_traps and road[0] not in s_traps:
                if now_map & (1 << d_traps[now_pos]) > 0 : # 0은 정방향이 아니면 아웃이라는 뜻
                    continue
                else:
                    if now_cost + road[1] < cost1024[now_map][road[0]] :
                        cost1024[now_map][road[0]]  = now_cost + road[1]
                        heapq.heappush( pq, [cost1024[now_map][road[0]], road[0], now_map] )

            else: # all in trap
                if now_map & (1 << d_traps[now_pos]) == 0 and now_map & (1 << d_traps[road[0]]) == 0 :
                    #둘다 꺼짐 -> 진행
                    new_map = now_map + (1 << d_traps[road[0]])
                    if now_cost + road[1]  < cost1024[new_map][road[0]] :
                        cost1024[new_map][road[0]] = now_cost + road[1]
                        heapq.heappush(pq, [cost1024[new_map][road[0]], road[0], new_map] )

                elif now_map & (1 << d_traps[now_pos]) == 0 and now_map & (1 << d_traps[road[0]]) > 0:
                    #넥스트만 꺼짐 -> 정지
                    continue
                elif now_map & (1 << d_traps[now_pos]) > 0 and now_map & (1 << d_traps[road[0]]) == 0:
                    #나우가 꺼짐 -> 정지
                    continue
                elif now_map & (1 << d_traps[now_pos]) > 0 and now_map & (1 << d_traps[road[0]]) > 0:
                    # 둘다 켜짐 -> 진행
                    new_map = now_map - (1 << d_traps[road[0]])
                    if now_cost + road[1]  < cost1024[new_map][road[0]] :
                        cost1024[new_map][road[0]] = now_cost + road[1]
                        heapq.heappush(pq, [cost1024[new_map][road[0]], road[0], new_map] )
        
        for road in r_road[now_pos]:
            if now_pos  not in s_traps and road[0] not in s_traps:
                continue
            elif now_pos not in s_traps and road[0] in s_traps:
                if now_map & (1 << d_traps[road[0]]) == 0 :
                    continue
                else :
                    new_map = now_map - (1 << d_traps[road[0]])
                    if now_cost + road[1] < cost1024[new_map][road[0]] :
                        cost1024[new_map][road[0]] = now_cost + road[1]
                        heapq.heappush(pq,[cost1024[new_map][road[0]], road[0], new_map] )

            elif now_pos in s_traps and road[0] not in s_traps:
                if now_map & (1 << d_traps[now_pos]) == 0 : # 1은 역방향이 아니면 아웃이라는 뜻
                    continue
                else:
                    if now_cost + road[1] < cost1024[now_map][road[0]] :
                        cost1024[now_map][road[0]]  = now_cost + road[1]
                        heapq.heappush( pq, [cost1024[now_map][road[0]], road[0], now_map] )
            else: # all in trap
                if now_map & (1 << d_traps[now_pos]) == 0 and now_map & (1 << d_traps[road[0]]) == 0 :
                    continue

                elif now_map & (1 << d_traps[now_pos]) == 0 and now_map & (1 << d_traps[road[0]]) > 0:
                    new_map = now_map - (1 << d_traps[road[0]])
                    if now_cost + road[1]  < cost1024[new_map][road[0]] :
                        cost1024[new_map][road[0]] = now_cost + road[1]
                        heapq.heappush(pq, [cost1024[new_map][road[0]], road[0], new_map] )
                    
                elif now_map & (1 << d_traps[now_pos]) > 0 and now_map & (1 << d_traps[road[0]]) == 0:
                    new_map = now_map + (1 << d_traps[road[0]])
                    if now_cost + road[1]  < cost1024[new_map][road[0]] :
                        cost1024[new_map][road[0]] = now_cost + road[1]
                        heapq.heappush(pq, [cost1024[new_map][road[0]], road[0], new_map] )

                else :
                    # 둘다 켜짐 -> 진행
                    continue
        # print(pq)

    answer[0] = min_end
    return answer[0]

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

# print( bin(7 & 4))
print(solution(n, start, end, roads, traps))