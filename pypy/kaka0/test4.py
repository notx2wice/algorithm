def dfs(idx,n, info ,ryan , answer, flag, shoot):
    if idx > 10 or shoot == 0:
        if shoot > 0 :
            ryan[idx - 1] += shoot
        a_point = 0
        r_point = 0
        for x in range(11):
            if (info[x] < ryan[x]):
                r_point += (10 - x)
            elif info[x] > ryan[x]:
                a_point += (10 - x)
            elif info[x] == 0 and ryan[x] == 0:
                continue
            elif info[x] == ryan[x]:
                a_point += (10 - x)

        if r_point - a_point >= flag[0]:
            if flag[0] == r_point - a_point:
                for k in range(10,-1,-1):
                    if ryan[k] == answer[k] :
                        continue
                    if ryan[k] > answer[k] :
                        for t in range(11):
                            answer[t] = ryan[t]
                        break
                    else :
                        break
            if r_point - a_point > flag[0]:   
               for t in range(11):
                   answer[t] = ryan[t]
            flag[0] = r_point - a_point
        ryan[idx -1] = 0
    else:
        for x in range(shoot + 1):
            if x > shoot:
                return
            if info[idx] +1 <= ryan[idx]:
                return
            else:
                ryan[idx] = x
                dfs(idx + 1,n, info, ryan, answer, flag, shoot - x)
                ryan[idx] = 0

def solution(n, info):
    flag = [0] # 최대 점수를 담아 야겠다.
    answer = [0 for _ in range(11)]
    t_ans = []
    ryan = [0 for _ in range(11)]
    dfs(0,n, info, ryan ,answer, flag, n)
    if flag[0] == 0:
        return [-1]
    else:
        return answer

if __name__ == "__main__":
    n = 10
    info = [0,0,0,0,0,0,0,0,3,4,3]
    
    print(solution(n, info))