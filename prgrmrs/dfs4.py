def dfs(choosed_ticket ,now,  answer, airdict, visited, max_ticket, answers):
    if choosed_ticket == max_ticket:
        answers.append(answer[:])
        return
    else :
        idx = 0
        for next in airdict[now]:
            if visited[now][idx] == 1:
                visited[now][idx] = 0
                answer.append(next)
                dfs(choosed_ticket + 1, next, answer, airdict, visited, max_ticket,answers)
                visited[now][idx] = 1
                answer.pop()
            idx += 1

def solution(tickets):
    answer = []
    answers = []
    airdict = dict()
    visited = dict()
    airset = set()

    for t in tickets:
        airset.add(t[0])
        airset.add(t[1])

    for airport in airset:
        airdict[airport] = []
        visited[airport] = []
    for t in tickets:
        airdict[t[0]].append(t[1])
        visited[t[0]].append(1)

    for lst in airdict:
        airdict[lst].sort()

    start = "ICN"
    answer.append("ICN")
    dfs(0, start ,answer, airdict, visited, len(tickets), answers)
    return answers[0]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))

