'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''


def uniquePaths(row: int, col: int) -> int:
	grid = [[0 for _ in range(col)] for _ in range(row)]

	for i in range(row): grid[i][0] = 1
	for j in range(col): grid[0][j] = 1

	for i in range(1, row):
		for j in range(1, col):
			grid[i][j] = grid[i-1][j] + grid[i][j-1]


	return grid[-1][-1]



print(uniquePaths(3, 7))
print(uniquePaths(3, 3))
print(uniquePaths(3, 4))