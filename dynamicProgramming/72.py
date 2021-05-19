'''
Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
'''


def editDistance(word1: str, word2: str) -> int:

    grid = [[ 0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

    for i in range(len(word2) + 1): grid[i][0] = i

    for j in range(len(word1) + 1): grid[0][j] = j

    for i in range(1, len(word2) + 1):
        for j in range(1, len(word1) + 1):

            if word1[j-1] == word2[i-1]:
                grid[i][j] = grid[i-1][j-1]
            else:
                grid[i][j] = min(grid[i-1][j], grid[i-1][j-1], grid[i][j-1]) + 1

    return grid[-1][-1]


print(editDistance("SATURDAY", "SUNDAY"))
print(editDistance("CAT", "CAR"))
print(editDistance("COMPUTER", "COMMUTER"))