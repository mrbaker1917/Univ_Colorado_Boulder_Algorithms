def counterGame(n):
    # Write your code here
    turn = "Louise"
    def two_powers(n):
        i = 2
        while 2**i < n:
            i += 1
        if 2**(i-1) == n:
            return 1
        else:
            n -= 2**(i-1)
            return n
    while n > 1:
        n = two_powers(n)
        if n == 1:
            return turn
        else:
            if turn == "Louise":
                turn = "Richard"
            else:
                turn = "Louise"

    return turn

print(counterGame(132)) # Louise