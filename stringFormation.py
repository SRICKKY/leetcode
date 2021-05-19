# String Formation
'''
Given an array of strings, each of the same length and a target string construct the target string using characters from the strings in the given array such that the indices of the characters in the order in which they are used to form a strictly increasing sequence. Here the index of character is the position at which it appears in the string. Note that it is acceptable to  use multiple characters from the same string.


Determine the number of ways to construct the target string. One construction is different from another if either the sequences of indices they use are different, or the sequences are same but there exists a character at some index such that it is chosen from a different string in these constructions. Since the answer can be very large, return the value modulo (10^9 + 7).
'''

# mod = 1000000007

mod = 10 ** 9 + 7
dp = [[-1 for i in range(1000)] for j in range(1000)]


def calculate(pos, prev, s, index):
    if pos == len(s):
        return 1

    if dp[pos][prev] != -1:
        return dp[pos][prev]

    c = ord(s[pos]) - ord('a');

    answer = 0
    for i in range(len(index[c])):
        if index[c][i] > prev:
            answer = (answer % mod + calculate(pos + 1, index[c][i], s, index) % mod) % mod

    dp[pos][prev] = answer

    # Store and return the solution for this subproblem 
    return dp[pos][prev]


def countWays(a, s):
    n = len(a)

    index = [[] for i in range(26)]
    
    for i in range(n):
        for j in range(len(a[i])):
            index[ord(a[i][j]) - ord('a')].append(j + 1)

    return calculate(0, 0, s, index)


# Driver Code 
if __name__ == '__main__':
    A = []
    A.append("adc")
    A.append("aec")
    A.append("erg")
    S = "ac"

    # A = ["valya", "lyglb", "vldoh"]
    # S = "val"

    # A = ["xzu", "dfw", "eor", "mat", "jyc"]
    # S = "cf"

    # A = ["afsdc", "aeeeedc", "ddegerg"]
    # S = "ae"

    print(countWays(A, S))
