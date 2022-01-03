from collections import defaultdict
def solution(genres, plays):
    answer = []
    all_in = []
    idxs = [x for x in range(len(plays))]
    for x in range(len(plays)):
        all_in.append([ genres[x] , plays[x], x ])

    gensumdict = defaultdict(int)
    alldic = defaultdict(list)

    for t in all_in:
        alldic[t[0]].append([t[1], t[2]])
    

    #alldic의 내부를 정렬 해둔다. 앨범 판매순 > idx 순 2번 정렬하자.
    for t in alldic.values():
        t.sort(key = lambda x : x[1])
        t.sort(key = lambda x : x[0], reverse = True)

    #장르별 앨범 판매량을 구하고 정렬한다.
    for x in all_in:
        gensumdict[x[0]] += x[1]
    l = list(gensumdict.items())
    l.sort(key = lambda x: x[1] , reverse=True) # 장르 순서 찾기

    for genre in l:
        if len(alldic[genre[0]]) >= 2:
            answer.append(alldic[genre[0]][0][1])
            answer.append(alldic[genre[0]][1][1])

        else:
            answer.append(alldic[genre[0]][0][1])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop" ]
plays =	[500, 600, 150, 800, 2500]	#[4, 1, 3, 0]


# genres = ["classic", "pop", "classic", "classic", "pop" ,"basic"]
# plays =	[500, 600, 150, 800, 2500, 3100]	#[4, 1, 3, 0]
print(solution(genres, plays))