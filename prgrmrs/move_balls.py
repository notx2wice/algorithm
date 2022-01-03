# 문제 설명
# n행 m열의 격자가 있습니다. 격자의 각 행은 0, 1, ..., n-1번의 번호,
#  그리고 각 열은 0, 1, ..., m-1번의 번호가 순서대로 매겨져 있습니다. 
# 당신은 이 격자에 공을 하나 두고, 그 공에 다음과 같은 쿼리들을 날리고자 합니다.

# 열 번호가 감소하는 방향으로 dx칸 이동하는 쿼리 (query(0, dx))
# 열 번호가 증가하는 방향으로 dx칸 이동하는 쿼리 (query(1, dx))
# 행 번호가 감소하는 방향으로 dx칸 이동하는 쿼리 (query(2, dx))
# 행 번호가 증가하는 방향으로 dx칸 이동하는 쿼리 (query(3, dx))
# 단, 공은 격자 바깥으로 이동할 수 없으며, 목적지가 격자 바깥인 경우 공은 이동하다가 
# 더 이상 이동할 수 없을 때 멈추게 됩니다. 
# 예를 들어, 5행 × 4열 크기의 격자 내의 공이 3행 2열에 있을 때 query(3, 10) 쿼리를 받은 경우 
# 공은 4행 2열에서 멈추게 됩니다. 
# (격자의 크기가 5행 × 4열이므로, 0~4번 행과 0~3번 열로 격자가 구성되기 때문입니다.)

# 격자의 행의 개수 n, 열의 개수 m, 정수 x와 y, 그리고 쿼리들의 목록을 나타내는 
# 2차원 정수 배열 queries가 매개변수로 주어집니다. 
# n × m개의 가능한 시작점에 대해서 해당 시작점에 공을 두고 queries 
# 내의 쿼리들을 순서대로 시뮬레이션했을 때, x행 y열에 도착하는 
# 시작점의 개수를 return 하도록 solution 함수를 완성해주세요.
dc = [-1,1,0,0]
dr = [0,0,-1,1]
#... n, m이 10 ** 9 
#벽에 부디치면 멈 추는 것인듯.

def solution(n, m, x, y, queries):
    answer = 0
    size = len(queries)
    rs, re = x, x
    cs, ce = y, y

    i = size - 1
    while (i >= 0):
        di = queries[i][0]
        dst = queries[i][1]

        if (di == 0):
            if cs != 0:
                cs = cs + dst
            ce = ce + dst
            if ce > m -1:
                ce = m -1
        elif di == 1:
            cs = cs -dst
            if cs < 0:
                cs = 0
            if ce != m -1:
                ce = ce -dst
        elif di == 2:
            if rs !=0 :
                rs = rs + dst
            re = re + dst
            if re > n-1:
                re = n -1
        
        elif di == 3:
            rs = rs -dst
            if rs < 0:
                rs = 0
            if re != n-1:
                re = re -dst
        if rs > n -1 or re < 0 or cs > m -1 or ce < 0:
            return answer
        i -= 1
    answer = (re -rs + 1) * (ce - cs + 1)
    return answer

n = 2
m = 2
x = 0
y = 0
queries = [[2,1],[0,1],[1,1],[0,1],[2,1]]

n = 2
m = 5
x = 0
y = 1
queries = [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]

print(solution(n, m, x, y, queries))

# import heapq

# def solution(operations):
#     hq = []
#     for op in operations:
#         cmd , num = op.split()
#         if not hq :
#             continue

#         if cmd == 'I':
#             heapq.heappush(hq, int(num))
#             continue
#         if num == "-1":
#             heapq.heappop(hq)
#         else:
#             hq.remove(max(hq))

#     if hq :
#         return [max(hq), min(hq)]
#     else :
#         [0, 0]