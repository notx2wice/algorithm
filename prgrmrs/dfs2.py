import itertools

check_arr = [ 0 for _ in range(10000000)]

def isPrime(num):
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True
    idx = 2
    while idx * idx <= num:
        if num % idx == 0:
            return False
        idx+=1
    return True


def solution(numbers):
    answer = 0
    idx = 1
    numbers = list(map(int, numbers))
    for idx in range(1, len(numbers) + 1):
        for choose in list( itertools.combinations(numbers, idx)):
            for per in list( itertools.permutations(choose)):
                temp = 0
                for x in per:
                    temp *= 10
                    temp += x
                if check_arr[temp] == 0:
                    check_arr[temp] = 1
                    if isPrime(temp):
                        answer+=1
        
    return answer

numbers = "17"
print(solution(numbers))

