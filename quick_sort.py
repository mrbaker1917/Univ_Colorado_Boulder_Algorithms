import random
import time

def quicksort(items):
  if (len(items) <= 1):
    return items
  pivot = random.choice(items)
  less_than_pivot = [x for x in items if x < pivot]
  equal_to_pivot = [x for x in items if x == pivot]
  more_than_pivot = [x for x in items if x > pivot]
  return quicksort(less_than_pivot) + equal_to_pivot + quicksort(more_than_pivot)

n = 1000000
rand_list = [random.randint(1, n) for _ in range(n)]
start = time.perf_counter()
quicksort(rand_list)
print(time.perf_counter() - start)