"""
에라토네스의 체.
"""
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1): # n == 4   :: 2 # n== 9 :: 2, 3
        if sieve[i] == True:         
            for j in range(2*i, n, i):
                sieve[j] = False
    
    return [i for i in range(2, n) if sieve[i] == True]

def solution(n):
    return len(prime_list(n + 1))

print(solution(100))