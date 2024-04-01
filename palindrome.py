def palindromeIndex(s):
    # Write your code here
    def is_palin(s1):
        length_s = len(s1)
        mid = length_s // 2
        if length_s % 2 == 0:
            if s1[:mid] == s1[mid:][::-1]:
                return -1
        else:
            if s1[:mid] == s1[mid+1:][::-1]:
                return -1
    
    if is_palin(s) == -1:
        return -1
    else:
        for i in range(len(s)):
            s1 = s[:i] + s[i+1:]
            if is_palin(s1) == -1:
                return i
        return -1

# print(palindromeIndex("aaabaaa"))

with open("palin_data.txt") as f:
    lines = f.readlines()
    for line in lines:
        print(line, palindromeIndex(line.strip()))