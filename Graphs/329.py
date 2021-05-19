# 329. Longest Increasing Path in a Matrix

def longestIncreasingPath(matrix):
        
        def dfs(i, j):
            # Check if visited
            if visited[i][j] != -1:
                return visited[i][j]

            res = 1

            # work with neighbors
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                
                # for each direction we try to find a new count
                direction_count = 0
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if matrix[i][j] < matrix[next_i][next_j]:
                        direction_count = 1 + dfs(next_i, next_j)

                res = max(direction_count, res)

            visited[i][j] = res
            return res

        
        # Check edge case
        if not matrix:
            return 0

        # Initialize
        rows, cols = len(matrix), len(matrix[0])
        visited = [[-1] * cols for _ in range(rows)]
        res = 0

        for row in range(rows):
            for col in range(cols):
                res = max(dfs(row, col), res)

        return res


    
print(longestIncreasingPath([
	[9,9,4],
	[6,6,8],
	[2,1,1]]
)) # 4 : 1 -> 2 -> 6 -> 9
print(longestIncreasingPath([
	[3, 4, 5],
	[11, 12, 6],
	[9, 8, 7]]
)) # 9 : 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 11 -> 12
