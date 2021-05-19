'''
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

'''

from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1: return 0

    dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
    
    dp[0][0] = 1

    for r in range(len(obstacleGrid)):
        for c in range(len(obstacleGrid[0])):
            if obstacleGrid[r][c] == 0:
                dp[r][c] += dp[r - 1][c] if r - 1 >= 0 else 0
                dp[r][c] += dp[r][c - 1] if c - 1 >= 0 else 0
                
    return dp[-1][-1]


print(uniquePathsWithObstacles(
	[
		[0,0,0],
		[0,1,0],
		[0,0,0]
	])
)
print(uniquePathsWithObstacles(
	[
		[0,1],
		[0,0]
	])
)
print(uniquePathsWithObstacles(
	[
		[0,0,1],
		[0,1,0],
		[0,0,0]
	])
)
