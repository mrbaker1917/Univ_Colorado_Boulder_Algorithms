def is_min_heap(a):
    d_a = {i + 1: x for i, x in enumerate(a)}
    mid = len(a) // 2
    for i in range(1, mid):
        if d_a[i] > d_a[i * 2] or d_a[i] > d_a[i * 2 + 1]:
            print(f"At index {i}, {d_a[i]} is greater than {d_a[i*2]} or {d_a[i*2+1]}")
            return False
    return True


l1 = [1,100,2,103,110,2,3]

print(is_min_heap(l1))
