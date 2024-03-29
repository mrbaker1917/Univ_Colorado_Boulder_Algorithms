'''Found the k-th smallest element in an array using quick select algorithm'''

import random
import numpy as np
import time

def quick_select(a, k):
    if len(a) == 1:
        return a[0]
    pivot = random.choice(a)
    less_than_pivot = [x for x in a if x < pivot]
    equal_to_pivot = [x for x in a if x == pivot]
    more_than_pivot = [x for x in a if x > pivot]
    if k <= len(less_than_pivot):
        return quick_select(less_than_pivot, k)
    elif k <= len(less_than_pivot) + len(equal_to_pivot):
        return pivot
    else:
        return quick_select(more_than_pivot, k - len(less_than_pivot) - len(equal_to_pivot))

n = 10**8
k = n//2
a = [random.randint(2, n) for _ in range(n)]
start = time.perf_counter()
print(quick_select(a, k))
print(time.perf_counter() - start)
