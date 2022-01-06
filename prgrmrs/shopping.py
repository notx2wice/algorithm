# 헐 길이가 짧은 걸 찾아야 함... 이어 받아서 여러번 하면 되긴 하겠네...

def find_end(start, gems, its):
    dumits = its.copy()
    while start < len(gems):
        if gems[start] in dumits:
            dumits.remove(gems[start])
        if not dumits:
            return start 
        start += 1
    return start

def find_start(end, gems, its):
    dumits = its.copy()
    while end > 0:
        if gems[end] in dumits:
            dumits.remove(gems[end])
        if not dumits:
            return end
        end -= 1
    return end

def solution(gems):
    its = set()

    for gem in gems:
        its.add(gem)

    gems = ["시발 박새영"] + gems
    gem_len = len(gems)
    min_width = gem_len
    answer = [1, gem_len]

    s, e = 1, 1
    while e < len(gems):
        e = find_end(s , gems, its) # 범위 초과 하면
        if e == gem_len:
            return answer
        s = find_start(e, gems, its)
        if s == 0 :
            return answer
        if e - s + 1 < min_width :
            min_width = e - s + 1
            answer = [s, e]
        s = s + 1
    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems = ["A", "B" ,"B", "C", "A", "B", "B", "A","B","C"]
gems = ["DIA", "EM", "EM", "RUB", "DIA"] #이런 케이스에서 틀리는 군.
print(solution(gems))