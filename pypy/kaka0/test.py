def solution(id_list, report, k):
    answer = []
    ac_list = []
    count_d = dict()
    user_d = dict()
    s_report = set()

    for x in report:
        if x in s_report:
            continue
        else :
            s_report.add(x)

    for x in id_list:
        count_d[x] = 0
        user_d[x] = list()

    for rpt in s_report:
        a, b = map(str,rpt.split())
        user_d[a].append(b)
        count_d[b] += 1

    for usr in id_list:
        temp = 0
        for u in user_d[usr]:
            if count_d[u] >= k:
                temp += 1
        answer.append(temp)

    return answer

if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    print(solution(id_list, report, k))