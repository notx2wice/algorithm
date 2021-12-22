def solution(brown, yellow):
    answer = []
    subanswer = []
    total = brown + yellow
    idx = 3
    while idx * idx <=total:
        if (total % idx) == 0:
            subanswer.append([total //idx, idx])
        idx += 1

    for x in subanswer:
        if (x[0] - 2) * (x[1] - 2) == yellow:
            answer.append(x[0])
            answer.append(x[1])
            return answer
    return answer


brown = 8
yellow = 1
print(solution(brown, yellow))