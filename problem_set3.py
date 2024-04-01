def swap(a, i, j):
    assert 0 <= i < len(a), f"accessing index {i} beyond end of array {len(a)}"
    assert 0 <= j < len(a), f"accessing index {j} beyond end of array {len(a)}"
    a[i], a[j] = a[j], a[i]


def tryPartition(a):
    # implementation of Lomuto partitioning algorithm
    n = len(a)
    pivot = a[n - 1]  # choose last element as the pivot.
    i = -1
    j = 0  # initialize i and j both to be 0
    for j in range(n - 1):  # j = 0 to n-2 (inclusive)
        # Invariant: a[0] .. a[i] are <= pivot
        #            a[i+1]...a[j-1] are > pivot
        if a[j] <= pivot:
            swap(a, i + 1, j)
            i = i + 1
    swap(a, i + 1, n - 1)  # place pivot in its correct place.
    return i + 1  # return the index where we placed the pivot


print(tryPartition([2, 3, 4, 5, 5]))


def testIfPartitioned(a, k):
    # TODO : test if all elements at indices < k are all <= a[k]
    #         and all elements at indices > k are all > a[k]
    # return TRUE if the array is correctly partitioned around a[k] and return FALSE otherwise
    assert 0 <= k < len(a)
    # your code here
    if k == 0:
        return a[k] < min(a[1:])
    elif k == (len(a) - 1):
        return a[k] >= max(a[:k])
    else:
        return max(a[:k]) <= a[k] and min(a[k + 1 :]) > a[k]


assert (
    testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 10, 23], 5) == True
), " Test # 1 failed."
assert (
    testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 11, 23], 4) == False
), " Test # 2 failed."
assert (
    testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 23, 21], 0) == True
), " Test # 3 failed."
assert (
    testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 22, 23], 9) == True
), " Test # 4 failed."
assert (
    testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 8, 23], 5) == False
), " Test # 5 failed."
assert (
    testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 13, 9, -11], 5) == False
), " Test # 6 failed."
assert (
    testIfPartitioned([4, 4, 4, 4, 4, 8, 9, 13, 9, 11], 4) == True
), " Test # 7 failed."
print("Passed all tests (10 points)")

def swap(a, i, j):
    assert 0 <= i < len(a), f'accessing index {i} beyond end of array {len(a)}'
    assert 0 <= j < len(a), f'accessing index {j} beyond end of array {len(a)}'
    a[i], a[j] = a[j], a[i]

def simplePartition(a, pivot):
    ## To do: partition the array a according to pivot.
    # Your array must be partitioned into two regions - <= pivot followed by elements > pivot
    ## If an element at the beginning of the array is already <= pivot in the beginning of the array, it should not
    ## be moved by the algorithm.
    # your code here
    i = -1
    j = 0
    n = len(a)
    for j in range(n - 1):
        if a[j] <= pivot: 
            swap(a, i + 1, j)
            i += 1
    swap(a, i + 1, n - 1)
    
    
            
def boundedSort(a, k):
    for j in range(1, k):
        simplePartition(a, j)

a = [1, 3, 6, 1, 5, 4, 1, 1, 2, 3, 3, 1, 3, 5, 2, 2, 4]
print(a)
simplePartition(a, 1)
print(a)
assert(a[:5] == [1,1,1,1,1]), 'Simple partition test 1 failed'

simplePartition(a, 2)
print(a)
assert(a[:5] == [1,1,1,1,1]), 'Simple partition test 2(A) failed'
assert(a[5:8] == [2,2,2]), 'Simple Partition test 2(B) failed'


simplePartition(a, 3)
print(a)
assert(a[:5] == [1,1,1,1,1]), 'Simple partition test 3(A) failed'
assert(a[5:8] == [2,2,2]), 'Simple Partition test 3(B) failed'
assert(a[8:12] == [3,3,3,3]), 'Simple Partition test 3(C) failed'

simplePartition(a, 4)
print(a)
assert(a[:5] == [1,1,1,1,1]), 'Simple partition test 4(A) failed'
assert(a[5:8] == [2,2,2]), 'Simple Partition test 4(B) failed'
assert(a[8:12] == [3,3,3,3]), 'Simple Partition test 4(C) failed'
assert(a[12:14]==[4,4]), 'Simple Partition test 4(D) failed'

simplePartition(a, 5)
print(a)
assert(a == [1]*5+[2]*3+[3]*4+[4]*2+[5]*2+[6]), 'Simple Parition test 5 failed'

print('Passed all tests : 10 points!')


from random import random

def dot_product(lst_a, lst_b):
    and_list = [elt_a * elt_b for (elt_a, elt_b) in zip(lst_a, lst_b)]
    return 0 if sum(and_list)% 2 == 0 else 1

# encode a matrix as a list of lists with each row as a list.
# for instance, the example above is written as the matrix
# H = [[0,1,0,1],[1,0,0,0],[1,0,1,1]]
# encode column vectors simply as a list of elements.
# you can use the dot_product function provided to you.
def matrix_multiplication(H, lst):
    # your code here
    return [dot_product(row, lst) for row in H]
    

# Generate a random m \times n matrix
# see the comment next to matrix_multiplication for how your matrix must be returned.
def return_random_hash_function(m, n):
    # return a random hash function wherein each entry is chosen as 1 with probability >= 1/2 and 0 with probability < 1/2
    # your code here
    return [[1 if random() >= 0.5 else 0 for _ in range(n)] for _ in range(m)]
    
A1 = [[0,1,0,1],[1,0,0,0],[1,0,1,1]]
b1 = [1,1,1,0]
c1 = matrix_multiplication(A1, b1)
print('c1=', c1)
assert c1 == [1,1,0] , 'Test 1 failed'

A2 = [ [1,1],[0,1]]
b2 = [1,0]
c2 = matrix_multiplication(A2, b2)
print('c2=', c2)
assert c2 == [1, 0], 'Test 2 failed'

A3 = [ [1,1,1,0],[0,1,1,0]]
b3 =  [1, 0,0,1]
c3 = matrix_multiplication(A3, b3)
print('c3=', c3)
assert c3 == [1, 0], 'Test 3 failed'

H = return_random_hash_function(5,4)
print('H=', H)
assert len(H) == 5, 'Test 5 failed'
assert all(len(row) == 4 for row in H), 'Test 6 failed'
assert all(elt == 0 or elt == 1 for row in H for elt in row ),  'Test 7 failed'

H2 = return_random_hash_function(6,3)
print('H2=', H2)
assert len(H2) == 6, 'Test 8 failed'
assert all(len(row) == 3 for row in H2),  'Test 9 failed'
assert all(elt == 0 or elt == 1 for row in H2 for elt in row ), 'Test 10 failed'
print('Tests passed: 10 points!')