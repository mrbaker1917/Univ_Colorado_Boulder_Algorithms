def formingMagicSquare(s):
    # Write your code here
    from itertools import permutations

    def make_magic_square():
        all_magic_squares = []
        for square in permutations(range(1, 10)):
            if sum(square[:3]) == sum(square[3:6]) == sum(square[6:]):
                if (
                    square[0] + square[3] + square[6] == square[1] + square[4] + square[7] == square[2] + square[5] + square[8]
                ):
                    if (
                        square[0] + square[4] + square[8] == square[2] + square[4] + square[6]
                    ):
                        square = [list(square[:3]), list(square[3:6]), list(square[6:])]
                        all_magic_squares.append(square)
        return all_magic_squares

    all_magic_squares = make_magic_square()
    
    def costs_to_magic_square(s):
        costs = []
        for sq in all_magic_squares:
            cost = 0
            for i in range(3):
                for j in range(3):
                    cost += abs(sq[i][j] - s[i][j])
            costs.append(cost)
        return min(costs)
    return costs_to_magic_square(s)




s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
s1 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
s2 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
s3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]