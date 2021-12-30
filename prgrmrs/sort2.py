
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer


numbers = [3,33,34,4,3333,332,334,3334,0,9,23,24,5,55,555,234,241,2323,4,243]
numbers = [1,10,100,1000]
numbers = [0,0]
numbers = [9,997,99,878,87]
numbers = [83,838,0, 1, 2]
print(solution(numbers))
