import functools
from collections import defaultdict
from collections import deque
import sys

sys.setrecursionlimit(10**10)
def comp(a,b):
    return b - a

l = [1,3,2,3,2,15,4345,34,5]

l.sort(key = functools.cmp_to_key(comp))
print(l)


d = defaultdict(deque)
d["가"].append(3)
d["가"].append(4)
d["가"].appendleft(0)

print(d)