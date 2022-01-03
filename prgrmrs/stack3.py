from collections import deque

def solution(bridge_length, weight, truck_weights):
    time ,tdx ,wOnBr, done = 0,0,0,0
    qq = deque()
    while True:
        time += 1
        if qq:
            if time - qq[0][0] >= bridge_length:
                temp = qq.popleft()
                wOnBr -= temp[1]
                done += 1
                if done == len(truck_weights):
                    return time
        if tdx < len(truck_weights) and wOnBr + truck_weights[tdx] <= weight :
            qq.append([time,truck_weights[tdx]] )
            wOnBr += truck_weights[tdx]
            tdx += 1
    return time

bridge_length = 2
weight = 10
truck_weights =	[7,4,5,6]

# bridge_length = 100
# weight =	100
# truck_weights =	[10]

bridge_length = 100
weight =	100
truck_weights =	[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution(bridge_length, weight, truck_weights))