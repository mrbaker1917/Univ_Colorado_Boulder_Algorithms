from min_heap import MinHeap

class MaxHeap:
    def __init__(self):
        self.H = [None]
        
    def size(self):
        return len(self.H)-1
    
    def __repr__(self):
        return str(self.H[1:])
        
    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] <= self.H[i//2],  f'Maxheap property fails at position {i//2}, parent elt: {self.H[i//2]}, child elt: {self.H[i]}'
    
    def max_element(self):
        return self.H[1]
    
    def bubble_up(self, index):
        # your code here
        assert index >= 1
        if index == 1:
            return
        parent_index = index // 2
        if self.H[parent_index] > self.H[index]:
            return
        else:
            self.H[parent_index], self.H[index] = self.H[index], self.H[parent_index]
            self.bubble_up(parent_index)
        
            
    
    def bubble_down(self, index):
        # your code here
        assert index >= 1 and index < len(self.H)
        if len(self.H) < 3:
            return
        left_child_index = index * 2
        right_child_index = index * 2 + 1
        left_child_value = self.H[left_child_index] if left_child_index < len(self.H) else float('-inf')
        right_child_value = self.H[right_child_index] if right_child_index < len(self.H) else float('-inf')
        if self.H[index] >= max(left_child_value, right_child_value):
            return
        max_child_value, max_child_index = max((left_child_value, left_child_index), (right_child_value, right_child_index))
        self.H[index], self.H[max_child_index] = self.H[max_child_index], self.H[index]
        self.bubble_down(max_child_index)
        
        
    
    # Function: insert
    # Insert elt into minheap
    # Use bubble_up/bubble_down function
    def insert(self, elt):
        # your code here
        self.H.append(elt)
        self.bubble_up(len(self.H)-1)
        
        
    # Function: delete_max
    # delete the largest element in the heap. Use bubble_up/bubble_down
    def delete_max(self):
        # your code here
        if self.size() == 0:
            return
        elif self.size() == 1:
            max_elt = self.H.pop()
            return max_elt
        else:
            max_elt = self.H[1]
            self.H[1] = self.H[-1]
            self.H.pop()
            self.bubble_down(1)
            return max_elt
        
h = MaxHeap()
print('Inserting: 5, 2, 4, -1 and 7 in that order.')
h.insert(5)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(2)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(4)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(-1)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(7)
print(f'\t Heap = {h}')
assert(h.max_element() == 7)
h.satisfies_assertions()

print('Deleting maximum element')
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 4)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 2)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == -1)
# Test delete_max on heap of size 1, should result in empty heap.
h.delete_max()
print(f'\t Heap = {h}')
print('All tests passed: 5 points!')


class MedianMaintainingHeap:
    def __init__(self):
        self.hmin = MinHeap()
        self.hmax = MaxHeap()
        
    def satisfies_assertions(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0
            return 
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1
            return 
        # 1. min heap min element >= max heap max element
        assert self.hmax.max_element() <= self.hmin.min_element(), f'Failed: Max element of max heap = {self.hmax.max_element()} > min element of min heap {self.hmin.min_element()}'
        # 2. size of max heap must be equal or one lessthan min heap.
        s_min = self.hmin.size()
        s_max = self.hmax.size()
        assert (s_min == s_max or s_max  == s_min -1 ), f'Heap sizes are unbalanced. Min heap size = {s_min} and Maxheap size = {s_max}'
    
    def __repr__(self):
        return 'Maxheap:' + str(self.hmax) + ' Minheap:'+str(self.hmin)
    
    def get_median(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0, 'Sizes are not balanced'
            assert False, 'Cannot ask for median from empty heaps'
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1, 'Sizes are not balanced'
            return self.hmin.min_element()
        # your code here
        if self.hmax.size() == self.hmin.size():
            return (self.hmax.max_element() + self.hmin.min_element()) / 2
        if self.hmax.size() + 1 == self.hmin.size():
            return self.hmin.min_element()
        
    
    # function: balance_heap_sizes
    # ensure that the size of hmax == size of hmin or size of hmax +1 == size of hmin
    # If the condition above does not hold, move the max element from max heap into the min heap or
    # vice versa as needed to balance the sizes.
    # This function could be called from insert/delete_median methods
    def balance_heap_sizes(self):
        # your code here
        if self.hmax.size() != self.hmin.size() or self.hmax.size()+1 != self.hmin.size():
            while self.hmax.size() > self.hmin.size():
                self.hmin.insert(self.hmax.max_element())
                self.hmax.delete_max()
            while self.hmin.size() > self.hmax.size()+1:
                self.hmax.insert(self.hmin.min_element())
                self.hmin.delete_min()
        
    
    def insert(self, elt):
        # Handle the case when either heap is empty
        if self.hmin.size() == 0:
            # min heap is empty -- directly insert into min heap
            self.hmin.insert(elt)
            return 
        if self.hmax.size() == 0:
            # max heap is empty -- this better happen only if min heap has size 1.
            assert self.hmin.size() == 1
            if elt > self.hmin.min_element():
                # Element needs to go into the min heap
                current_min = self.hmin.min_element()
                self.hmin.delete_min()
                self.hmin.insert(elt)
                self.hmax.insert(current_min)
                # done!
            else:
                # Element goes into the max heap -- just insert it there.
                self.hmax.insert(elt)
            return 
        # Now assume both heaps are non-empty
        # your code here
        if elt >= self.hmax.max_element():
            self.hmin.insert(elt)
        else:
            self.hmax.insert(elt)
        self.balance_heap_sizes()
        
        
    def delete_median(self):
        self.hmax.delete_max()
        self.balance_heap_sizes()