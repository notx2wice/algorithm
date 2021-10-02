def is_prime(nu):
    idx = 2
    if nu == 1:
        return 0
    if nu == 2:
        return 1
    while idx * idx <= nu :
        if nu % idx == 0:
            return 0
        idx+=1
    return 1

def solution(n, k):
    k_str = str()
    answer = 0
    while ( n > 0):
        p = n//k
        q = n%k
        k_str = str(q) + k_str
        n = p
    num_l = []
    for x in map(str, k_str.split('0')):
        if x == '':
            continue
        num_l.append(int(x))
    for x in num_l:
        if is_prime(x) == 1:
            answer += 1
    return answer

if __name__ == "__main__" :
    n = 437674
    k = 3
    # n = 110011
    # k = 10
    print(solution(n, k))