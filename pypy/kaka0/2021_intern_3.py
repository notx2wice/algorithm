# !/usr/bin/python3
from collections import deque
def solution(n, k, cmd):
    bag500 = [0  for _ in range(2000)]
    table = [1  for _ in range(n)]
   # print(table)
    stack = deque()
    N = n
    idx = k
    for s in cmd:
        if s[0] == 'D':
            move = int(s[2:len(s)])
            s_flag = 0
            idx += 1
            while (idx % 500 != 0 ):
                if table[idx] == 1:
                    move -= 1
                if move == 0:
                    s_flag = 1
                    break
                idx += 1
            if s_flag == 0:
                bidx = idx // 500
                # bidx += 1
                hihi = 0
                while (move >= ( 500 - bag500[bidx])):
                    if (move == ( 500 - bag500[bidx])):
                        break
                    idx += 500
                    move -= (500 - bag500[bidx])
                    bidx+=1
                # idx = bidx * 500
                
                while (move != 0):
                    if table[idx] == 1:
                        move -= 1
                    if move == 0:
                        break
                    idx += 1
          #  print(s, idx, s_flag)
        elif s[0] == 'U':
            move = int(s[2:len(s)])
            s_flag = 0
          #  print(s, idx, move)

            idx -= 1
            while (idx % 500 != 499):
                if table[idx] == 1:
                    move -= 1
                if move == 0:
                    s_flag = 1
                    break
               # print(s, idx, move, table)
                idx -= 1

          #  print(s, idx, move, table)

            if s_flag == 0:
                bidx = idx // 500
                # bidx -= 1
                hihi = 0
                while (move >= ( 500 - bag500[bidx] )):
                    if (move == ( 500 - bag500[bidx] )):
                        break
                    idx -= 500
                    move -= (500 - bag500[bidx])
                    bidx-=1
                
                # idx = bidx * 500 + 499
                while (move != 0):
                    if table[idx] == 1:
                        move -= 1
                    if move == 0:
                        break
                    idx -= 1

        elif s[0] == 'C':
            table[idx] = 0
            stack.append(idx)
            bidx = idx // 500
            bag500[bidx] += 1
            # 인덱스 삭제 하고 알 맞은 인덱스 까지 가는 것에 정보 활용
            tidx = idx + 1
            s_flag = 0
            e_flag = 0
            if tidx == n:
                e_flag = 1
            
            if e_flag == 0:
                while tidx % 500 != 0:
                   # print(tidx)
                    if tidx == n:
                        e_flag = 1
                        break
                    if table[tidx] == 1:
                        s_flag = 1
                        idx = tidx
                        break
                    tidx += 1
                if tidx == n:
                    e_flag = 1
                #여기 까지 확인 tidx == 500의 배수가 됨
                if s_flag == 0 and e_flag != 1:
                    bidx += 1
                    if (bidx == N // 500 and N % 500 == bag500[bidx]):
                        e_flag = 1
                    if not e_flag:
                        while (bag500[bidx] == 500):
                            if (bidx == N// 500):
                                e_flag = 1
                                break
                            bidx += 1
                        if (bidx == N // 500 and N% 500 == bag500[bidx]):
                            e_flag = 1
                        # 여기?? 뭔가 이상
                        if not e_flag:
                            tidx = bidx * 500
                            if tidx == n:
                                e_flag = 1
                            if e_flag != 1:
                                while (table[tidx] != 1):
                                    if tidx == n:
                                        e_flag = 1
                                        break
                                    tidx += 1
                                if tidx != n and table[tidx] == 1:
                                    s_flag = 1
                                    idx = tidx
                                
            #역주행 시작
            if e_flag and s_flag == 0:
                s_flag = 0
                tidx = idx - 1
                while ( tidx % 500 != 499):
                    if (table[tidx] ):
                        idx = tidx
                        s_flag = 1
                        break
                    tidx -= 1
                if s_flag == 0:
                    bidx = idx // 500
                    bidx -= 1
                    while (bag500[bidx] == 500 and bidx != 0 ):
                        bidx -= 1
                    bidx += 1
                    tidx = 500 * bidx - 1
                    while (table[tidx] == 0):
                        tidx -= 1
                    idx = tidx   
          #  print(s, idx, s_flag)
  
        elif s[0] == 'Z':
            temp = stack.pop()
            table[temp] = 1
            bag500[temp // 500] -= 1
           # print(s, idx, s_flag)

    answer = ''
    for x in range(N):
        if(table[x] == 0):
            answer += 'X'
        else:
            answer += 'O'
    return answer