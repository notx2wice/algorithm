
# 문제 설명
# 하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 
# 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 
# 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

# 제한 사항
# jobs의 길이는 1 이상 500 이하입니다.
# jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
# 각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
# 각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
import heapq

def solution(jobs):
    jobs.sort(key = lambda x : x[0])
    l = len(jobs)
    idx = 0
    time = 0
    asum = 0
    done = 0
    processing = [0,0,0]
    hq = []
    while time <= 3000 or done < l:
        #힙에 넣을 거 추가 한 후에 
        if idx < l :
            if jobs[idx][0] <= time:
                heapq.heappush(hq, [ jobs[idx][1] ,  jobs[idx][0]] )
                idx += 1
                continue
        # #작업중인지 확인 해서 
        if processing[0] :
            #작업 중이면 이번에 끝날 작업인가 확인.
            if processing[1] + processing[3] <= time:
                asum += (time - processing[2])
                processing[0] = 0
        if processing[0] == 0 :
            if hq :
                temp = heapq.heappop(hq)
                done += 1
                processing = [1, temp[0], temp[1], time]
        time += 1
    answer = asum // l
    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))