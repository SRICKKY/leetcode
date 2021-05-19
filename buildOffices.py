# Build Offices

from itertools import combinations
from collections import deque


def buildOffice(height, width, n):
    arr = []
    for i in range(height):
        for j in range(width):
            arr.append((i, j, 0))

    ans = float("inf")
    for points in combinations(arr, n):
        q = deque([])
        visited = set()

        for m, n, dist in points:
            q.append((m, n, dist))
            visited.add((m, n))

        distAns = 0
        distArr = []

        while q:
            i, j, dist = q.popleft()
            distAns = max(dist, distAns)
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < height and 0 <= y < width and (x, y) not in visited:
                    q.append((x, y, dist+1))
                    visited.add((x, y))
        ans = min(distAns, ans)

    return ans


# print(buildOffice(2, 3, 2))
print(buildOffice(5, 1, 1))
# print(buildOffice(2, 3, 2))
