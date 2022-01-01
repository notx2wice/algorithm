from collections import deque

def there_is_bigger(prior):
    idx = 0
    while idx < len(prior):
        if (prior[0] < prior[idx]):
            return idx
        idx += 1
    return 0
def solution(priorities, location):
    answer = 0
    prior = deque(priorities)
    t_list = [0 for _ in range(len(priorities))]
    t_list[location]  = 1
    loca = deque(t_list)
    while prior:
        bdx = there_is_bigger(prior)
        if bdx:
            cdx = 0
            while cdx < bdx:
                t = loca.popleft()
                loca.append(t)
                t = prior.popleft()
                prior.append(t)
                cdx+=1
        else:
            prior.popleft()
            flag = loca.popleft()
            answer+=1
            if flag:
                return answer
    return "it cant be printed"
# priorities	location	return
priorities = [2, 1, 3, 2]	
location = 2	#1
priorities =  [1, 1, 9, 1, 1, 1]
location = 0	# 5
print(solution(priorities, location))