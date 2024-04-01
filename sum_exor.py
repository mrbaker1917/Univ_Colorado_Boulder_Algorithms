def sumXor(n):
    # Write your code here
    if n == 0:
        return 1
    number_of_zeros = bin(n).count('0')
    result = (2 ** number_of_zeros) // 2
    return result


print(sumXor(10**15))
