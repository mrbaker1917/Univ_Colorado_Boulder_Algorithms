def magic_square(s):
    cols = [
        [s[0][0], s[1][0], s[2][0]],
        [s[0][1], s[1][1], s[2][1]],
        [s[0][2], s[1][2], s[2][2]],
    ]
    diags = [[s[0][0], s[1][1], s[2][2]], [s[0][2], s[1][1], s[2][0]]]
    sums = [
        sum(s[0]),
        sum(s[1]),
        sum(s[2]),
        sum(cols[0]),
        sum(cols[1]),
        sum(cols[2]),
        sum(diags[0]),
        sum(diags[1]),
    ]
    for row in s:
        print(sum(row))
    return all([sum == sums[0] for sum in sums[1:]])
def make_magic_square(s):
    result = 0
    for r in s:
        result += 15 - sum(r)
    return result

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
s1 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
s2 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
s3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

print(make_magic_square(s2))
