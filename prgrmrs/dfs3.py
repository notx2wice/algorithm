from collections import deque

def match_words_len(word, next_word):
    agly = 0
    for x in range(len(word)):
        if (word[x] != next_word[x]):
            agly += 1
            target_idx = x
    if agly != 1:
        return 0
    elif agly == 1:
        return 1
    return 0


def solution(begin, target, words):
    answer = 0
    visited = set()
    visited.add(begin)
    qq = deque()
    qq.append([0, begin])
    while qq:
        move, word = qq.popleft()
        if word == target:
            return move
        for next_word in words:
            if next_word in visited :
                continue
            match_words = match_words_len(word, next_word)
            if match_words:
                visited.add(next_word)
                qq.append([move + 1, next_word])

    return answer

begin = "hit"	
target = "cog"	
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))