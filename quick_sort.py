import random
import time

def quicksort(items):
  if (len(items) <= 1):
    return items
  pivot = random.choice(items)
#   pivot = items[-1]
  less_than_pivot = [x for x in items if x < pivot]
  equal_to_pivot = [x for x in items if x == pivot]
  more_than_pivot = [x for x in items if x > pivot]
  return quicksort(less_than_pivot) + equal_to_pivot + quicksort(more_than_pivot)

n = 10**6
rand_list = [random.randint(1, n) for _ in range(n)]
start = time.perf_counter()
quicksort(rand_list)
print(time.perf_counter() - start)

''' Key takeaways: about quicksort is that if you choose pivots randomly, the worst case 
# time complexity is O(n^2) but the average case time complexity is O(nlogn). Hence, 
quicksort is used very often in practice.

QUIZ:
Question 1:
Consider a run of Quicksort over array A of size 8:
A = [4, 5, 7, 1, 3, 2, 6, 8]
Suppose we choose a pivot element uniformly at random from the elements of
A. Select all the correct answers from the list below.
3 / 3 points

With probability 1/8, the resulting two partitions will have 3 and 4 elements. (Wrong)
With probability 1/4, the resulting two partitions will have 3 and 4 elements. (Correct)
This is correrct since the choices that will ensure this happens are to choose either 4 or 5 as the pivot.

The probability that the element 8 or 1 is chosen is 1/4. (Correct)
This is correct since the choices that will ensure this happens are to choose either 1 or 8 as the pivot.

Question 2:
Consider an array of size n with distinct elements to be sorted using Quicksort with randomized pivoting.
Let us say that the partition is completely unbalanced and the two partitions have 0 and n-1 elements.
which are true:
The probability that all pivots chosen by the Quicksort run will lead to completely unbalanced partitions is 2(n-1)/n! (Correct)
Assume base case is encountered for arrays of size 1.
The probability of a completely unbalanced array is 1/n. (Wrong)
The probability of a completely unbalanced array is 2/n. (Correct)

Question 3:
Choose all the correct statements from the list below about Quicksort:

Suppose we chose the pivot by randomly choosing three elements and taking the median of the 
chosen three as the pivot, the running time of quicksort is now Θ(nlog(n)) in the expected case. (Correct, True, 
since this is more or less equivalent to a random choice of pivot and the analysis carries over with a few modifications.)

If it were possible to find the median element of an array in O(n) time worst case, then quicksort will run in 
Θ(nlog(n)) time in the worst case. (Correct, since it is possible to find the median and partition with the median as the pivot in 
O(n) time. This will cause roughly balanced partitions and the running time will become 
Θ(nlog(n)) even in the worst case.)

Suppose we chose the pivot by randomly choosing three elements and taking the median of the chosen three as the pivot, 
the running time of quicksort is now Θ(nlog(n)) in the worst case. (False, since in the unfortunate case that the three 
elements are the least or largest elements in the array, we will still have an unbalanced partition  that will lead to 
Θ(n^2) worst case running time.)

'''